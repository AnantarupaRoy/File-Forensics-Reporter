import subprocess
import re
import optional_modules

def olevba(path):
	data=subprocess.Popen(['olevba','-c',path],stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("OUTPUT FROM OLEVBA:\n\n")
		f.close()
	
	for line in output.split(b"\n"):
		if re.search(r"VBA",line.decode()):

			with open("Report.md","a+b") as f:
				f.write(line+b"\n")
				f.close()

def pyxswf(path):
	data=subprocess.Popen(['pyxswf','-x',path],stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("OUTPUT FROM PYXSWF:\n\n")
		f.close()
	
	for line in output.split(b"\n"):
		if re.search(r"http://decalage.info/python/oletools",line.decode()):
			continue
		elif re.search(r"https://github.com/decalage2/oletools/issues",line.decode()):
			continue
		else:
			with open("Report.md","a+b") as f:
				f.write(line+b"\n")
				f.close()

def msodde(path):
	data=subprocess.Popen(['msodde','-a',path],stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("OUTPUT FROM MSODDE:\n\n")
		f.close()
	
	for line in output.split(b"\n"):
		if re.search(r"http://decalage.info/python/oletools",line.decode()):
			continue
		elif re.search(r"https://github.com/decalage2/oletools/issues",line.decode()):
			continue
		elif re.search(r"THIS IS WORK IN PROGRESS",line.decode()):
			continue
		else:
			with open("Report.md","a+b") as f:
				f.write(line+b"\n")
				f.close()

def mraptor(path):

	data=subprocess.Popen(['mraptor',path],stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("OUTPUT FROM MRAPTOR:\n\n")
		f.close()
	
	for line in output.split(b"\n"):
		if re.search(r"http://decalage.info/python/oletools",line.decode()):
			continue
		elif re.search(r"https://github.com/decalage2/oletools/issues",line.decode()):
			continue
		elif re.search(r"THIS IS WORK IN PROGRESS",line.decode()):
			continue
		elif re.search(r"A=AutoExec",line.decode()):
			continue
		elif re.search(r"Exit code",line.decode()):
			continue
		else:
			with open("Report.md","a+b") as f:
				f.write(line+b"\n")
				f.close()

def unzip(path):

	data=subprocess.Popen(['unzip',path],stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("OUTPUT FROM UNZIP:\n\n")
		f.close()
	
	
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()


def solve(path):
	
	optional_modules.exiftool(path)
	optional_modules.xxd(path)
	olevba(path) # extract VBA macros
	pyxswf(path) # extract SWF objects
	msodde(path) # extract DDE links
	mraptor(path) # detect malicious VBA macros
	unzip(path)










