#!/usr/bin/env python3
# coding: utf-8
#
# 2つのWebサイトから並列処理にて
# 指定した拡張子の画像をダウンロードするスクリプト
#
# --- multiprocessing ---
#
# --- 使用する前に ---------------------------
# 23行目 : URL1を指定
# 24行目 : URL2を指定
# 30行目 : 取得するURLを特定するためのHTMLを指定
# 37行目 : ファイルの拡張子を指定
# --------------------------------------------
from multiprocessing import Process
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import re
import os

URL1 = "<URL1>"
URL2 = "<URL2>"

def get_specific_url(url):
    """URLを取得してそのリストを返す"""
    html = urlopen(url)
    bsobj = BeautifulSoup(html, "html.parser")
    specific_urls = [i.get("href") for i in bsobj.find("div",
                                                {"class":"more"}).findAll("a")]
    return specific_urls

def get_img(url, t, labelfile, labelout):
    """GIF画像をダウンロード"""
    for img_url in get_specific_url(url):
        if re.search(r"\.gif$", img_url):
            rel = urlopen(img_url)
            with open(os.path.basename(img_url), "wb") as fp:
                fp.write(rel.read())
            urlretrieve(img_url)
            os.rename(os.path.basename(img_url),
                        "{0}".format(labelfile) + os.path.basename(img_url))
            print("[{0}] : ".format(labelout) + img_url + "  downloaded.",
                                                                    end="\n")
            time.sleep(t)

def main(url1, t1, ulabel1, label1, url2, t2, ulabel2, label2):
    process1 = Process(name="process1", target=get_img,
                                                args=(url1, t1, ulabel1, label1))
    process2 = Process(name="process2", target=get_img,
                                                args=(url2, t2, ulabel2, label2))

    process1.start()
    process2.start()
    process1.join()
    process2.join()

if __name__ == "__main__":
    main(URL1, 2, "url1-", "1st", URL2, 3, "url2-", "2nd")
