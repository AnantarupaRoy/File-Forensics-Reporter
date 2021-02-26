import re
import subprocess
import optional_modules

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
	
		
	# stegseek
	data = subprocess.Popen(["stegseek",path,"/usr/share/wordlists/rockyou.txt"], stdout=subprocess.PIPE )
	output=data.communicate()[0]
	try:	
		filename=path+".out"
		with open(filename,"r") as f1:
			text = f1.read()
		with open("Report.md","a") as f:
			f.write("\n\n OUTPUT FROM STEGSEEK : \n\n")
			f.write(text)
			f.close()
	except:
		with open("Report.md","a") as f:
			f.write("no valid passphrase using stegseek")
			f.close()

	optional_modules.exiftool(path)
	optional_modules.binwalk(path)
	optional_modules.xxd(path)
				
	
	
	 
