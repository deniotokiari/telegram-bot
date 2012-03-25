import urllib2,ConfigParser
from time import strftime,sleep
help=['!new']
def setDate():
	file=open('lib/anidb','r')
	str=file.read()
	file.close()
	if str=='':
		file=open('lib/anidb','w')
		file.write(strftime('%x').split('/')[1]+'.'+strftime('%x').split('/')[0]+' False')
		file.close()
	else:
		if str.split(' ')[0]!=strftime('%x').split('/')[1]+'.'+strftime('%x').split('/')[0]:
			file=open('lib/anidb','w')
			file.write(strftime('%x').split('/')[1]+'.'+strftime('%x').split('/')[0]+' False')
			file.close() 
setDate()
def newAniDB():
	time=strftime('%m %d')
	mon,day=time.split(' ')[0],time.split(' ')[1]
	url=urllib2.urlopen('http://imggrabberredirect.appspot.com/anidb.net/perl-bin/animedb.pl?show=main')
	page=url.read(17000)
	started=page.split('<h4><span>Just Started</span></h4>')[1].split('</ol>')[0].replace('<ol>','')
	finished=page.split('<h4><span>Just Finished</span></h4>')[1].split('</ol>')[0].replace('<ol>','')
	mess,j=['Started:'],0
	for i in started.split('\n'):
		if i.replace('\t','').replace('\n','')=='':continue
		if i.split('<span>')[1].split('</span>')[0]!=day+'.'+mon:break
		mess.append(i.split('<span>')[1].split('</span>')[0]+': '+i.split('</a>')[0].split('>')[-1]+' http://anidb.net/a'+i.split('<a href="')[1].split('">')[0].split('=')[2])
		j+=1
	if j==0:mess=[]
	mess.append('Finished:')
	j=0
	for i in finished.split('\n'):
		if i.replace('\t','').replace('\n','')=='':continue
		if i.split('<span>')[1].split('</span>')[0]!=day+'.'+mon:break
		mess.append(i.split('<span>')[1].split('</span>')[0]+': '+i.split('</a>')[0].split('>')[-1]+' http://anidb.net/a'+i.split('<a href="')[1].split('">')[0].split('=')[2])
		j+=1
	if j==0:mess.remove('Finished:')	
	return mess
def run(text,sock):
	if text.msg.words(0)=='!new':
		msg=newAniDB()	
		if msg==[]:sock.notice(text.sender().split('!')[0],'No news yet...')
		else:
			for i in msg:
				sock.notice(text.sender().split('!')[0],i)
				sleep(1)
	h,min=strftime('%H %M').split(' ')[0],strftime('%H %M').split(' ')[1]
	if (min=='00' or min=='01') and text().find('PING')!=-1:
		if h=='00' or h=='18':setDate()
		file=open('lib/anidb','r')
		str=file.read()
		file.close()
		mon,day,flag=str.split(' ')[0].split('.')[1],str.split(' ')[0].split('.')[0],str.split(' ')[1]
		if flag=='False' or mon!=strftime('%m %d').split(' ')[0] or day!=strftime('%m %d').split(' ')[1]:
			msg=newAniDB()
			if msg!=[]:
				file=open('lib/anidb','w')
				file.write(str.replace('False','True'))
				file.close()
				config=ConfigParser.ConfigParser()
				config.read('config.ini')
				chan=config.get('Channel','Channels').split(',')
				for i in chan:
					for j in msg:
						sock.msg(i,j)
						sleep(1)		