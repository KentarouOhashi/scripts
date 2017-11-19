#!/usr/bin/env python3
# coding: utf-8
#
# 指定したWebサイト内の特定の画像をダウンロード
#
# --- 使用する前に ---------------------------------
# 18行目 : URLを指定
# 24行目 : 取得する画像のURLを特定するためのHTMLを指定
# 30行目 : ダウンロードするファイルの拡張子を指定
# --------------------------------------------------
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import re
import os

BASE_URL = "<URL>"

def get_specific_url(url):
    """画像へのURLを取得しリストを返す"""
    html = urlopen(url)
    bsobj = BeautifulSoup(html, "html.parser")
    specific_urls = [i.get("href") for i in bsobj.find("div", {"class":"more"})
                                                            .findAll("a")]
    return specific_urls

def main(url, t):
    for img_url in get_specific_url(url):
        if re.search(r"\.gif$", img_url):
            rel = urlopen(img_url)
            with open(os.path.basename(img_url), "wb") as fp:
                fp.write(rel.read())
            urlretrieve(img_url)
            print(img_url + "  downloaded.", end="\n")
            time.sleep(t)

if __name__ == "__main__":
    main(BASE_URL, 3)
