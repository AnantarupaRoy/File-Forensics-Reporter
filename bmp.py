
import optional_modules
import subprocess

def solve(path):
	# strings
	optional_modules.strings(path)

	# stegseek
	optional_modules.stegseek(path)
	# LSB-steg
	optional_modules.lsb_steg(path)
	optional_modules.carving(path)


	optional_modules.exiftool(path)
	optional_modules.binwalk(path)
	optional_modules.xxd(path)
