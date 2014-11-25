ASU-FA14-CSE310-HW5
===================

Hey guys I just wanted to put this up in case I end up breaking something, but also so you could take a look at what I have so far. You can input the input.txt file through terminal with 'python maxprofit.py input.txt'. I don't know if that works for Windows but it does for Linux.


###Commit: Update so now edges are beautiful###
Okay so I finally got edges to work really nicely. At the end it prints the edges in an unordered form. If you would like to see them in an ordered form then add 'from collections import OrderedDict' at the top and change the definition of edges (line 44) to 'OrderedDict()' instead of '{}'. I hope I'm making progress in the right direction.
