#coding: utf-8
def access(user):
		file=open('lib/owner','r')
		str=file.read()
		file.close()
		host=user.split('@')[1]
		if host in str:return True
		else:return False
def run(text,sock):pass