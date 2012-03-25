#coding: utf-8
import rehash,antiflood
def run(text,sock):
	try:flood=antiflood.run(text,sock)
	except:flood=False
	if flood==False:
		for i in sock.plugins[0][0]:i.run(text,sock)