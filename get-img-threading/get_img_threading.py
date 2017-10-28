#!/usr/bin/env python3
# coding: utf-8
#
# 2つのWebサイトから並列処理にて
# 指定した拡張子の画像をダウンロードするスクリプト
#
# --- threading ---
#
# --- 使用する前に ---------------------------
# 17行目 : URLを指定
# 18行目 : URLを指定
# 31行目 : ファイルの拡張子を指定
# 45行目 : 画像へのURLを特定するためのHTMLを記述
# 52行目 : ファイルの拡張子を指定
# --------------------------------------------
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading
import time
import re
import os

URL1 = "<URL>"
URL2 = "<URL>"

def get_specific_url(url):
    """画像へのURLを取得しリストを返す"""
    html = urlopen(url)
    bsobj = BeautifulSoup(html, "html.parser")
    specific_urls = [i.get("href") for i in bsobj.find("div",
                                                {"class":"more"}).findAll("a")]
    return specific_urls

class MultiprocessScraping(threading.Thread):
    """ threading.Threadのサブクラスの定義"""

    def __init__(self, url1, time1):
        super(MultiprocessScraping, self).__init__()
        self.url = url1
        self.time = time1

    def run(self):
        """GIF画像をダウンロードするメソッド"""
        for img_url in get_specific_url(self.url):
            if re.search(r"\.gif$", img_url):
                rel = urlopen(img_url)
                with open(os.path.basename(img_url), "wb") as fp:
                    fp.write(rel.read())
                urlretrieve(img_url)
                os.rename(os.path.basename(img_url),
                                        "url1-" + os.path.basename(img_url))
                print("[1st] : " + img_url + "  downloaded.", end="\n")
                time.sleep(self.time)

def multiprocess_scraping(url2, time2):
    """GIF画像へのURLを取得し、画像をダウンロードするメソッド"""
    for img_url in get_specific_url(url2):
        if re.search(r"\.gif$", img_url):
            rel = urlopen(img_url)
            with open(os.path.basename(img_url), "wb") as fp:
                fp.write(rel.read())
            urlretrieve(img_url)
            os.rename(os.path.basename(img_url),
                                        "url2-" + os.path.basename(img_url))
            print("[2nd] : " + img_url + "  downloaded.", end="\n")
            time.sleep(time2)

def _main(url1, time1, url2, time2):
    thread1 = MultiprocessScraping(url1, time1)
    thread1.start()

    # threading.Threadのインスタンスを作る
    thread2 = threading.Thread(target=multiprocess_scraping, name="thread2",
                                                                args=(url2, time2))
    thread2.start()

if __name__ == "__main__":
    _main(URL1, 2, URL2, 3)
