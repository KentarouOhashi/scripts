#!/usr/bin/env python
# coding: utf-8
#
# ファイルをリネームするスクリプト
#
# --- 使用する前に ---
# 18行目 : 拡張子を指定
# 19行目 : ファイル名を指定
# --------------------
import os
import re


def main():
    i = 1
    files = os.listdir('.')
    for file in files:
        if re.search(r'\.png$', file):
            os.rename(file, "image{0:d}.png".format(i))
            i += 1
        else:
            pass


if __name__ == '__main__':
    main()
