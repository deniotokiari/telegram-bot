#coding: utf-8
from owner import access
def run(text,sock):
	if text.msg.words(0)=='$c' and access(text.sender())==True:
		sock().send('PRIVMSG '+text.msg().split('$c')[1]+'\r\n')