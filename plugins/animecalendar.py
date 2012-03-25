from time import strftime,sleep
import urllib2,re
help=['!today']
def run(text,sock):
	if text.msg.words(0)=='!today':
		time=strftime('%Y %m %d')
		year,mon,day=time.split(' ')[0],time.split(' ')[1],time.split(' ')[2]
		url=urllib2.urlopen('http://animecalendar.net/'+year+'/'+mon+'/'+day)
		page=url.read().replace('\n','').replace('\t','')
		result=re.finditer(r'\<a href\=\"\/show\/.+\<\/a\>\<\/h3\>\<small\>.+\<\/small\>\<br \/\>\<br\ \/\>\<em\>.+\<\/em\>\<\/div\>\<\/td\>\<\/tr\>\<\/table\>\<\/td\>\<\/tr\>\<tr\>\<td valign\=\".+\<\/td\>',page)
		for res in result:msg=res.group()
		title=[]
		for i in msg.split('</a>'):title.append(i.split('>')[-1])
		time=[]
		for i in msg.split('<small>'):time.append(i.split('</small>')[0])
		title.remove(title[-1])
		time.remove(time[0])
		j=0
		msg=[]
		for i in title:
			msg.append(i+' - '+time[j])
			j+=1
		for i in msg:
			sock.notice(text.sender().split('!')[0],i)
			sleep(1)