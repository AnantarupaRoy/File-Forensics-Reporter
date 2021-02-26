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
else:		
	print("unrecognised filetype")		
