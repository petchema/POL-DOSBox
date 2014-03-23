#!/usr/bin/python
import sys, os

tmp = sys.argv[1]
tmp = tmp.replace(" ","")
tmp = tmp.split("\\")

i = 0
for content in tmp:
	content2 = content.split(".")
	if(len(content2[0]) > 8):
		content2[0] = content2[0][0:6]+"~1" ## Fixme, we should consider the case if there are several files
		content = ".".join(content2)
	tmp[i] = content
	i+=1
	
tmp = "\\".join(tmp)
tmp = tmp.upper()
sys.stdout.write("%s\n" % tmp)
