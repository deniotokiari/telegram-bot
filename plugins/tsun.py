# -*- coding: cp1251 -*-
import random
help=['!tsun']
def run(text,sock):
	_BAKA_ = open('lib/tsundere_words','r').read().split(';')
	_BOT_NICK_ = 'Loli'
	if _BOT_NICK_ in text.msg():
		if text().find('кису')!=-1:sock.msg(text.recipient(), text.sender().split('!')[0]+', дамэ')
		else:sock.msg(text.recipient(), text.sender().split('!')[0]+', '+_BAKA_[random.randint(0,len(_BAKA_)-1)])
	if text.msg.words(0)=='!tsun':
		sock.msg(text.recipient(), text.sender().split('!')[0]+', '+_BAKA_[random.randint(0,len(_BAKA_)-1)])