import re
import subprocess

# binwalk
# xxd
# exif
def binwalk(path):
	data = subprocess.Popen(["binwalk",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM BINWALK:\n\n")
		f.close()
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()

def xxd(path):
	data = subprocess.Popen(["xxd","-a",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nHEXDUMP OF FILE:\n\n")
		f.close()
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()
	
def exiftool(path):
	data = subprocess.Popen(["exiftool",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM EXIFTOOL:\n\n")
		f.close()
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()
