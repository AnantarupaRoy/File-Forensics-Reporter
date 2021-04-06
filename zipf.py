
import subprocess
import re
from zipfile import ZipFile 
import sys
import hashlib


def solve(path):
	
	try:
		with ZipFile(path, 'r') as zip:
			zip.extractall() 

	except:
		data = subprocess.Popen(["zip2john",path], stdout=subprocess.PIPE)
		output=data.communicate()[0]
		# with open("hash","r") as f1:
		for line in output.split(b"\n"):
			if (re.search(path,line.decode()) or re.search(r"\*",line.decode()) and (not "ver" in line.decode())):
				hashvalue=line.decode()
				with open("Report.md","a") as f2:
					f2.write("\n\nHASH VALUE FROM JOHN:\n\n")
					f2.write(hashvalue+"\n")
				f2.close()
		# f1.close()

		data = subprocess.Popen(["fcrackzip","-u","-D","-p","/usr/share/wordlists/rockyou.txt",path], stdout=subprocess.PIPE)
		output=data.communicate()[0]
		with open("Report.md","a+b") as f:
			f.write(output)
			f.close()

 	

    	
