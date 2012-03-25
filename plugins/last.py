# -*- coding: cp1251 -*-
import urllib2
from time import sleep
from extra import extra
from operator import itemgetter
help=['!last help']

def dcm(n):
    suni = n.decode('utf8')
    scp1251 = suni.encode('cp1251')
    return scp1251
def dum(n):
    suni = n.decode('cp1251')
    scp1251 = suni.encode('utf8')
    return scp1251
def lastSong(nick,sock,where_send):
    try :
        s = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user="+nick+"&api_key=23caa86333d2cb2055fa82129802780a").read().split("</track>")[0]
        artist = s.split("<artist")[1].split("</artist>")[0].split(">")[1]
        track = s.split("<name>")[1].split("</name>")[0]
        is_album = 0
        if "</album>" in s:
            album = s.split("<album")[1].split("</album>")[0].split(">")[1]
            is_album = 1
        url = s.split("<url>")[1].split("</url>")[0]
        if is_album: sock.msg(where_send, extra.b+dcm(artist)+extra.b_close+' - ['+dcm(album)+'] - '+extra.b+dcm(track)+extra.b_close+' < '+url+' >')
        else: sock.msg(where_send, extra.b+dcm(artist)+' - '+dcm(track)+extra.b_close+' < '+url+' >')
    except : sock.msg(where_send, 'Something go wrong...')

def nowPlaying(nick,sock,where_send):
    try:
        s = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user="+nick+"&api_key=23caa86333d2cb2055fa82129802780a").read()
        if '<track nowplaying="true">' in s:
            s = s.split("</track>")[0]
            artist = s.split("<artist")[1].split("</artist>")[0].split(">")[1]
            track = s.split("<name>")[1].split("</name>")[0]
            is_album = 0
            if "</album>" in s:
                album = s.split("<album")[1].split("</album>")[0].split(">")[1]
                is_album = 1
            url = s.split("<url>")[1].split("</url>")[0]
            if is_album: sock.msg(where_send, extra.b+dcm(artist)+extra.b_close+' - '+extra.color_red+'['+dcm(album)+']'+extra.color_black+' - '+extra.b+dcm(track)+extra.b_close+' < '+url+' >')
            else: sock.msg(where_send, extra.b+dcm(artist)+' - '+dcm(track)+extra.b_close+' < '+url+' >')
        else: sock.msg(where_send, 'Nothing is playing now.')
    except: sock.msg(where_send, 'Something go wrong...')

def sortAll(nicks,counts):
    dict = {}
    for i in range(len(nicks)):
        dict[nicks[i]] =  int(counts[i])
    list = sorted(dict.items(), key=itemgetter(1),reverse=True)
    return list

def compare(nick,sock,where_send,flag):
    try:
        nicks = nick.split("+")
        counts = []
        nicks_arr = []
        for n in nicks:
            if "-p" in flag:
                s = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user="+n+"&api_key=23caa86333d2cb2055fa82129802780a").read()
                counts.insert(len(counts),s.split("<playcount>")[1].split("</playcount>")[0])
                nicks_arr.insert(len(counts),s.split("<name>")[1].split("</name>")[0])
                st = 'playcount'
            else:
                s = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=library.getartists&api_key=b25b959554ed76058ac220b7b2e0a026&user="+n).read(400)
                st = 'artistcount'
                counts.insert(len(counts),s.split("total=\"")[1].split("\">")[0])
                
                nicks_arr.insert(len(counts),s.split("user=\"")[1].split("\"")[0])
        list = sortAll(nicks_arr,counts)
        for c in range(len(counts)):
            sock.msg(where_send, str(c+1)+ ". "+str(list[c]).split("'")[1].split("'")[0]+' '+st+' = '+str(list[c]).split(" ")[1][:-1])
            sleep(1)
    except: sock.msg(where_send, 'Something go wrong...')

def run(text,sock):
    if text.msg.words(0)=='!last' or text.msg.words(0)=='!l':
        if text.msg.words(1)=="help":
            sock.notice(text.sender().split('!')[0], 'Commands: !last count <nick>|!last cmp -p|-a <nick1>+<nick2>+...+<nickN>|!last np or nowplaying <nick>|!last ls or lastsong <nick>')
        if text.msg.words(1)=="count":
            try:
                if text.msg.words(2)=="-a":
                    artist = text.msg().split("-a "+text.msg.words(3)+" ")[1].replace(' ','+')
                    s = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=user.getartisttracks&user="+text.msg.words(3)+"&artist="+artist+"&api_key=23caa86333d2cb2055fa82129802780a").read(200)
                    sock.msg(text.recipient(), s.split('user="')[1].split('" artist')[0]+": "+s.split('artist="')[1].split('" items')[0]+" playcount = "+s.split('items="')[1].split('" page')[0])
                else:
                    s = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user="+text.msg.words(2)+"&api_key=23caa86333d2cb2055fa82129802780a").read()
                    sock.msg(text.recipient(), s.split("<name>")[1].split("</name>")[0]+' playcount = '+s.split("<playcount>")[1].split("</playcount>")[0])
            except: sock.msg(text.recipient(), text.msg.words(2)+' : nick does not exist.')
        if text.msg.words(1)=="cmp":
            compare(text.msg.words(3), sock,text.recipient(),text.msg.words(2))
        if text.msg.words(1)=="lastsong" or text.msg.words(1)=="ls":
            lastSong(text.msg.words(2), sock, text.recipient())
        if text.msg.words(1)=="nowplaying" or text.msg.words(1)=="np":
            nowPlaying(text.msg.words(2), sock, text.recipient())
        if text.msg.words(1)=="similar":
            artist = text.msg().split("similar ")[1].replace(' ','+')
            s = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist="+dum(artist)+"&limit=5&api_key=23caa86333d2cb2055fa82129802780a").read()
            for i in range(5):    
                sock.msg(text.recipient(), dcm(s.split("<name>")[1].split("</name>")[0])+' - '+s.split("<url>")[1].split("</url>")[0])
                s = s[s.find("</artist>")+9:]
                sleep(1)
    if text.msg.words(0)=='!np': nowPlaying(text.msg.words(1), sock, text.recipient())