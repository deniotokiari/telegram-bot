import urllib2,random
help=['!img <tag>']
def run(text,sock):
	if text.msg.words(0)=='!img':
		tag=text.msg.words(1).replace('!','%21').replace('&','%26').replace(';','%3B')
		link=['http://oreno.imouto.org/','http://konachan.com/']
		link=random.choice(link)
		url=urllib2.urlopen(link+'post/index.xml?tags='+tag+'&limit=1&page=1')
		parse,num=url.read(),0
		num=parse.split('<posts count="')[1].split('"')[0]
		if num!='0':
			num=random.randint(1,int(num))
			url=urllib2.urlopen(str(link+'post/index.xml?limit=1&tags='+tag+'&page='+str(num)))
			parse=url.read()
			try:size=parse.split(' width="')[1].split('"')[0]+'x'+parse.split(' height="')[1].split('"')[0]
			except:size=''
			sock.msg(text.recipient(),' :'+size+': '+str(parse.split('file_url="')[1].split('"')[0]))
		else:sock.msg(text.recipient(),'This image is illuminated...')

	