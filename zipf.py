
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
		BUF_SIZE = 32768 
		md5 = hashlib.md5()
		sha1 = hashlib.sha1()
		with open("Report.md","a")as f1:
			with open(path, 'rb') as f:

				while True:
					data = f.read(BUF_SIZE)
					if not data:
					  break
					md5.update(data)
					sha1.update(data)
			f1.write("MD5: {0}".format(md5.hexdigest())+"\n")
			f1.write("SHA1: {0}".format(sha1.hexdigest()))
			f.close()
		f1.close()
		data = subprocess.Popen(["fcrackzip","-u","-D","-p","/usr/share/wordlists/rockyou.txt",path], stdout=subprocess.PIPE)
		output=data.communicate()[0]
		with open("Report.md","a+b") as f:
			f.write(output)
			f.close()


    	
