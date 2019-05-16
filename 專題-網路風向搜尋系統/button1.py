import requests
import time
from bs4 import BeautifulSoup
TotalGood=0
TotalUn=0
TotalBad=0
TitlePageLinks = []
TitlePageTitles = []
TitlePageNames = []
SearchStr=''
Content=[]
option = {"cookie": "__cfduid=d2beeb4d6e110138543143fdb61585e081533740132; _ga=GA1.2.2109102077.1533740133; _gid=GA1.2.253250291.1543754336; over18=1"}

def Get(Link): 
    LinkData = BeautifulSoup(requests.get(Link,headers = option).text, "html.parser")
   
    Good = len(LinkData.find_all('span', string="推 "))
    Bad = len(LinkData.find_all('span', string="噓 "))
    Unknown = len(LinkData.find_all('span', string="→ "))
    global TotalGood
    global TotalUn
    global TotalBad
    TotalGood+=Good
    TotalUn+=Unknown
    TotalBad+=Bad
    return "{0:>3}, {1:>3}, {2:>3}".format(Good, Bad, Unknown)


def fetch(url):
    requ=requests.get(url,cookies={'over18':'1'})
    return requ
def Hot():
    #熱門看板========================
    MainPageData = requests.get("https://www.ptt.cc/bbs/index.html").text
    MainPage = BeautifulSoup(MainPageData, "html.parser")


    for link in MainPage.find_all('a', class_="board"):
        TitlePageLinks.append("https://www.ptt.cc"+link.get('href'))
        TitlePageTitles.append(link.find('div', class_="board-title").string)
        TitlePageNames.append(link.find('div', class_="board-name").string)

    for Index in range(len(TitlePageLinks)):
        print("{0:>3} {1:<15} {2}".format(Index,TitlePageNames[Index],TitlePageTitles[Index]))

    #PageData = requests.get(TitlePageLinks[eval(input("Please choose a topic to enter: "))],headers = option).text
    #Page = BeautifulSoup(PageData, "html.parser")

    #print("{0:>2}, {1:>2}, {2:>2} {3:^30}".format("推","噓","→", "----------標題----------"))
    #熱門看板=========================
def Search(str1,str2):
    global TotalGood
    global TotalBad
    #統計歸零
    TotalBad=0
    TotalGood=0
    SearchStr=str1
    for i in range(1,3):
        url='https://www.ptt.cc/bbs/'+str2+'/search?page='+str(i)+'&q='+SearchStr
        PageData = fetch(url).text
        Page = BeautifulSoup(PageData, "html.parser")
        if Page.find_all('div', class_="title")==[]:
            break
        for link in Page.find_all('div', class_="title"):
            title=link.find('a').string
            if title[0]=='R':
                continue
            try:
                Get("https://www.ptt.cc"+link.find('a').get('href'))
                #print("{0:>10} {1:<40}".format(Get("https://www.ptt.cc"+link.find('a').get('href')), link.find('a').string))
            except AttributeError: 
                print("{0:>10} {1:<40}".format("{0:>3}, {1:>3}, {2:>3}".format("NaN", "NaN", "NaN"), link.string.strip()))
    print(TotalGood,TotalBad)
def GetContent(url):
    global Content
    r=fetch(url)
    html=r.text;
    html.encode('utf-8')
    s=BeautifulSoup(html,"html.parser")

    #抓推文內容
    for t1,t2 in zip(s.find_all('span',class_='f3 push-content'),s.find_all('span',class_='push-tag')):
        tmpt2=str(t2)
        if tmpt2.find('推 ')!=-1:
            str1=''
        elif tmpt2.find('噓 ')!=-1:
            str1=''
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
        Content.append(str1)

def FetchCon(str1,str2):
    global Content
    for page in range(1,3):  
        url='https://www.ptt.cc/bbs/'+str2+'/search?page='+str(page)+'&q='+str1
        resp=fetch(url)
        html=resp.text
        soup=BeautifulSoup(html,"html.parser")
        Soup=soup.find_all('div',class_="title")
        if Soup==[]:
            return False
        for line in Soup:
            title=line.find('a').string
            if title[0]=='R':
                continue
            Content.append(title+"\n")
            h=line.find_all('a')
            if h==None:
                continue
            for hh in h:
                GetContent('https://www.ptt.cc'+hh.get('href'))
    return True

    
def GTotalGood():
    global TotalGood
    return TotalGood
def GTotalBad():
    global TotalBad
    return TotalBad
if __name__ == '__main__':
    Get()
    fetch()
    Hot()
    Search()
    GTotalGood()
    GTotalBad()
    FetchCon()
    GetContent()
