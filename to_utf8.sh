#!/bin/bash
# エンコードをUTF-8に変換するスクリプト

files=(`ls -1`)

for file in ${files[@]}
do
  nkf -w --overwrite $file
done
