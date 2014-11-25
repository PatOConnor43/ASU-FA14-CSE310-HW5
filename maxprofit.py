#!/usr/bin/env python
import sys
import re
import string

#So this function starts to build a graph for you. It is meant to add path by
#path until the while loop that calls it finishes. The graph is a dict.
def makeGraph(starting_node, ending_node, profit, time, aGraph):
    if not starting_node in aGraph:
        aGraph[starting_node] = [[ending_node, profit, time]]
    else:
        aGraph[starting_node].append([ending_node, profit, time])
        

#Read input file
inFile = sys.argv[1]
lines = open(inFile,'r').readlines()

#Use regular expresion to filter out anything that is not a number.
#This first number should be number of verticies
nVert = int(re.sub("[^0-9]", "", lines[0]))

#Some vertex information lists --WILL PROBABLY BE CHANGED--
verticies_name = []
verticies_profit = []
verticies = [verticies_name, verticies_profit]

#Same as verticies but with edges
nEdges = int(re.sub("[^0-9]", "", lines[nVert+1]))
edge_start = []
edge_end = []
edge_time =[]
edges = [edge_start, edge_end, edge_time]

#Making an empty dict for graph
graph = {}

#This loop appends to the vertex lists using regular expressions
for i in xrange(1, nVert+1):
    verticies_name.append(re.sub("[^a-zA-Z]", "", lines[i]))
    verticies_profit.append(re.sub("[^0-9]", "", lines[i]))

#This loop adds to edges using regular expressions
for j in xrange(nVert+2, nVert+nEdges+2):
    edge_start.append(lines[j].split()[0])
    edge_end.append(lines[j].split()[1])
    edge_time.append(lines[j].split()[2])


#Some loop variables
indexi = 0
indexj = 0
go = True

#This is where the magic happens... eventually. This loop is a liar. Currently it works,
#but the profit values are incorrect. Working on remedy on whiteboard. If you run it,
#it kind of looks nice though
for i in xrange(len(verticies_name)):
    while verticies_name[i] == edge_start[indexi] and go:
        makeGraph(edge_start[indexi], edge_end[indexi],verticies_profit[i] , edge_time[indexi], graph)
        if indexi < len(edge_start)-1:
            indexi += 1
        else:
            go = False
   
print graph

#These are just for checking values
"""
for x in range(nVert):
    print verticies[0][x] + " " + str(verticies[1][x])

for x in xrange(nEdges):
    print edges[0][x] + " " + edges[1][x] + " " +edges[2][x]
"""
