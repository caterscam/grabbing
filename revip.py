import requests
import cfscrape
import re
import os,sys,time
from multiprocessing.dummy import Pool
from bs4 import BeautifulSoup
from time import time as timer

headers = {
    'Host': 'domains.tntcode.com',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    
def checking(don):
    scraper = cfscrape.create_scraper()
    done = don.rstrip()
    
    try:
        
        ten = scraper.get("https://domains.tntcode.com/ip/"+don)
        time.sleep(4)
        tenx = ten.content
        
        
        regs = re.findall('<a style=\"text-decoration:none;\" href=\"(.*)\" rel=\"nofollow\" target=\"_blank\">', tenx)
        jum = len(regs)
        #print(jum)
        print("[!] "+str(done)+" IP | "+str(jum)+" Domain")
        for regs in regs:
            
            with open('resultweb.txt', 'a') as o:
                        o.writelines(regs + '\n')
        #
            #
    except:
        pass
            
def Main():
        try:
            print("\n\t | Reverse IP by SetraJowo | ")
            print("\n\t\t Gitlab : https://gitlab.com/setrajowo")
            ip = raw_input("\n\nInput List IP \t: ")
            thread = raw_input("Threads (Input 1) \t: ")
            print("\n\n")
            ips = open(ip, 'r').read().splitlines()
            pool = Pool(int(thread))
            results = pool.map(checking, ips)
        except:
            pass
        
if __name__ == '__main__':
    Main()