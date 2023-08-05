import alac
import re
import pandas as pd
import warnings
import numpy as np
import math
import click
import time
import inspect

def getTotalBalance(text: str):
    try:
        trowraw = re.findall(r'(Total.*\$.*)', str(text), re.MULTILINE)[0]
        totalrow = re.sub(r'[^0-9|\.|\s|\$]', "", trowraw)
        if len(totalrow.split("$")[-1])>5:
            totalrow = totalrow.split(" . ")[0]
        tbal = totalrow.split("$")[3].strip().replace("$","").replace(",","").replace(" ","")
        tbal = float(tbal)
    except:
        tbal = np.nan
    return tbal
def getBalanceByCode(text: str, code: str):
    actives = re.findall(r'(ACTIVE.*\$.*)', str(text))
    fees = pd.Series(actives,dtype=str)
    fees_noalpha = fees.map(lambda x: re.sub(r'[^0-9|\.|\s|\$]', "", x))
    srows = fees.map(lambda x: x.strip().split(" "))
    drows = fees_noalpha.map(lambda x: x.replace(",","").split("$"))
    coderows = srows.map(lambda x: str(x[5]).strip() if len(x)>5 else "")
    balancerows = drows.map(lambda x: str(x[-1]).strip() if len(x)>5 else "")
    codemap = pd.DataFrame({
    'Code': coderows,
    'Balance': balancerows
    })
    matches = codemap[codemap.Code==code].Balance
    return matches.sum()
def getConvictionCodes(text) -> [str]:
    return alac.getCharges(text)[15]
def parse(conf, method, *args):
    path_in = conf['input_path']
    path_out = conf['table_out']
    max_cases = conf['count']
    out_ext = conf['table_ext']
    print_log = conf['log']
    warn = conf['warn']
    queue = conf['queue']
    no_write = conf['no_write']
    from_archive = False if conf['path_mode'] else True
    if warn == False:
        warnings.filterwarnings("ignore")
    batches = pd.Series(np.array_split(queue, math.ceil(max_cases / 1000)))
    batchsize = max(pd.Series(batches).map(lambda x: x.shape[0]))

    start_time = time.time()
    alloutputs = []
    uselist = False
    print(args)
    func = pd.Series(args).map(lambda x: 1 if inspect.isfunction(x) else 0)
    funcs = func.index.map(lambda x: args[x] if func[x]>0 else np.nan)
    funcs = funcs.dropna()
    no_funcs = func.index.map(lambda x: args[x] if func[x]==0 else np.nan)
    no_funcs = no_funcs.dropna()
    countfunc = func.sum().astype(int)

    print(f"COUNTFUNC:{countfunc}")
    column_getters = pd.DataFrame(columns=['Name','Method','Arguments'],index=(range(0,countfunc)))
    print(f"COUNTFUNC:{column_getters}")
    print(column_getters['Name'])
    df_out = pd.DataFrame()

    local_get = []


    for i, x in enumerate(funcs):
        if inspect.isfunction(x):
            print(i)
            column_getters.Name[i] = x.__name__
            column_getters.Method[i] = x

    for i, x in enumerate(args):
        if inspect.isfunction(x) == False:
            column_getters.Arguments.iloc[i-1] = x

    def ExceptionWrapperArgs(mfunc, x, *args):
        unpacked_args = args
        a = mfunc(x, unpacked_args)
        return a

    def ExceptionWrapper(mfunc, x):
        a = mfunc(x)
        return a

    with click.progressbar(batches) as bar:
        for i, c in enumerate(bar):
            exptime = time.time()
            b = pd.DataFrame()

            if from_archive == True:
                allpagestext = c
            else:
                allpagestext = pd.Series(c).map(lambda x: getPDFText(x))
            for i, getter in enumerate(column_getters.Method.tolist()):
                arg = pd.Series(column_getters.Arguments.tolist()[i])
                print(i, getter, arg)
                #try:
                if not arg.any():
                    name = getter.__name__
                    col = pd.DataFrame({
                        name: allpagestext.map(lambda x: ExceptionWrapper(getter, x))
                        })
                else:
                    name = getter.__name__
                    col = pd.DataFrame({
                        name: allpagestext.map(lambda x: ExceptionWrapperArgs(getter, x, arg))
                        })
                n_out = [df_out, col]
                df_out = pd.concat(n_out,axis=1)

            if no_write == False and (i % 5 == 0 or i == len(batches) - 1):
                alac.write(conf, df_out) # rem alac
    if not no_write:
        alac.write(conf, df_out) # rem alac
    allout = df_out.infer_objects()
    try:
        allout = allout.map(lambda x: x.values[0])
    except AttributeError:
        pass
    alac.log_complete(conf, start_time)
    return allout

a = alac.config("/Users/samuelrobson/Desktop/Tutwiler.pkl.xz","/Users/samuelrobson/Desktop/TutTables2.xlsx", max_cases=2000, print_log=True, launch=True)
parse(a, getTotalBalance, getBalanceByCode, "D999", getConvictionCodes)

