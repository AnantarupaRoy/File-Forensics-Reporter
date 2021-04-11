import re
import subprocess
import optional_modules

def solve(path):
	# pdf-parser
	optional_modules.pdf_parser(path)


	# carving
	optional_modules.carving(path)

	optional_modules.exiftool(path)
	
	optional_modules.xxd(path)
