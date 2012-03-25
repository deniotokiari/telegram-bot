from time import sleep,strftime
import urllib2,re,ConfigParser
help=['!rip']
def mal():
	file=open('lib/parser','r')
	str=file.read()
	file.close()
	url=urllib2.urlopen('http://myanimelist.net/')
	page=url.read(7400)
	msg=''
	result=re.search(r'\<p class\=\"spaceit\"\>\<a href\=\"http:\/\/.+\" style\=.+\>\<strong>.+\<\/strong\>\<\/a\>\<\/p\>',page)
	msg=result.group().split('<strong>')[1].split('</strong>')[0]
	msg+=' : '+result.group().split('<a href="')[1].split('"')[0]
	if str.split('mal{')[1].split('}')[0]!=msg:
		file=open('lib/parser','w')
		file.write(str.replace(str.split('mal{')[1].split('}')[0],msg))
		file.close()
		return msg
	else:return ''
def yousei():
	file=open('lib/parser','r')
	str=file.read(1200)
	file.close()
	url=urllib2.urlopen('http://yousei-raws.org/rss.xml')
	page=url.read()
	msg=''
	msg=page.split('<title>')[2].split('</title>')[0]
	msg+=' : '+page.split('<link>')[2].split('</link>')[0]
	if str.split('yousei{')[1].split('}')[0]!=msg:
		file=open('lib/parser','w')
		file.write(str.replace(str.split('yousei{')[1].split('}')[0],msg))
		file.close()
		return msg
	else:return ''
def ane():
	file=open('lib/parser','r')
	str=file.read()
	file.close()
	url=urllib2.urlopen('http://afternoonnapsempire.org/feed/')
	page=url.read(1200)
	msg=''
	msg=page.split('<title>')[2].split('</title>')[0]
	msg+=' : '+page.split('<link>')[2].split('</link>')[0]
	if str.split('ane{')[1].split('}')[0]!=msg:
		file=open('lib/parser','w')
		file.write(str.replace(str.split('ane{')[1].split('}')[0],msg))
		file.close()
		return msg
	else:return ''
def saiei():
	file=open('lib/parser','r')
	str=file.read()
	file.close()
	url=urllib2.urlopen('http://saiei.org/?feed=rss2')
	page=url.read(1200)
	msg=''
	msg=page.split('<title>')[2].split('</title>')[0]
	msg+=' : '+page.split('<link>')[2].split('</link>')[0]
	if str.split('saiei{')[1].split('}')[0]!=msg:
		file=open('lib/parser','w')
		file.write(str.replace(str.split('saiei{')[1].split('}')[0],msg))
		file.close()
		return msg
	else:return ''
def sankaku():
	file=open('lib/parser','r')
	str=file.read()
	file.close()
	url=urllib2.urlopen('http://www.sankakucomplex.com/feed/')
	page=url.read(1200)
	msg=''
	msg=page.split('<title>')[2].split('</title>')[0]
	msg+=' : '+page.split('<link>')[2].split('</link>')[0]
	msg=msg.replace('&#8220;','"').replace('&#8221;','"')
	if str.split('sankaku{')[1].split('}')[0]!=msg:
		file=open('lib/parser','w')
		file.write(str.replace(str.split('sankaku{')[1].split('}')[0],msg))
		file.close()
		return msg
	else:return ''
def run(text,sock):
	if text.msg.words(0)=='!rip':
			file=open('lib/parser','r')
			str=file.read()
			file.close()
			msg=[]
			msg.append(str.split('yousei{')[1].split('}')[0])
			msg.append(str.split('ane{')[1].split('}')[0])
			msg.append(str.split('saiei{')[1].split('}')[0])
			for i in msg:
				sock.notice(text.sender().split('!')[0],i)
				sleep(0.9)
	min=strftime('%M')
	if (min=='10' or min=='11') and text().find('PING')!=-1:
		msg=mal()
		config=ConfigParser.ConfigParser()
		config.read('config.ini')
		chan=config.get('Channel','Channels').split(',')
		if msg!='':
			for i in chan:sock.msg(i,msg)
	if (min=='20' or min=='21') and text().find('PING')!=-1:
		msg=yousei()
		config=ConfigParser.ConfigParser()
		config.read('config.ini')
		chan=config.get('Channel','Channels').split(',')
		if msg!='':
			for i in chan:sock.msg(i,msg)
	if (min=='30' or min=='31') and text().find('PING')!=-1:
		msg=ane()
		config=ConfigParser.ConfigParser()
		config.read('config.ini')
		chan=config.get('Channel','Channels').split(',')
		if msg!='':
			for i in chan:sock.msg(i,msg)
	if (min=='40' or min=='41') and text().find('PING')!=-1:
		msg=saiei()
		config=ConfigParser.ConfigParser()
		config.read('config.ini')
		chan=config.get('Channel','Channels').split(',')
		if msg!='':
			for i in chan:sock.msg(i,msg)
	if (min=='50' or min=='51') and text().find('PING')!=-1:
		msg=sankaku()
		config=ConfigParser.ConfigParser()
		config.read('config.ini')
		chan=config.get('Channel','Channels').split(',')
		if msg!='':
			for i in chan:sock.msg(i,msg)