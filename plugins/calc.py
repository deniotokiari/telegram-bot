# -*- coding: cp1251 -*-
import urllib2

def skobki(str):
    try:
        return str.split("(")[1].split(")")[0]
    except: return "no"

def multiply(str):
    try:
        if "*" in str:
            i = str.split("*")
            num1,num2 = "",""
            s1,s2 = i[0],i[1]
            col1=-1
            for l in i[0]:
                if(s1[col1:].isdigit()):
                    num1 = s1[col1]+num1
                else: break
                col1-=1
            col2=0
            for l in i[1]:
                if(s2[col2].isdigit()):
                    num2 += s2[col2]
                else: break
                col2+=1
            return int(num1),int(num2)
    except: return "no","no"

def plus(str):
    try:
        if "+" in str:
            i = str.split("+")
            num1,num2 = "",""
            s1,s2 = i[0],i[1]
            col1=-1
            for l in i[0]:
                if(s1[col1].isdigit()):
                    num1 = s1[col1]+num1
                else: break
                col1-=1
            col2=0
            for l in i[1]:
                if(s2[col2].isdigit()):
                    num2 += s2[col2]
                else: break
                col2+=1
            return int(num1),int(num2)
    except: return "no","no"

def minus(str):
    try:
        if "-" in str:
            i = str.split("-")
            num1,num2 = "",""
            s1,s2 = i[0],i[1]
            col1=-1
            for l in i[0]:
                if(s1[col1:].isdigit()):
                    num1 = s1[col1]+num1
                else: break
                col1-=1
            col2=0
            for l in i[1]:
                if(s2[col2].isdigit()):
                    num2 += s2[col2]
                else: break
                col2+=1
            return int(num1),int(num2)
        else:
            return "-","-"
    except: return "no","no"

def div(str):
    try:
        if "/" in str:
            i = str.split("/")
            num1,num2 = "",""
            s1,s2 = i[0],i[1]
            col1=-1
            for l in i[0]:
                if(s1[col1:].isdigit()):
                    num1 = s1[col1]+num1
                else: break
                col1-=1
            col2=0
            for l in i[1]:
                if(s2[col2].isdigit()):
                    num2 += s2[col2]
                else: break
                col2+=1
            return int(num1),int(num2)
        else:
            return "/","/"
    except: return "no","no"

help=['!calc']
def run(text,sock):
    if text.msg.words(1)=='-by':
        s = urllib2.urlopen("http://www.nbrb.by/").read().split("США<td align=right>")[1].split("<td align=right>")[0].replace(' ','').replace('.00','')
        if 'course' in text.msg():
            sock.msg(text.recipient(), s)
        else: sock.msg(text.recipient(), str(float(text.msg.words(2).split('+')[0])*float(s)))
    if text.msg.words(0)=='!calc':
        if text.msg.words(1)!='-by':
            string = text.msg.words(1)
            for i in range(len(string.split("("))-1):
                if(skobki(string)!="no"):
                    s = skobki(string)
                    tempS = s
                    for i in range(len(s.split("*"))-1):
                        n1, n2 = multiply(s)
                        if(n1!="no"): s=s.replace(str(n1)+"*"+str(n2),str(n1*n2))
                    for i in range(len(s.split("/"))-1):
                        n1, n2 = div(s)
                        if(n1!="no"): s=s.replace(str(n1)+"/"+str(n2),str(n1/n2))
                    for i in range(len(s.split("+"))-1):
                        n1, n2 = plus(s)
                        if(n1!="no"): s=s.replace(str(n1)+"+"+str(n2),str(n1+n2))
                    for i in range(len(s.split("-"))-1):
                        n1, n2 = minus(s)
                        if(n1!="no"): s=s.replace(str(n1)+"-"+str(n2),str(n1-n2))
                    string = string.replace('('+tempS+')',s)
            for i in range(len(string.split("*"))-1):
                n1, n2 = multiply(string)
                if(n1!="no"): string=string.replace(str(n1)+"*"+str(n2),str(n1*n2))
            for i in range(len(string.split("/"))-1):
                n1, n2 = div(string)
                if(n1!="no"): string=string.replace(str(n1)+"/"+str(n2),str(n1/n2))
            for i in range(len(string.split("+"))-1):
                n1, n2 = plus(string)
                if(n1!="no"): string=string.replace(str(n1)+"+"+str(n2),str(n1+n2))
            for i in range(len(string.split("-"))-1):
                n1, n2 = minus(string)
                if(n1!="no"): string=s.replace(str(n1)+"-"+str(n2),str(n1-n2))
            sock.msg(text.recipient(), string)