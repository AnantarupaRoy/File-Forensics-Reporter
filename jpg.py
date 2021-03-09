import re
import subprocess
import optional_modules

def solve(path):

	# stegextract
	optional_modules.stegextract(path)

	
	# strings
	optional_modules.strings(path)
	
		
	# stegseek
	optional_modules.stegseek(path)
	# outguess
	optional_modules.outguess(path)
	optional_modules.carving(path)

	optional_modules.exiftool(path)
	optional_modules.binwalk(path)
	optional_modules.xxd(path)
