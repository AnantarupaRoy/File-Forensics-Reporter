import subprocess
import optional_modules

def solve(path):
	# strings
	optional_modules.strings(path)
	optional_modules.stegsnow(path)
	optional_modules.carving(path)

	optional_modules.exiftool(path)
	optional_modules.binwalk(path)
	optional_modules.xxd(path)
