#!/usr/bin/python
# -*- coding: utf-8 -*-
# author : t.me/sxcertox
import os
import re
import socket
import requests
import concurrent.futures

os.system("clear")

class Rev:
	def __init__(self):
		self.loop = 0
		self.reversed = 0
		self.duplicate = []
	def api(self, target):
		#try:
			self.loop += 1
			if len(target.split(".")) == 4:
				ip = target
			else:
				regex = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', target)[0]
				ip = socket.gethostbyname(regex)
			if ip not in self.duplicate:
				self.duplicate.append(ip)
				api = requests.get(f"http://www.ipneighbor.com/neighbors.php?q={str(ip)}&state=fromSecondPage&db=16", headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36"}, stream=True, timeout=15).text
				regex = re.findall("<TD>(.*?)</TD>\n", api)
				for results in regex:
					if "." in results:
						self.reversed += 1
						open("grab.txt","a+").write(f"{results.lower()}\n")
		#except:pass
			print (f"\r[ grab ] {self.loop}/{len(self.file)}  {self.reversed} sites", end="")
	def main(self):
		print ("""\033[37;1m
  ___       ____    
 / _ \___  |_  /_ __
/ // / _ \_/_ <\ \ /
\___/ .__/____/_\_\ 
   /_/ private reverse IP unlimated
   \033[97m\033[101m\033[97m[ buy here t.me/takanabee ]\033[0m
		""")
		self.file = open(input("\033[37;1m[*] list : "), errors="ignore").read().splitlines()
		thread = int(input("[*] speed : "))
		with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as th:
			for target in self.file:
				th.submit(self.api, target)
if __name__=="__main__":
	Rev().main()
