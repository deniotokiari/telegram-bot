#coding: utf-8
import os
from owner import access
def run(text,sock):
	if '!help' in text.msg.words(0):
		file=open('lib/help','r')
		j=0
		for i in file.readlines():
			if j!=1:
				if access(text.sender())!=True:
					j+=1
					continue
			sock.notice(text.sender().split('!')[0],i)
		file.close()
msg=[['Owner: '],['User: ']]
for fname in os.listdir('plugins'):
		if fname.endswith('.py'):
			module_name=fname
			if module_name!='__init__.py' and module_name!='help.py':
				file=open('plugins/'+module_name,'r')
				str=file.read()
				file.close()
				if str.find('help=[\'')!=-1:
					str=str.split('help=[')[1].split('\']')[0].replace('\',\'','|').replace('\'','')
					if str.find('$')!=-1:msg[0].append(str)
					else:msg[1].append(str)
str=''
for q in msg:
	j=0
	for i in q:
		j+=1
		if j<3:
			str+=i
			continue
		str+='|'+i
	str+='\n'
file=open('lib/help','w')
file.write(str.replace(',','|'))
file.close()			