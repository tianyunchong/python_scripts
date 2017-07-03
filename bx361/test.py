#!/bin/python2.7
#coding=utf-8
import os,sys
sys.path.append(os.path.dirname(os.getcwd()))
from models.empire.linkageModel import LinkageModel
from pinyin import pinyin
obj = LinkageModel("/data/cap/python/python_scripts/config/base.conf")
query = obj.getQuery()
num = 0
for item in query:
    if item.parent_id != 18:
        continue
    pinyinStr = pinyin.get(item.linkage_name, "", format="strip")
    item.pinyin = pinyinStr
    print item.linkage_name
    obj.session.commit()
