#Hackwget
import os
import sys
import subprocess
from subprocess import *
link =input("Please input link exmp:http://google.com/x or http://google.com/test-x you must be enter all string befor (X)\n")
range1=int(input("Please Enter Sart Range Expm:0 \n"))
range2=int(input("Please Enter end Range Expm:10 \n "))
f = open('myfile.txt','w')
for i in list(range(range1,range2)):
	 f.write(('%s%s \n'%(link,i)))
	  # f = open('myfile.txt','w')
	 # f.write(test)
f.close()
proc = subprocess.Popen(['wget -c --retry-connrefused --tries=0 --timeout=5 -i  myfile.txt  && echo "WE GOT IT Please enter for exit" || echo "Failure Please Enter to exit"'], shell=True)
