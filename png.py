import re
import subprocess
import optional_modules

def solve(path):
	# stegextract
	optional_modules.stegextract(path)

	# strings
	optional_modules.strings(path)

	# pngcheck
	optional_modules.pngcheck(path)
	
	# zsteg
	optional_modules.zsteg(path)

	# LSB-steg
	optional_modules.lsb_steg(path)
	# extras
	optional_modules.exiftool(path)
	optional_modules.binwalk(path)
	optional_modules.carving(path)
	optional_modules.xxd(path)
