# main 74
# Sam Robson
import os
import sys
import glob
import re
import math
import numexpr
import xarray
import bottleneck
import numpy as np
import xlrd
import openpyxl
import datetime
import pandas as pd
import time
import warnings
import click
import inspect
from alacorder import get #
from alacorder import parse #
from alacorder import logs #
from alacorder import write #
from alacorder import config
import PyPDF2
from io import StringIO
try:
    import xlsxwriter
except ImportError:
    pass
table = ""
upick_table = ('''
Select preferred table output below.
	A:  Case Details
	B:  Fee Sheets
	C:  Charges (all)
	D:  Charges (disposition only)
	E:  Charges (filing only)

>> Enter A, B, C, D, or E to continue:

''')
pick_table = click.style(upick_table,bold=True)
ujust_table = ('''

EXPORT DATA TABLE: To export data table from case inputs, enter full output path. Use .xls or .xlsx to export all tables, or, if using another format (.csv, .json, .dta), select a table after entering output file path.

>> Enter path:

''')
just_table = click.style(ujust_table,bold=True)
uboth =  ('''

EXPORT FULL TEXT archive: To process case inputs into a full text archive (recommended), enter archive path below with file extension .pkl.xz.

EXPORT DATA TABLE: To export data table from case inputs, enter full output path. Use .xls or .xlsx to export all tables, or, if using another format (.csv, .json, .dta), select a table after entering output file path.

>> Enter path:

''')
both = click.style(uboth,fg='bright_white')
utitle = ('''

ALACORDER beta 74
© 2023 Sam Robson

Alacorder processes case detail PDFs into data tables suitable for research purposes. Alacorder also generates compressed text archives from the source PDFs to speed future data collection from the same set of cases.

ACCEPTED      /pdfs/path/   PDF directory           
INPUTS:       .pkl.xz       Compressed archive      

>> Enter input path: 

''')
title = click.style(utitle,fg='bright_white')
utext_p = ('''

>> Enter path to output text file (must be .txt): 

''')
text_p = click.style(utext_p,bold=True)

def print_help():
    ctx = click.get_current_context()
    click.echo(ctx.get_help())
    ctx.exit()

