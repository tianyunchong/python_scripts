#!/bin/python2.7
#coding=utf-8
import os,sys
sys.path.append(os.path.dirname(os.getcwd()))
from models.baseModel import *
obj = BaseInitModel("/data/cap/python/python_scripts/config/base.conf")
print obj.session