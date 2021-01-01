#!/usr/bin/env python3
import requests
import sys
import queue
from bs4 import BeautifulSoup
import threading
import time
import re
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/76.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive'
        }


class BaiduURL(threading.Thread):
    def __init__(self,queue1):
        threading.Thread.__init__(self)
        self._queue = queue1

    def run(self):
        while not self._queue.empty():
            url = self._queue.get_nowait()
            spider(url)
def spider(url):
    res = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(res.content.decode('utf-8'),'lxml')
    urls = soup.find_all(name='a',attrs={'class':'','data-click':re.compile(('.'))})
    for urll in urls:
        try:
            r_get_url = requests.get(url=urll['href'],headers=headers,timeout=8)
        except:
            pass
        if r_get_url.status_code == 200:
            print(r_get_url.url)
def main(keyword):
    queue1 = queue.Queue()
    for i in range(0,40,10):
        queue1.put(f'http://www.baidu.com/s?wd={keyword}&pn={str(i)}')

    threads = []
    thread_count = 1

    for i in range(thread_count):
        threads.append(BaiduURL(queue1))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:python3 getURL.py [keyword]')
        sys.exit(-1)
    else:
        print("""
              _    _   _  ____   _      _          __        
  __ _   ___ | |_ | | | ||  _ \ | |    (_) _ __   / _|  ___  
 / _` | / _ \| __|| | | || |_) || |    | || '_ \ | |_  / _ \ 
| (_| ||  __/| |_ | |_| ||  _ < | |___ | || | | ||  _|| (_) |
 \__, | \___| \__| \___/ |_| \_\|_____||_||_| |_||_|   \___/ 
 |___/                                                       
                            Author:NorthShad0w   Version:1.0  
                            Support Search Engine:Baidu
        """)
        main(sys.argv[1])


