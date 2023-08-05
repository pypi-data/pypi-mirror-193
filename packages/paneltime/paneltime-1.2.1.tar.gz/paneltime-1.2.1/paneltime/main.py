#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Todo: 



#capture singular matrix with test_small.csv
#make sure error in h function triggers an exeption


import numpy as np
import panel
import warnings
import model_parser
import maximize
import os
import time

N_NODES = 1
warnings.filterwarnings('error')
np.set_printoptions(suppress=True)
np.set_printoptions(precision=8)


def execute(model_string,dataframe, IDs_name, time_name,heteroscedasticity_factors,options,window,
			exe_tab,instruments, console_output, mp, paralell2):

	"""optimizes LL using the optimization procedure in the maximize module"""
	if not exe_tab is None:
		if exe_tab.isrunning==False:return
	datainput=input_class(dataframe,model_string,IDs_name,time_name, options,heteroscedasticity_factors,instruments, paralell2)
	if datainput.timevar is None:
		print("No valid time variable defined. This is required")
		return

	summary = doit(datainput,options,mp,options.pqdkm.value,window,exe_tab, console_output)
	
	return summary

class input_class:
	def __init__(self,dataframe,model_string,IDs_name,time_name, options,heteroscedasticity_factors,instruments, paralell2):
		
		model_parser.get_variables(self,dataframe,model_string,IDs_name,time_name,heteroscedasticity_factors,instruments,options)
		self.descr=model_string
		self.n_nodes = N_NODES
		self.paralell2 = paralell2
		self.args=None
		if options.arguments.value!="":
			self.args=options.arguments.value
			
def doit(datainput,options,mp,pqdkm,window,exe_tab, console_output):
	print ("Creating panel")
	pnl=panel.panel(datainput,options,pqdkm)			

	mp.send_dict({'panel':pnl})
	mp.collect('init')
	s = mp.dict_file.replace('\\','/')

	mp.exec(
			"panel.init()\n"
			f"mp.send_dict({{'panel':panel}})\n"
			"mp.collect('init')\n"
			"mp.exec('panel.init()', 'panelinit')\n"
			"mp.collect('panelinit')\n", 
			'panelinit')
	mp.collect('panelinit')
	pnl.init()
	
	if not options.parallel.value:
		mp = None
	if not mp.direct:
		summary = maximize.run(pnl, pnl.args.args_init, mp, window, exe_tab, console_output)
	else:
		summary =  maximize.maximize_single(pnl, pnl.args.args_init)
	
	return summary



def indentify_dataset(glob,source):
	try:
		window=glob['window']
		datasets=window.right_tabs.data_tree.datasets
		for i in datasets:
			data_source=' '.join(datasets[i].source.split())
			editor_source=' '.join(source.split())
			if data_source==editor_source:
				return datasets[i]
	except:
		return False
			

		
def identify_global(globals,name):
	try:
		variable=globals[name]
	except:
		variable=None	
	return variable