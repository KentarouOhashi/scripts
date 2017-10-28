#!/usr/bin/env python3
# coding: utf-8
from get_img_multiprocessing import get_specific_url, get_img
from urllib.request import urlopen
from bs4 import BeautifulSoup
from unittest import TestCase, skip, main

class TestGetImgMultiprocessing(TestCase):
 
    def setUp(self):
        self.url = "<URL>"
    
    def test_get_specific_url(self):
        """
        get_specific_urlのテストメソッド
        """
        html = urlopen(self.url)
        bsobj = BeautifulSoup(html, 'html.parser')
        urls = [i.get("href") for i in bsobj.find("div",
                                        {"class":"more"}).findAll("a")]
        self.assertListEqual(get_specific_url(self.url), urls)

if __name__ == "__main__":
    main()
