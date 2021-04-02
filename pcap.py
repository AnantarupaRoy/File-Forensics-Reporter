import subprocess
import optional_modules

def solve(path):
	
	optional_modules.binwalk(path)
	optional_modules.carving(path)
