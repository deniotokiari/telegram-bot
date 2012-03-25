#coding: utf-8
import socket,ConfigParser,time,plugins.behavior,plugins.rehash,threading
class Bot():
	def __init__(self):
		config=ConfigParser.ConfigParser()
		config.read('config.ini')
		self.nick=config.get('Bot','Nick')
		self.ident=config.get('Bot','Ident')
		self.realname=config.get('Bot','Realname')
		self.password=config.get('Bot','Password')
		self.mode=config.get('Bot','Mode')
class Server(Bot):
	def __init__(self):
		Bot.__init__(self)
		config=ConfigParser.ConfigParser()
		config.read('config.ini')
		self.server=config.get('Connect','Server')
		self.port=config.get('Connect','Port')
		self.channel=config.get('Channel','Channels')
	def connect(self):
		sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((self.server,int(self.port)))
		sock.send('USER '+self.ident+' host servname : '+self.realname+'\r\n') 
		sock.send('NICK '+self.nick+'\r\n') 
		sock.send('MODE '+self.nick+' +'+self.mode+'\r\n')
		sock.send('PRIVMSG NickServ IDENTIFY '+self.password+'\r\n')
		time.sleep(3)
		sock.send('JOIN '+self.channel+'\r\n')
		sock.send('PRIVMSG Chanserv voice\r\n')
		self.sock=sock
		return sock
class Msg():
	def __init__(self,text):
		self.text=text
	def __msg(self):
		try:msg=self.text.split(':')[2].replace('\n','').replace('\r','')
		except:msg=''
		return msg
	def words(self,a=None):
		if a==None:
			try:msg=self.__msg().split(' ')
			except:msg=''
			return msg
		else:
			try:msg=self.__msg().split(' ')[a]
			except:msg=''
			return msg
	def join(self,num):
		try:msg=' '.join(self.words()[num:])
		except:msg=''
		return msg
	def __call__(self):return self.__msg()
class Text():
	def __init__(self,text):
		self.text=text
		self.msg=Msg(text)
	def sender(self):
		text=self.text
		try:sender=text.split(':')[1].split(' ')[0]
		except:sender=''
		return sender
	def typeMsg(self):
		try:type=self.text.split(':')[1].split(':')[0]
		except:type=''
		if type!='':
			if 'PRIVMSG' in type:
				if '#' in type:type='msg'
				else:type='privmsg'
			if 'NOTICE' in type:
				if '#' in type:type='notice'
				else:type='privnotice'
		return type
	def recipient(self):
		try:recipient=self.text.split(' ')[2]
		except:recipient=''
		return recipient
	def __call__(self):return self.text
class Sock():
	def __init__(self,sock,text,plug,nick):
		self.text=Text(text)
		self.sock=sock
		self.plugins=plug
		self.nick=nick
	def	msg(self,recipient,text):
		x=recipient
		if self.text.typeMsg() is 'privmsg':x=self.text.sender().split('!')[0]
		self.sock.send('PRIVMSG '+x+' '+text+'\r\n')
	def notice(self,recipient,text):
		x=recipient
		if self.text.typeMsg() is 'privmsg':x=self.text.sender().split('!')[0]
		self.sock.send('NOTICE '+x+' '+text+'\r\n')
	def __call__(self):return self.sock
exit=False
bot=Server()
plug=[[plugins.rehash.loadPlugins()[0]]]
while exit==False:
	try:sock=bot.connect()
	except:pass
	sock.settimeout(300.0)
	while 1:
		try:text=sock.recv(1024)
		except:break
		if not text:break
		if text.find('PING')!=-1:sock.send('PONG '+text.split()[1]+'\r\n')
		socks=Sock(sock,text,plug,bot.nick)
		texts=socks.text
		tread=threading.Thread(target=plugins.behavior.run,args=(texts,socks))
		tread.daemon=False
		tread.start()
		#if text.find('PING')==-1:print '[GET]',text
		if text.find('ERROR :Closing Link:')!=-1 and text.find('Ping timeout')==-1:exit=True
	if exit!=True:time.sleep(10)
