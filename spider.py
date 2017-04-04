import re
import time
import requests
from bs4 import BeautifulSoup,NavigableString
import urllib.request

p = re.compile('applism&amp;t=[0-9]+')
p5 =re.compile('keyword')
p6 = "http://cache.2ch-ranking.net/cache.php?thread=potato.2ch.net/applism/"
p7 = re.compile('/&[amp;]*res=100')
p8 =re.compile('art[0-9]+')
p9 ="art"
p10 =re.compile('#[0-9]+')
i =0
tiss =[]
tus =[]


def gett():
    v =0
    tiss =[]
    tus =[]
    bans =[]
    yy =0
    yyy =0
    response2 = urllib.request.urlopen("http://potato.2ch.net/applism/")
    data = response2.read()
    soup = BeautifulSoup(data, "lxml")
    titles = soup.find_all("a")
    while v < len(titles):
        title =titles[v]
        proti = title.get("href")
        if isinstance(proti,type(None)):
            v+=1
            continue
        han = re.search(p10,proti)
        if isinstance(han,type(None)):
            v+=1
            continue      
        ti = title.string
        if isinstance(ti,type(None)):
            v+=1
            continue
        popo = re.search(p5,ti)
        if isinstance(popo,type(None)):
            v+=1
            continue
        else:
            ti = re.search(p8,ti)
            if isinstance(ti,type(None)):
                continue
            ti = ti.group()
            ti = ti.lstrip(p9)
            ti = int(ti)
            tiss.append(ti)
            bans.append(v)
            v+=1
    while yy  < len(tiss):
        if yy==0:
            maxx = tiss[0]
            yy +=1
            yyy =0
            continue
        elif tiss[yy] >= maxx:
            maxx = tiss[yy]
            yyy =yy
            yy+=1
            continue
        else:
            yy += 1
            continue
    sharp = bans[yyy] -1
    honmaru = titles[sharp]
    honmaru =honmaru.get("href")
    super = honmaru.lstrip("../test/read.cgi/applism/")
    super = super.rstrip("/l50")
    return super

def gettt():
    yy =0
    yyy =0
    response2 = urllib.request.urlopen("http://2ch-ranking.net/index.html?board=applism")
    data = response2.read()
    soup = BeautifulSoup(data, "lxml")
    titles = soup.find_all("a")
    for title in titles:
        ti = title.string
        if isinstance(ti,type(None)):
            continue
        popo = re.search(p5,ti)
        if isinstance(popo,type(None)):
            continue
        else:
            ti = re.search(p8,ti)
            if isinstance(ti,type(None)):
                continue
            ti = ti.group()
            ti = ti.lstrip(p9)
            ti = int(ti)
            tiss.append(ti)
            tus.append(title)
    while yy  < len(tiss):
        if yy==0:
            maxx = tiss[0]
            yy +=1
            yyy =0
            continue
        elif tiss[yy] >= maxx:
            maxx = tiss[yy]
            yyy =yy
            yy+=1
            continue
        else:
            yy += 1
            continue
    title = tus[yyy]
    ii = title.get("href")
    ii = ii.lstrip(p6)
    ii = re.sub(p7,"",ii)
    return ii

lists=[]
y=0
o  =1
while i < 1000:
    y=0
    u = 0
    numm =gettt()
    hantei = numm in lists
    if hantei:
        time.sleep(300)
        continue
    lists.append(numm)
    while y < 60:
        u =0
        urll = "http://potato.2ch.net/test/read.cgi/applism/" + numm
        datae = requests.get(urll)
        datae = datae.text
        u = datae.count('data-id')
        if u >999:
            with open(numm + ".html", "w")as fo:
                fo.write(datae)
            o +=1
            break
        elif y==59:
            with open(numm + ".html", "w")as fo:
                fo.write(datae)
                break
        else:
            y +=1
            time.sleep(300)
            continue
        time.sleep(300)
