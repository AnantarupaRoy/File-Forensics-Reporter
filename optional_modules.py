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

def stegextract(path):
	
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM STEGEXTRACT:\n\n")
		f.close()
	try:
		data = subprocess.Popen(["stegextract",path,"--outfile","out"], stdout=subprocess.PIPE)
		output=data.communicate()[0]
		with open("out","r") as f1:
			secret=f1.read()

		with open("Report.md","a") as f:
			f.write(secret)
			f.close()
	except:
		with open("Report.md","a") as f:
			f.write("\n\nNOTHING FROM STEGEXTRACT\n\n")
			f.close()

