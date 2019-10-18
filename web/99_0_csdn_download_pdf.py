# TODO
# 我想获取http://www.delixi-electric.com/cpzx/index.htm这个网站的电气说明书PDF
# import requests
# import urllib.request
from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import os

# request.HTTPBasicAuthHandler

def collect_category(url):
    category_urls = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    r = request.Request(url, headers = headers)
    r = request.urlopen(r)
    text = r.read()
    # h = soup.select('ul.down_right_td')
    # t = soup.select('li.down_right_bd')
    # urls = soup.select("ul.down_right_td li.down_right_bd")
    soup = BeautifulSoup(text, "html.parser")
    t = soup.select("div.pro_menu")
    urls = soup.select("div.pro_menu ul li a")
    for i in urls:
        category_urls.append("http://www.delixi-electric.com/"+i.get("href"))
    print (category_urls)
    return category_urls

def collect_items(url):
    items_urls = []
    headers = {

"Content-Length": "20",
"Pragma": "no-cache",
"Cache-Control": "no-cache",
"Accept": "application/json, text/javascript, */*; q=0.01",
"Origin": "http://www.delixi-electric.com",
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Referer": "http://www.delixi-electric.com/dcyb/index.htm",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
# Cookie: _site_id_cookie=5; clientlanguage=zh_CN; Hm_lvt_0e9b7c72b8f056c27fe83526d2f7d660=1571225284; JSESSIONID=EBC7617FB2C8D7A662EF2FC17BBFA860.hsapp2; Hm_lpvt_0e9b7c72b8f056c27fe83526d2f7d660=1571228084
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',

    }
    data = {
        "channleId": "414",
        "type": "1"
    }
    r = request.Request(url, headers = headers, data = data)
    r = request.urlopen(r)
    soup = BeautifulSoup(r.text, "html.parser")
    urls = soup.select("#pro_list > li > a")
    for i in urls:
        items_urls.append("http://www.delixi-electric.com/"+i.get("href"))
    return items_urls

def download_pdf(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    r = request.Request(url, headers = headers)
    r = request.urlopen(r)
    soup = BeautifulSoup(r.text, "html.parser")
    urls = soup.select("body > div:nth-child(10) > div > div:nth-child(3) > ul > li > a")

    for i in urls:

        name = i.get_text()
        name = re.sub("/", "", name)
        print (name)

        if os.path.exists('D:/delixi/%s.pdf' % name):
            print("文件已存在")
            continue

        pdf_url = "http://www.delixi-electric.com/"+i.get("href")
        print (pdf_url)
        u = request.urlopen(pdf_url)
        print ("进入成功，正在下载......")
        block_sz = 8192
        with open('E:/test/%s.pdf' % name, 'wb') as f:
            while True:
                buffer = u.read(block_sz)
                if buffer:
                    f.write(buffer)
                else:
                    print('第%d个文件已下载' % n)
                    break
        print ("=====================")


url = "http://www.delixi-electric.com/dcyb/index.htm"
# url = "http://www.delixi-electric.com/queryProductFile.jspx"
try:
    category_urls = collect_category(url)
except HTTPError as e:
    print(e.read().decode('utf-8'))
    exit(0)
print ("目录链接收集完毕")
n = 0
for i in category_urls:
    items_urls = collect_items(i)
    print ("准备开始下载PDF")
    for a in items_urls:
        n+=1
        download_pdf(a)
print ("全部文件下载完毕")
