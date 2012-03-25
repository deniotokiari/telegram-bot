import threading,time
file=open('lib/antiflood','w')
file.write('')
file.close()
file=open('lib/help','r')
help=file.read().replace('\n','')
file.close()
def delUser(user):
	time.sleep(5)
	file=open('lib/antiflood','r')
	flooders=file.read()
	file.close()
	file=open('lib/antiflood','w')
	file.write(flooders.replace(user,''))
	file.close()

def run(text,sock):
	if text.msg.words(0) in help:
		file=open('lib/antiflood','r')
		flooders=file.read()
		file.close()
		if text.sender() in flooders:
			sock.notice(text.sender().split('!')[0],'Flood!')
			return True
		else:
			file=open('lib/antiflood','r')
			str=file.read()
			file.close()
			file=open('lib/antiflood','w')
			file.write(str+text.sender())
			file.close()
			user=text.sender()
			tread=threading.Thread(target=delUser,args=(user,))
			tread.daemon=False
			tread.start()
			return False	
	else:return False	