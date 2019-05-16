import requests
from importlib import reload
from bs4 import BeautifulSoup
import threading
import jieba

ur=[]
content=[]
title=[]
str1=""
endindex=24850
tt=24900
def fetch(url):
    requ=requests.get(url,cookies={'over18':'1'})
    return requ


def TITLE(page):
    url = 'https://www.ptt.cc/bbs/Gossiping/index'+str(page)+'.html'
    resp=fetch(url)
    html=resp.text
    soup=BeautifulSoup(html,"html.parser")
    Soup=soup.find_all('div',class_="title")
    if Soup==[]:
        return False
    for pr in Soup:
        if pr.find('a')==None:
            continue
        str2=pr.find('a').text
        title.append(str2)
    return True

File=open('Gossip-Content.txt','ab')

def GetContent(url):
    global str1
    r=fetch(url)
    html=r.text;
    html.encode('utf-8')
    s=BeautifulSoup(html,"html.parser")

    #抓推文內容
    for t1,t2 in zip(s.find_all('span',class_='f3 push-content'),s.find_all('span',class_='push-tag')):
        tmpt2=str(t2)
        #if tmpt2.find('推 ')!=-1:
            #str1='1\t'
        if tmpt2.find('噓 ')!=-1:
            str1='0\t'
        else:
            continue
        text=t1.get_text(strip=True)
        tokens= [t for t in text.split()]
        for t in tokens:
            if t!=':':
                if(t[0]==':'):
                    str1+=t[1:]
                else:
                    str1+=t
        str1=str1+"\n"
        File.write(str1.encode('utf-8'))
def links(page):
    url = 'https://www.ptt.cc/bbs/Gossiping/index'+str(page)+'.html'
    resp=fetch(url)
    html=resp.text
    soup=BeautifulSoup(html,"html.parser")
    Soup=soup.find_all('div',class_="title")
    if Soup==[]:
        return False
    for line in Soup:
        h=line.find_all('a')
        if h==None:
            continue
        for hh in h:
            GetContent('https://www.ptt.cc'+hh.get('href'))
    return True



while(tt!=endindex):
    t=threading.Thread(target=links,args=(tt,))
    #GetContent('https://www.ptt.cc/bbs/Gossiping/M.1546930210.A.C04.html')
    t.start()
    t.join()
    print(tt)
    tt-=1
File.close()

'''
File=open('Gossip-Content.txt','rb')
ccc=0;
for i in File:
    ccc+=1
    if ccc>=10:
        break
    else:
        ccc+=1
    strX=i.decode('utf-8')
    xx=jieba.cut_for_search(strX)
    Length=sum(1 for x in xx)
    for x in xx:
        print(x)
    print(strX)
File.close()
'''
'''
for i in ur:
    print(i)
'''
'''
resp=fetch(url)
html=resp.text
soup=BeautifulSoup(html,"html.parser")
#抓連結    
for line in soup.select('.title'):
    h=line.find_all('a')
    for hh in h:
        ur.append(hh.get('href'))
'''
    
