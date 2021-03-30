from kamene.all import *
import subprocess
import scapy

def solve(path):
	
	pcap = rdpcap(path)
	with open ("Report.md","a+") as f:
		f.write("UDP:\n\n")
		
		print(pcap)
		f.close()
	for p in pcap[UDP]:
		try:
			with open ("Report.md","a+b") as f:
				if "xml version" in  p[Raw].load.decode():
					continue
				else:
					f.write(p[Raw].load)
		
		except:
			continue

	with open ("Report.md","a+") as f:
		f.write("\n\nTCP:\n\n")
		f.close()
	for p in pcap[TCP]:
		try:
			with open ("Report.md","a+b") as f:
				f.write(p[Raw].load)
		
		except:
			continue
	
