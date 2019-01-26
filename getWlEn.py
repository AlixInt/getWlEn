#!/usr/bin/env python3
# Coded by Eng:gr13r (E-8661
# Open source 
# ModuleNotFoundError
from bs4 import BeautifulSoup
import urllib.request
banner = '''
Link GitHub : https://github.com/AlixInt/getWlEn.git
[+] getWlEn.
[*] coded by Eng:gr13r (E-8661

            _     _    _ _   _____        
           | |   | |  | | | |  ___|       
  __ _  ___| |_  | |  | | | | |__ _ __    
 / _` |/ _ \ __| | |/\| | | |  __| '_ \   
| (_| |  __/ |_  \  /\  / | | |__| | | |
 \__, |\___|\__|  \/  \/|_| \____/_| |_|
  __/ |                                   
 |___/                                    


[*]- Started ...
'''
urls = ['http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_A-B/?page=1','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_A-B/?page=2','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_A-B/?page=3','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_A-B/?page=4','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_A-B/?page=5','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_C-D/?page=1','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_C-D/?page=2','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_C-D/?page=3','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_C-D/?page=4','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_C-D/?page=5','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_C-D/?page=6','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_C-D/?page=7','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_E-G/?page=1','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_E-G/?page=2','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_E-G/?page=3','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_E-G/?page=4','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_E-G/?page=5','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_E-G/?page=6','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_H-K/?page=1','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_H-K/?page=2','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_H-K/?page=3','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_H-K/?page=4','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_L-N/?page=1','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_L-N/?page=2','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_L-N/?page=3','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_L-N/?page=4','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_O-P/?page=1','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_O-P/?page=2','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_O-P/?page=3','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_O-P/?page=4','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_O-P/?page=5','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_Q-R/?page=1','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_Q-R/?page=2','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_Q-R/?page=3','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_S/?page=1','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_S/?page=2','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_S/?page=3','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_S/?page=4','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_S/?page=5','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_T/?page=1','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_T/?page=2','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_T/?page=3','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_U-Z/?page=1','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_U-Z/?page=2','http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_U-Z/?page=3']
print("{0}[*] loading...".format(banner))
for url in urls:
	opurl = urllib.request.urlopen(url)
	rurl = opurl.read()
	soup = BeautifulSoup(rurl,'html.parser')
	u =  soup.findAll("ul",{"class":"result-list1 wordlist-oxford3000 list-plain"})
	for i in soup.findAll("ul",{"class":"result-list1 wordlist-oxford3000 list-plain"}):
		i = i.findAll("a")
		for ii in i:
			ii = ii.text
			filewe = open('wordlist-English.txt','a')
			line = "{0}\n".format(ii)
			filewe.write(line)
			filewe.close()
print("[+] Completed .")
	
