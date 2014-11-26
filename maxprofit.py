#!/usr/bin/env python
import sys
import re
import string
from collections import OrderedDict
"""
#So this function starts to build a graph for you. It is meant to add path by
#path until the while loop that calls it finishes. The graph is a dict.
def makeGraph(starting_node, ending_node, profit, time, aGraph):
    if not starting_node in aGraph:
        aGraph[starting_node] = [[ending_node, profit, time]]
    else:
        aGraph[starting_node].append([ending_node, profit, time])
        
"""

#This searches through each vertex in verticies to find one with a matching
#name and it returns the index in verticies where it was found
def findEnd(name_of_node, list_of_vert):
    
    for i in range(len(list_of_vert)):
        if name_of_node == list_of_vert[i][0]:
            return i



def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not start in graph:
            return []
        paths = []
        for key in graph:
            for entry in key:
                if not entry[0] in path:
                    newpaths = find_all_paths(graph, entry[0], end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
        return paths

#Didn't work as expected
"""
def deleteDead(newpaths, graph):
    for i in newpaths:
        for j in i:
            for k in graph[j]:
                if not i.next() in graph[j][k] and k == len(graph[j]):
                    return newpaths.remove(i)
    return newpaths
"""
#Read input file
inFile = sys.argv[1]
lines = open(inFile,'r').readlines()

#Use regular expresion to filter out anything that is not a number.
#This first number should be number of verticies
nVert = int(re.sub("[^0-9]", "", lines[0]))

#Some vertex information lists --WILL PROBABLY BE CHANGED--
#verticies_name = []
#verticies_profit = []
verticies = []

#Same as verticies but with edges
nEdge = int(re.sub("[^0-9]", "", lines[nVert+1]))
edge_start = []
edge_end = []
edge_time =[]
edges = OrderedDict()

#Making an empty dict for graph
graph = OrderedDict()

#This loop adds Verticies to the Verticies list in the form V = [Vertex_Name, Profit]
#So this list will look like Verticies = [V1, V2,..., Vn]
#To be clear, each V is a ---LIST--- so I will not be putting another set of [] around them
for i in range(1, nVert+1):
    verticies.append([re.sub("[^a-zA-Z]", "", lines[i]), re.sub("[^0-9]", "", lines[i])])

#This loop will create a dict of edges in the form edges['edge_name'] = [[V1],[V2],time]
#An example of the entire dict would be edges = {'V1V2':[V1, V2, time], ..., 'Vn-1Vn':[Vn-1, Vn, time]}
#This holds as long as the Verticies are actually connected, otherwise try anotherr pair
j = nVert+2
go = True
for i in range(len(verticies)):
    while lines[j].split()[0] == verticies[i][0] and go:
        findMe = lines[j].split()[1]
        index = findEnd(findMe, verticies)
        edges[lines[j].split()[0]+lines[j].split()[1]] = [verticies[i], verticies[index], lines[j].split()[2]]
        if j < len(lines)-1:
            j+=1
        else:
            go = False

#This creates a graph from the edges in the form graph[vertex_name] = [Connected_vertex, profit, time]
#So a complete graph would be represented as
#graph = {'A': [B, Profit, time], ..., 'B':[C, Profit, Time]..., ..., (until we get the final connections)}
for i in edges:
    ch = edges[i][0][0]
    if ch in graph:
        graph[ch].append([edges[i][1][0], edges[i][1][1], edges[i][2]])
    else:
        graph[ch] = [[edges[i][1][0], edges[i][1][1], edges[i][2]]]

paths=[]
paths = find_all_paths(graph, lines[1].split()[0], lines[nVert].split()[0])
print paths

#These are just for checking values
"""
for x in range(nVert):
    print verticies[0][x] + " " + str(verticies[1][x])

for x in xrange(nEdges):
    print edges[0][x] + " " + edges[1][x] + " " +edges[2][x]
"""
