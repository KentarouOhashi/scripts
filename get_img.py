#!/usr/bin/env python3
# coding: utf-8
#
# 指定したWebサイトから指定した拡張子の画像をダウンロード
#
# --- 使用する前に ---
# 18行目 : URLを指定
# 24行目 : 目的のWebサイトに合わせてHTMLタグを指定
# 31行目 : ファイルの拡張子を指定
# --------------------
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import re
import os

BASE_URL = "<URL>"

def get_img_url(url):
    """画像のURLを取得しリストを返す"""
    html = urlopen(url)
    bsobj = BeautifulSoup(html, "html.parser")
    img_urls = [i.get("src") for i in bsobj.findAll("img",
                        src=re.compile(r"^http\:\/\/blog\-imgs\-[0-9]{2}"))]

    return img_urls

def main(url):
    for img_url in get_img_url(url):
        if re.search(r"\.gif$", img_url):
            res = urlopen(img_url)
            with open(os.path.basename(img_url), "wb") as fp:
                fp.write(res.read())
            urlretrieve(img_url)
            print(img_url + "  downloaded.", end="\n")
            time.sleep(5)

if __name__ == "__main__":
    main(BASE_URL)
