#!/usr/bin/env python
#This is the prototype process for outputting the .dot files.
#Shamelessly inspired by the CSE 310 HW 5 assignment instructions.

import sys
import string

def make_dotfiles(dotstring,numV):
	names=[0]*numV
	profit=[0]*numV
	adjacency=[[0]*numV for i in range(numV)]
	weight=[[0]*numV for i in range(numV)]
	dotstring="Graph G{\n"
	print dotstring
	dotstring=dotstring+ "	node [fillcolor=none];\n"
	print dotstring
	for i in range(0,numV):
		dotstring=dotstring+"	"+ i + "[label=%s %d;\n]" + names[i]+profit[i]
		print dotstring
		for j in range(0,numV):
			if(adjacency[i][j]==0):
				dotstring=dotstring+ "	"+ i+" -- "+ j+"[label="+weight[i][j]+"];\n"
				print dotstring
		dotstring="%s\n"
		print dotstring
	dotstring="};\n"
	print dotstring
