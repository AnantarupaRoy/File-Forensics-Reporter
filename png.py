import re
import subprocess

def solve(path):

	# strings
	data = subprocess.Popen(["strings",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM STRINGS:\n\n")
		f.close()	
		
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()

	
	# zsteg
	data = subprocess.Popen(["zsteg", "-a",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM ZSTEG:\n\n")
		f.close()
		
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()
	
