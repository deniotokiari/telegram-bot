# -*- coding: cp1251 -*-
import urllib2
from time import sleep
help=['!bash']
def run(text,sock):
	if text.msg.words(0)=="!bash":
			if not text.msg.words(1):
				try:
					response = urllib2.urlopen("http://bash.org.ru/forweb").read()
					bash = response.split("<' + '/span><' + 'br>")[1].split("<' + 'br><' + 'br><' + 'small>")[0]
					s = bash.split("<' + 'br>")
					for b in s:
						sock.msg(text.recipient(), b)
						sleep(1)
				except: sock.msg(text.recipient(),'Something go wrong.')
			else:
				try:
					response = urllib2.urlopen("http://bash.org.ru/quote/"+text.msg.words(1)).read()
					bash = response.split("		<div>")[1].split("</div>")[0].replace('&quot;','"').replace('&lt;','<').replace('&gt;','>')
					s = bash.split("<br>")
					for b in s:
						sock.msg(text.recipient(), b)
						sleep(1)
				except: sock.msg(text.recipient(),'Something go wrong.')