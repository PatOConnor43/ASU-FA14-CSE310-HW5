#!/usr/bin/env python
import sys
import re
import string


inFile = sys.argv[1]
lines = open(inFile,'r').readlines()
#nVert_str = re.sub("\D", "", lines[0])
nVert = int(re.sub("[^0-9]", "", lines[0]))
verticies_name = []
verticies_profit = []
verticies = [verticies_name, verticies_profit]

nEdges = int(re.sub("[^0-9]", "", lines[nVert+1]))
edge_start = []
edge_end = []
edge_time =[]
edges = [edge_start, edge_end, edge_time]

for i in xrange(1, nVert+1):
    verticies_name.append(re.sub("[^a-zA-Z]", "", lines[i]))
    verticies_profit.append(re.sub("[^0-9]", "", lines[i]))

for j in xrange(nVert+2, nVert+nEdges+2):
    edge_start.append(lines[j].split()[0])
    edge_end.append(lines[j].split()[1])
    edge_time.append(lines[j].split()[2])


for x in range(nVert):
    print verticies[0][x] + " " + str(verticies[1][x])

for x in xrange(nEdges):
    print edges[0][x] + " " + edges[1][x] + " " +edges[2][x]
    