@click.command()
@click.option('--input-path','-in',required=True,prompt=title,help="Path to input archive or PDF directory", show_choices=False)
@click.option('--output-path','-out',prompt=both,help="Path to output table (.xls, .xlsx, .csv, .json, .dta) or archive (.pkl.xz)", show_choices=False)
@click.option('--count','-c',default=0, help='Max cases to pull from input',show_default=False)
@click.option('--table','-t', help="Table export choice")
@click.option('--append', '-a', default=False, help="Append cases if existing archive at output path", is_flag=True, show_default=True)
@click.option('--overwrite', '-o', default=False, help="Overwrite output path if exists (cannot be used with append mode)", is_flag=True, show_default=True)
@click.option('--launch', default=True, is_flag=True, help="Launch export in default application", show_default=True)
@click.option('--dedupe','-dd', default=False, is_flag=True, help="Remove duplicate cases from input archive",hidden=True)
@click.option('--log', default=False, is_flag=True, help="Print outputs to console upon completion")
@click.option('--warn','-w', default=False, is_flag=True, help="Print warnings from alacorder, pandas, and other dependencies to console", show_default=True, hidden=True)
@click.option('--no-write', default=False, is_flag=True, help="Do not export to output path",hidden=True)
@click.option('--no-prompt', default=False, is_flag=True, help="Skip confirmation prompts")
@click.option('--debug', default=False, is_flag=True, help="Prints extensive logs to console for development purposes")
@click.option('--no-batch', default=False,is_flag=True,help="Process all inputs as one batch")
def cli(input_path, output_path, count, table, append,overwrite, launch, dedupe, log, warn, no_write, no_prompt, debug, no_batch):
	"""

	ALACORDER beta 74

	Alacorder processes case detail PDFs into data tables suitable for research purposes. Alacorder also generates compressed text archives from the source PDFs to speed future data collection from the same set of cases.

	© 2023 Sam Robson  github.com/sbrobson959/alacorder
	"""

	## INPUT PATH
	if input_path == "help": # help alias
		print_help()

	if table == "all" and os.path.splitext(output_path)[1] != ".xls" and os.path.splitext(output_path)[1] != ".xlsx":
		table = ""

	cin = config.inputs(input_path)
	if cin.GOOD == True:
		is_full_text = cin.IS_FULL_TEXT
		queue = cin.QUEUE
		found = cin.FOUND
		click.echo(cin.ECHO)
	else:
		click.echo(cin.ECHO)
		raise Exception("Invalid input. Alacorder quit.")

	cout = config.outputs(output_path)
	if cout.GOOD == True:
		ext = cout.OUTPUT_EXT
		make = cout.MAKE
		is_appendable = bool(cout.IS_APPENDABLE)
		exists = cout.EXISTING_FILE
		OLD_ARCHIVE = cout.OLD_ARCHIVE
		old_count = cout.OLD_ARCHIVE_COUNT
		click.echo(cout.ECHO)
	else:
		click.echo(cout.ECHO)
		raise Exception("Invalid output. Alacorder quit.")

	cf = config.set(cin, cout, count=count, table=table, overwrite=overwrite, append=append, launch=launch, log=log, dedupe=dedupe, warn=warn, no_write=no_write, no_prompt=no_prompt, debug=debug)

	click.echo(cf.ECHO)

	if cf.GOOD == True and cf.TABLE == "NEEDS_TABLE_SELECTION" and (table == "" or table == None):
		pick = click.prompt(pick_table) # add str
		if pick == "A":
			table = "cases"
		elif pick == "B":
			table = "fees"
		elif pick == "C":
			table = "charges"
		elif pick == "D":
			table = "disposition"
		elif pick == "E":
			table = "filing"
		else:
			if warn:
				click.secho("WARNING: Invalid table selection - defaulting to \'cases\'...",fg='red')
			table = "cases"

	if not overwrite and os.path.isfile(output_path) and not cout.IS_APPENDABLE:
		if click.confirm(logs.echo_yellow("Existing file at output path will be written over! Continue?",echo=False)):
			overwrite = True
			click.echo("Reconfiguring...")
			cf = config.set(cin, cout, count=count, table=table, overwrite=overwrite, append=append, launch=launch, log=log, dedupe=dedupe, warn=warn, no_write=no_write, no_prompt=no_prompt, debug=debug, skip_echo=True)
			click.echo(cf.ECHO)
	if not append and not overwrite and cout.IS_APPENDABLE:
		if click.confirm(click.style("Appending to existing file at output path. Continue?",fg='bright_yellow',bold=True)):
			append = True
			click.echo("Reconfiguring...")
			cf = config.set(cin, cout, count=count, table=table, overwrite=overwrite, append=append, launch=launch, log=log, dedupe=dedupe, warn=warn, no_write=no_write, no_prompt=no_prompt, debug=debug)
			click.echo(cf.ECHO)
		else:
			overwrite = True
			click.echo("Reconfiguring...")
			cf = config.set(cin, cout, count=count, table=table, overwrite=overwrite, append=append, launch=launch, log=log, dedupe=dedupe, warn=warn, no_write=no_write, no_prompt=no_prompt, debug=debug)
			click.echo(cf.ECHO)

	if cf.OVERWRITE == True:
		os.remove(output_path)
		if cf.WARN:
			click.secho("Removed existing file at path...",fg='red')

	if cf.APPEND == True and log == True:
		click.secho(cf.INPUT_PICKLE,fg='blue')

	## REMOVE DUPLICATES NEED TO ACTUALLY MAKE IT DO THAT 
	if cf.DEDUPE == True:
		pass

	## START PARSE...()
	if cf.MAKE == "singletable" or cf.MAKE == "multiexport":
		parse.table(cf,table)
	elif cf.MAKE == "archive":
		write.archive(cf)
	else: 
		click.echo("Alacorder did not complete a task and quit.")

	if launch and cf.MAKE != "archive":
		click.launch(output_path)


if __name__ == "__main__":
	cli()
