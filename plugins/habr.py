#coding: utf-8
from time import sleep,strftime
import urllib2,ConfigParser
def run(text,sock):
	pass
	"""if text().find('PING')!=-1:
		file=open('lib/habr','r')
		str=file.read()
		file.close()
		msg=''
		try:url=urllib2.urlopen('http://imggrabberredirect.appspot.com/habrahabr.ru/rss/')
		except:url=urllib2.urlopen('http://imggrabberredirect.appspot.com/habrahabr.ru/rss/')
		page=url.read(1500).replace('\n','')
		try:title=page.split('<![CDATA[')[2].split(']')[0].
		except:title='Error'
		url=page.split('<link>')[3].split('<')[0]
		msg=title+': '+url
		if str!=msg:
			file=open('lib/habr','w')
			file.write(msg)
			file.close()
			sock.notice('dl4',msg)
			sleep(1)"""