import re
import subprocess
import optional_modules

def solve(path):
	# stegextract
	optional_modules.stegextract(path)

	# strings
	data = subprocess.Popen(["strings",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM STRINGS:\n\n")
		f.close()	
		
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()

	# pngcheck
	data = subprocess.Popen(["pngcheck",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM PNGCHECK:\n\n")
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
	
	# extras
	optional_modules.exiftool(path)
	optional_modules.binwalk(path)
	optional_modules.xxd(path)
