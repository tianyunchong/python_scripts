#!/bin/python2.7
# coding=utf-8
import sys,os
from sqlalchemy.ext.declarative import declarative_base
import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
BaseModel = declarative_base()
class BaseInitModel(object):
    '''
     base model
    '''
    defConfig = ""
    cpParser = None
    session = None

    def __init__(self, dbConfig):
        self.defConfig = dbConfig
        self.initByDbConf()
        self.initConnection()

    def initByDbConf(self):
        '''parse config file'''
        print self.defConfig
        if not os.path.exists(self.defConfig):
            raise Exception
        self.cpParser = ConfigParser.SafeConfigParser()
        self.cpParser.read(self.defConfig)

    def initConnection(self):
        '''init session and or '''
        user = self.cpParser.get("db", "user")
        password = self.cpParser.get("db", "pass")
        host = self.cpParser.get("db", "host")
        db = self.cpParser.get("db", "db")
        connectStr = 'mysql+mysqldb://%s:%s@%s/%s?charset=utf8' % (user, password, host, db)
        engine = create_engine(connectStr, echo=False)
        sessionClass = sessionmaker(bind=engine)
        self.session = sessionClass()