#!/usr/bin/env python3
# coding: utf-8
from unittest import TestCase, main
from get_img import get_img_url
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class TestGetImg(TestCase):

    def setUp(self):
        self.url = "<URL>"

    def test_get_img_url(self):
        """
        get_img_urlのテストメソッド
        """
        html = urlopen(self.url)
        bsobj = BeautifulSoup(html, 'html.parser')
        urls = [i.get("src") for i in bsobj.findAll("img", \
                        src=re.compile(r"^http\:\/\/blog\-imgs\-[0-9]{2}"))]
        self.assertListEqual(get_img_url(self.url), urls)

if __name__ == "__main__":
    main()
