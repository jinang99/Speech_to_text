import glob
import os


#Appending the contents of all the .txt files of the users to the final.txt file which will be uploaded to the LM Tool using webcrawler.py
f1 = open("C:\\sphinx\\final\\etc\\final.txt",'a')
files = glob.glob("C:\\sphinx\\final\\*.txt")
dic = []
for i in files:
	f = open(i,'r')
	while True:
			    line = f.readline()
			    line = line.rstrip('\n')
			    #print(line)
			    
			    if ("" != line):
			    	dic.append(line)
			    else:
			    	break
	dic.sort()
	for j in dic:
		f1.write(j+"\n")
	dic = []




	
	