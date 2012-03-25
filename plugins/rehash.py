#coding: utf-8
import os,imp,time
from owner import access
help=['$rehash']
def loadPlugins():
	plugins,msg=[],0
	plugin_dir='plugins'
	error = ''
	for fname in os.listdir(plugin_dir):
		if fname.endswith('.py'):
			plugin_name=fname[:-3]
			if plugin_name!='__init__':
				try:
					package_obj=__import__(plugin_dir+'.'+plugin_name)
					msg+=1
				except:
					error += '[%s]'%(plugin_name)
					continue
				plugin_obj=getattr(package_obj,plugin_name)
				if plugin_name!='behavior' and plugin_name!='antiflood':plugins.append(plugin_obj)
				imp.reload(plugin_obj)
	msg = str(msg)
	if error != '': msg += ' |Error: ' + error
	return plugins,'Loaded plugins: '+ msg
def run(text,sock):
	if text.msg.words(0)=='$rehash' and access(text.sender())==True:
		sock.plugins[0][0],msg=loadPlugins()
		sock.msg(text.recipient(),msg)
