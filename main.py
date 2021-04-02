import re
import subprocess
import extcheckfunc
import os
import sys

file=sys.argv[1]
path = os.path.abspath(file)

result = subprocess.run(["file",path], stdout=subprocess.PIPE)
result=str(result.stdout)
details=re.findall(r'\w+',result)


if('PNG' in details):
	import png
	print("png file")
	png.solve(path)
		
elif('JPEG' in details):
	import jpg
	print("jpeg file")
	jpg.solve(path)
	
elif('WAVE' in details):
	import wav
	print("wave file")
	wav.solve(path)
	
elif("text" in details):
	import text
	print("text file")
	text.solve(path)
	
elif("bitmap" in details):
	import bmp
	print("bitmap file")
	bmp.solve(path)
	
elif("PDF" in details):
	import pdf
	print("pdf file")
	pdf.solve(path)
	
elif("Zip" in details):
	import zipf
	print("zip file")
	zipf.solve(path)
	
elif('pcap' in details):
	import pcap
	print("pcap file")
	pcap.solve(path)
	
elif('Microsoft' in details and not 'WAVE' in details):
	import msoffice
	print("office file")
	msoffice.solve(path)

else:		
	print("unrecognised filetype")		
