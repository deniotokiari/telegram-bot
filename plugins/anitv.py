#coding: utf-8
import urllib2,re,time
help=['!anitv <title>']
def run(text,sock):
	if text.msg.words(0)=='!anitv':
		url=urllib2.urlopen('http://anitv.is-ingenio.us/')
		page=url.read()
		result=re.finditer(r'\<tr\>\<td\>.+\<\/td\>\<td\>.+\<\/td\>\<td\>\<.+\>.+\<\/div\>\<\/td\>\<td\>.+\<\/td\>\<td\>.+\<\/td\>\<td\>\<.+\<\/font\>\<\/td\>\<.+\<a href\=\'.+\<\/a\>\<\/td\>\<\/tr\>',page)
		i=0
		f=text.msg.words(1)
		try:g=f[0].upper()+f[1:]
		except:g=''
		h=f.upper()
		mess=[]
		for res in result:
			if i==5:break
			msg=res.group()
			title=msg.split('<tr><td>')[1].split('</td>')[0]
			if not f in title:
				if not g in title:
					if not h in title:continue
			i+=1
			ep=msg.split('</td><td>')[1].split('</td>')[0]
			channel=msg.split('<div')[1].split('</div>')[0].split('>')[1]
			try:anidb=msg.split('<a href=\'')[1].split('\'')[0]
			except:anidb=''
			eta=msg.split('<font color=\'#008000\'>')[1].split('<')[0]
			mess.append(title+' ep:'+ep+' '+channel+' '+anidb+' ETA:'+eta)
		if mess==[] and f=='':sock.msg(text.recipient(),'Nothing yet')
		if mess==[] and f!='':sock.notice(text.sender().split('!')[0],'Nothing yet')
		for i in mess:
			if f=='':
				sock.msg(text.recipient(),i)
				time.sleep(1)
			else:
				sock.notice(text.sender().split('!')[0],i)
				time.sleep(1)
	