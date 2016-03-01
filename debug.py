#!/usr/bin/env python 
import sys, os

with open(os.path.dirname(os.path.realpath(__file__))+"contentfilter-"+sys.argv[2]+"-log.txt", "wb") as file:
    for i in range(len(sys.argv)):
        file.write(str(i)+": "+sys.argv[i]+"\n")
        
os._exit(1)