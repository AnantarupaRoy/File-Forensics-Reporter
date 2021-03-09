import re
import subprocess
import optional_modules

def solve(path):
	# strings
	optional_modules.strings(path)
	# audio-spectro
	optional_modules.spectro(path)
	# lsb
	optional_modules.wavsteg(path)
	optional_modules.carving(path)

	optional_modules.exiftool(path)
	optional_modules.binwalk(path)
	optional_modules.xxd(path)
	
