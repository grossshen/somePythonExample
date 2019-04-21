import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json
import pandas
import time

# 新浪新闻首页https://news.sina.com.cn/china
#
def getAllArticles(sourceUrl):
    newsUrls=getNewsUrls()
    newsDetails=[]
    for p in newsUrls:
        newsDetails.append(p.text.strip())
    return newsDetails

def getNewsUrls():
    sourceUrl = 'https://news.sina.com.cn/china/'
    res=requests.get(sourceUrl)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'lxml')

    newsRowLink = soup.find_all('a',attrs={"href": True})
    newsLinks = []
    pattern=r'http.*doc.*html'
    for newsLink in newsRowLink:
        if(re.match(pattern,newsLink['href'])):
            newsLinks.append(newsLink['href'])
            time.sleep(0.2)
    return newsLinks

def getNewsdetail(newsUrl):
    newsUrl='https://news.sina.com.cn/c/2019-04-19/doc-ihvhiewr7168445.shtml'
    res=requests.get(newsUrl)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'lxml')

    newsTitle=str(soup.find("h1",class_="main-title"))
    newsArticle=str(soup.find("div",class_="article"))
    list=[newsTitle,newsArticle]
    jsonObject=json.dumps(list)
    return list


def test1():
    pattern = r'http(.*)html'
    if(re.match(pattern,'javascript:;',re.M|re.I)):
        print("xxxxxxxxxxxx")
    elif(re.match(pattern,'http://www.sina.com.html')):
        print("yyyyyyyyyyyyy")
    else:print("zzzzzzzzzzz")


def main():
    getNewsdetail('https://news.sina.com.cn/c/2019-04-19/doc-ihvhiewr7168445.shtml')
    # test1()
    pass



if __name__=='__main__':
    main()
