# -*- coding: utf-8 -*-
import re

import requests
from bs4 import BeautifulSoup


def getUrlInfo(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    res.encoding = 'gb18030'
    return res.text


def writeFile(file, mode):
    return open(file, mode, encoding="utf-8")


def resolveDetail(url):
    print(url)
    soup = BeautifulSoup(getUrlInfo(url), 'lxml')
    replyContentTag = soup.find('div', class_='ReplyContent')
    pTag = replyContentTag.findAll('p')
    w = writeFile('./result/price.txt', 'a')
    w.write
    for i in range(len(pTag)):
        tx = pTag[i].text
        if tx.find('年') > 0:
            year = tx[0:tx.find("年")]
            month = tx[tx.find("年") + 1: tx.find("月")]
            day = tx[tx.find("月") + 1: tx.find("日")]
            w.write(str(year + '.' + month + '.' + day))
            w.write('   |   ')
            trend = tx[tx.find("：") + 1: tx.find(";")]
            w.write(trend)
        if tx.find('江西-南昌') > 0:
            price = re.search("\d+(\.\d+)?", tx)
            print(price.group())
            w.write('   |   ')
            w.write(price.group())
        if tx.find('江西-宜春') > 0:
            price = re.search("\d+(\.\d+)?", tx)
            print(price.group())
            w.write('   |   ')
            w.write(price.group())
        if tx.find('江西-九江') > 0:
            price = re.search("\d+(\.\d+)?", tx)
            print(price.group())
            w.write('   |   ')
            w.write(price.group())
        if tx.find('江西-德安') > 0:
            price = re.search("\d+(\.\d+)?", tx)
            print(price.group())
            w.write('   |   ')
            w.write(price.group())
    w.write('\n')
    w.close()


if __name__ == '__main__':
    for i in range(5):
        url = "http://www.feedtrade.com.cn/e/search/result/index.php?searchid=12857&page=" + str(i)
        soup = BeautifulSoup(getUrlInfo(url), 'lxml')
        h2Tag = soup.findAll('h2', class_='r')
        print(h2Tag)
        for i in range(len(h2Tag)):
            resolveDetail(h2Tag[i].a.get('href'))
