#coding: utf-8
from time import sleep,strftime
import urllib2
def run(text,sock):
	if text().find('PING')!=-1:
		file=open('lib/toshokan','r')
		str=file.read()
		file.close()
		msg=[]
		try:url=urllib2.urlopen('http://tokyotosho.info/rss.php?filter=2,11')
		except:url=urllib2.urlopen('http://tokyotosho.info/rss.php?filter=2,11')
		page=url.read(4200)
		for i in range(6):
			item=page.split('<item>')[i+1].split('</item>')[0]
			category=item.split('<category>')[1].split('</category>')[0]
			title=item.split('<title>')[1].split('</title>')[0]
			torent=item.split('<link><![CDATA[')[1].split(']]></link>')[0]
			size=item.split('Size:')[1].split('<br')[0]
			try:comment=iteme.split('Comment')[1].split(']]')[0]
			except:comment=''
			last_msg=category+title+torent+size+comment
			if i==0:new_msg=category+title+torent+size+comment
			if last_msg==str:break
			msg.append(''+category+': 3'+title)
			msg.append('12Torrent:12 '+torent)
			msg.append('10Size:'+size+' | Comment10'+comment)
		if msg!=[]:
			file=open('lib/toshokan','w')
			file.write(new_msg)
			file.close()
			for i in msg:
				sock.msg('#wwips',i)
				sleep(1)