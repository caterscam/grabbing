#mass filter wordpress only
#add path to lines
#code by banner and me only remakes

#!/usr/bin/env
import sys , requests , re
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init										
init(autoreset=True)

fr  =   Fore.RED																					
fg  =   Fore.GREEN	

print """  
  [#] Create By ::
	  ___                                                    ______        
	 / _ \                                                   |  ___|       
	/ /_\ \_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___ | |_ _____  __
	|  _  | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __||  _/ _ \ \/ /
	| | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \| || (_) >  < 
	\_| |_/_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/\_| \___/_/\_\ 
	                          __/ |
	                         |___/ Sript Filter
"""

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
	path =  str(sys.argv[0]).split('\\')
	exit('\n  [!] Enter <'+path[len(path)-1] + '> <sites.txt>')
	

def URL(url):
	if url[-1] == "/":
		pattern = re.compile('(.*)/')
		site = re.findall(pattern,url)
		url = site[0]
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url	
	
	
def filter(site):
	pet = re.compile('<meta name="generator" content="(.*)" />')
	try:
		site = URL(site)
		src = requests.get(site,timeout=15).content
		if re.findall(pet,src):
			generator = re.findall(pet,src)[0]
			if 'WordPress' in generator :
				print ' --| '+site +' --> {}[WordPress]'.format(fg)
				with open('wordpress.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'Joomla' in generator :
				print ' --| '+site +' --> {}[Joomla]'.format(fg)
			elif 'Drupal' in generator :
				print ' --| '+site +' --> {}[Drupal]'.format(fg)
			elif 'PrestaShop' in generator :
				print ' --| '+site +' --> {}[PrestaShop]'.format(fg)
			else :
				if 'wp-content/themes' in src :
					print ' --| '+site +' --> {}[WordPress]'.format(fg)
					with open('wordpress.txt', mode='a') as d:
						d.write(site+'/\n')
				elif 'catalog/view/theme'	in src :
					print ' --| '+site +' --> {}[OpenCart]'.format(fg)
				elif 'sites/all/themes' in src :
					print ' --| '+site +' --> {}[Drupal]'.format(fg)
				elif '<script type="text/javascript" src="/media/system/js/mootools.js"></script>' in src or '/media/system/js/' in src or 'com_content' in src :
					print ' --| '+site +' --> {}[Joomla]'.format(fg)
				elif 'js/jquery/plugins/' in src :
					print ' --| '+site +' --> {}[PrestaShop]'.format(fg)
				else :
					print ' --| '+site +' --> {}[Other]'.format(fr)
		else :
			if '/wp-content/' in src :
				print ' --| '+site +' --> {}[WordPress]'.format(fg)
				with open('wordpress.txt', mode='a') as d:
					d.write(site+'/\n')
			elif '/blog/wp-content/'	in src :
				print ' --| '+site +' --> {}[OpenCart]'.format(fg)
				with open('wordpress.txt', mode='a') as d:
					d.write(site+'/\n')
			elif '/site/wp-content/'	in src :
				print ' --| '+site +' --> {}[OpenCart]'.format(fg)
				with open('wordpress.txt', mode='a') as d:
					d.write(site+'/\n')
			elif '/wp/wp-content/'	in src :
				print ' --| '+site +' --> {}[OpenCart]'.format(fg)
				with open('wordpress.txt', mode='a') as d:
					d.write(site+'/\n')
			elif '/wordpress/wp-content/'	in src :
				print ' --| '+site +' --> {}[OpenCart]'.format(fg)
				with open('wordpress.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'sites/all/themes' in src :
				print ' --| '+site +' --> {}[Drupal]'.format(fg)
			elif '<script type="text/javascript" src="/media/system/js/mootools.js"></script>' in src or '/media/system/js/' in src or 'com_content' in src :
				print ' --| '+site +' --> {}[Joomla]'.format(fg)
			elif 'js/jquery/plugins/' in src :
				print ' --| '+site +' --> {}[PrestaShop]'.format(fg)
			elif 'osCommerce' in src :
				print ' --| '+site +' --> {}[osCommerce]'.format(fg)
			elif 'index.php?osCsid=' in src :
				print ' --| '+site +' --> {}[osCommerce]'.format(fg)
			elif 'index.php/cPath' in src :
				print ' --| '+site +' --> {}[osCommerce]'.format(fg)				
			else :
				print ' --| '+site +' --> {}[Other]'.format(fr)		
	except :
		print ' --| '+site +' --> {}[Time Out]'.format(fr)
mp = Pool(150)
mp.map(filter, target)
mp.close()
mp.join()		
