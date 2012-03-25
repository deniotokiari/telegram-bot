#coding: utf-8
from owner import access
import ConfigParser,threading,time
help=['$die,$join,$part,$stat,$nick']
def infoSet(command,chan):
	config=ConfigParser.ConfigParser()
	config.read('config.ini')
	channel=config.get('Channel','Channels')
	file=open('config.ini','r')
	str=file.read()
	file.close()
	file=open('config.ini','w')
	if '$join' in command:
		msg=channel+','+chan
		file.write(str.replace(channel,msg))
	else:
		print 'ds'
		str=str.replace(chan,'').replace(',,',',')
		if str[-1]==',':str=str[:-1]
		file.write(str)
	file.close()
def run(text,sock):
	if text.msg.words(0)=='$die' and access(text.sender())==True:sock().send('QUIT :exit\r\n')
	if '$join' in text.msg.words(0) and access(text.sender())==True:
		sock().send('JOIN '+text.msg.words(1)+'\r\n')
		command=text.msg.words(0)
		channel=text.msg.words(1)
		infoSet(command,channel)
	if '$part' in text.msg.words(0) and access(text.sender())==True:
		sock().send('PART '+text.recipient()+'\r\n')
		command=text.msg.words(0)
		chan=text.recipient()
		infoSet(command,chan)
	if '$stat' in text.msg.words(0) and access(text.sender())==True:
		msg,j=threading.enumerate(),0
		time.sleep(1)
		for i in msg:
			i=str(i)
			sock.msg(text.recipient(),' :'+str(j)+': '+(i.split('(')[1].split(')')[0]))
			j+=1
			time.sleep(1)
