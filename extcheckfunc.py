import re
import subprocess
import optional_modules
from colorama import init
from colorama import Fore
from colorama import deinit

init()

# This is a superficial analysis and can be wrong. In cases where the bytes are heavily damaged the tool 
# will not be able to identify the filetype it is most suited to be.
# This tool can only identify if the file is supposed to be a PNG,JPEG or WAV file based on some non-damaged 
# signature bytes

def solve(path):
	optional_modules.xxd(path)
	with open("xxd_output.md","r") as f:
		data=f.read()
		if (re.search(r"8950 4e47",data) or re.search(r"0d0a 1a0a",data) or re.search(r"4948 4452",data) or re.search(r"4945 4e44",data)):
			print(Fore.RED+"It might be a corrupted PNG file.")
		elif(re.search(r"4578 6966",data) or re.search(r"4a46 4946",data) or re.search(r"ffd9",data) or re.search(r"ffd8 ffe0",data) or re.search(r"ffd8 ffe1",data)):
			print(Fore.RED+"It might be a corrupted JPEG file.")
		elif(re.search(r"5249 4646",data) or re.search(r"5741 5645",data) or re.search(r"666d 74",data)):
			print(Fore.RED+"It might be a corrupted wav file.")
		
		else:
			print("unrecognised filetype")

		f.close()
	data = subprocess.Popen(["rm","xxd_output.md"], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	data = subprocess.Popen(["rm","Report.md"], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	deinit()


