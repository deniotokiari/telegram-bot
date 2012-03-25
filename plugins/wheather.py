import urllib2
help=['!w or !weather <town>']
def run(text,sock):
    if text.msg.words(0)=='!w' or text.msg.words(0)=='!weather':
        try:
            s = urllib2.urlopen("http://www.google.com/ig/api?weather="+text.msg.words(1)).read()
            sock.msg(text.recipient(), "In "+text.msg.words(1)+" now: "+ s.split('<condition data="')[1].split('"/>')[0]+", "+ s.split('<temp_c data="')[1].split('"/>')[0]+' celsius.')
        except: sock.msg(text.recipient(),"Congrats, something go wrong.")