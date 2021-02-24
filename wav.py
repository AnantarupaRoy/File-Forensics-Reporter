import re
import subprocess

def solve(path):
	# strings
	data = subprocess.Popen(["strings",path], stdout=subprocess.PIPE)
	output=data.communicate()[0]
	with open("Report.md","a") as f:
		f.write("\n\nOUTPUT FROM STRINGS:\n\n")
		f.close()	
		
	with open("Report.md","a+b") as f:
		f.write(output)
		f.close()
	# audio-spectro
	
	subprocess.run(['sox', path , '-n','spectrogram'])
	
		
	with open("Report.md","a") as f:
		f.write("A spectrogram of the audio file has been created in spectrogram.png file.\n\n")
		f.close()
	
	# lsb
	data = subprocess.Popen(["stegolsb","wavsteg","-r","-i",path,"-o","output.txt","-b","10000"], stdout=subprocess.PIPE )
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
	
