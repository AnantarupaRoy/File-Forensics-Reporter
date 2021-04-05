import re
import subprocess


# binwalk
# xxd
# exif
pwd=subprocess.Popen(["pwd"], stdout=subprocess.PIPE)
location=pwd.communicate()[0]
def binwalk(path):
	data = subprocess.Popen(["binwalk",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\nOUTPUT FROM BINWALK:\n")
		f.close()
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()

def xxd(path):
	data = subprocess.Popen(["xxd","-a",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nHexdump of the file has been stored in xxd_output.md\n\n")
		f.close()
	with open("xxd_output.md","a+b") as f:
		f.write(output)
		f.close()
	
def exiftool(path):
	data = subprocess.Popen(["exiftool",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\nOUTPUT FROM EXIFTOOL:\n")
		f.close()
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()

def stegextract(path):
	
	with open("Report.md","a") as f:
		f.write("\nOUTPUT FROM STEGEXTRACT:\n")
		f.close()
	try:
		data = subprocess.Popen(["stegextract",path,"--outfile","out"], stdout=subprocess.PIPE)
		output=data.communicate()[0]
		with open("out","r") as f1:
			secret=f1.read()

		with open("Report.md","a") as f:
			f.write(secret)
			f.close()
	except:
		with open("Report.md","a") as f:
			f.write("\nNOTHING FROM STEGEXTRACT\n")
			f.close()

def strings(path):
	data = subprocess.Popen(["strings",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM STRINGS:\n\n")
		f.close()	

	for line in output.split():
			
			# print(line.decode())
		clean = ''.join(re.findall(r'\w',line.decode()))
		if (len(clean)>5):
			# print(clean)
		
			with open("Report.md","a") as f:
					
				f.write(clean+"\n")
				f.close()

def pngcheck(path):
	data = subprocess.Popen(["pngcheck",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\nOUTPUT FROM PNGCHECK:\n")
		f.close()	
		
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()

def zsteg(path):
	data = subprocess.Popen(["zsteg",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]

	with open("Report.md","a") as f:
		f.write("\nOUTPUT FROM ZSTEG:\n")
		f.close()

		
	with open("Report.md","a+b") as f:
		for line in output.split(b"\r"):
			
			if re.search(r'\.\.\s\S',line.decode()):
				
				f.write(line)
		f.close()

def stegseek(path):
	data = subprocess.Popen(["stegseek",path,"/usr/share/wordlists/rockyou.txt"], stdout=subprocess.PIPE )
	output=data.communicate()[0]
	with open("Report.md","a") as f:
			f.write("\nOUTPUT FROM STEGSEEK : \n")
	try:	
		filename=path+".out"
		with open(filename,"r") as f1:
			text = f1.read()
		with open("Report.md","a") as f:
			
			f.write(text)
			f.close()
	except:
		with open("Report.md","a") as f:
			f.write("no valid passphrase using stegseek")
			f.close()

def spectro(path):
	subprocess.run(['sox', path , '-n','spectrogram'])
	
		
	with open("Report.md","a") as f:
		f.write("A spectrogram of the audio file has been created in spectrogram.png file.\n\n")
		f.close()

def wavsteg(path):
	data = subprocess.Popen(["stegolsb","wavsteg","-r","-i",path,"-o","output.txt","-b","5000"], stdout=subprocess.PIPE )
	output=data.communicate()[0]
	# try:	
	filename="output.txt"
	with open(filename,"rb") as f1:
		text = f1.read()
	with open("Report.md","a") as f:
		f.write("\n\n OUTPUT FROM STEGO-LSB: \n\n")
		f.close()
	with open("Report.md","a+b") as f2:
		f2.write(text)

def outguess(path):
	data = subprocess.Popen(["outguess","-r",path,"outguess_answer.txt"], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\nOUTPUT FROM OUTGUESS:\n")
		f.close()	
		
	try:	
		
		with open("outguess_answer.txt","r") as f1:
			text = f1.read()
		with open("Report.md","a") as f:
			f.write(text)
			f.close()
	except:
		with open("Report.md","a") as f:
			f.write("no data from outguess")
			f.close()

def lsb_steg(path):
	
	data = subprocess.Popen(["stegolsb","steglsb","-r","-i",path,"-o","outfile.zip","-n","2"], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	try:
		with open("Report.md","a") as f:
			f.write("\n\nThe output from stegolsb is stored in outfile.zip.\n\n")
			f.close()	
	except:
		with open("Report.md","a") as f:
			f.write(output)
			f.close()

def pdf_parser(path):
	data = subprocess.Popen(["pdf-parser","-a",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM PDF-PARSER:\n\n")
		f.close()	
		
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()
		
def carving(path):
	data = subprocess.Popen(["foremost","-T",path,"-v"], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM FOREMOST:\n\n")
		f.close()	
		
	with open("Report.md","a+b") as f:
		for line in output.split(b"\n"):
			
			
			if re.search(r'FILES EXTRACTED',line.decode()):
				
				f.write(line+b"\n\n")
			elif re.search(r':=\s',line.decode()):
				f.write(line+b"\n\n")
		f.close()

def stegsnow(path):
	data = subprocess.Popen(["stegsnow",path,"stegsnow_answer.txt"], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	try:	
		
		with open("stegsnow_answer.txt","r") as f1:
			text = f1.read()
		with open("Report.md","a") as f:
			f.write("\n\nOUTPUT FROM STEGSNOW : \n\n")
			f.write(text)
			f.close()
	except:
		with open("Report.md","a") as f:
			f.write("no valid output from stegsnow")
			f.close()


	
	


