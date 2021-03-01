import re
import subprocess
import optional_modules

def solve(path):
	# pdf-parser
	data = subprocess.Popen(["pdf-parser","-a",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM PDF-PARSER:\n\n")
		f.close()	
		
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()


	# strings
	data = subprocess.Popen(["strings",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM STRINGS:\n\n")
		f.close()	
		
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()

	# carving
	data = subprocess.Popen(["foremost","-T",path,"-v"], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM FOREMOST:\n\n")
		f.close()	
		
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()

	optional_modules.exiftool(path)
	optional_modules.binwalk(path)
	optional_modules.xxd(path)
