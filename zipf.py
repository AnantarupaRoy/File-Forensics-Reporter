
import subprocess
import re
from zipfile import ZipFile 


def solve(path):
	try:
		with ZipFile(path, 'r') as zip:
			zip.extractall() 

	except:
		data = subprocess.Popen(["fcrackzip","-u","-D","-p","/usr/share/wordlists/rockyou.txt",path], stdout=subprocess.PIPE)
		output=data.communicate()[0]
		with open("Report.md","a+b") as f:
			f.write(output)
			f.close()


 	

    	
