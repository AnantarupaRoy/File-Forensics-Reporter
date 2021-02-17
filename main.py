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
print (details)


if('PNG' in details):
	import png
	print("png")
	png.solve(path)
		
elif('JPEG' in details):
	import jpg
	print("jpg")
	jpg.solve(path)
	
elif('wav' in details):
	import wav
	print("wav")
	wav.solve(path)
else:		
	print("unrecognised filetype")		
