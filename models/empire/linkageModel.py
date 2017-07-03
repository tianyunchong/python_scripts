#!/bin/python2.7
#coding=utf-8
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR, SMALLINT
from models.baseModel import BaseModel, BaseInitModel
class LinkageModel(BaseInitModel, BaseModel):
    __tablename__ = "phome_linkage"
    linkage_id = Column(Integer, primary_key=True)
    parent_id  = Column(Integer)
    linkage_name = Column(VARCHAR(255))
    linkage_type = Column(Integer)
    linkage_path = Column(VARCHAR(255))
    linkage_sort = Column(SMALLINT)
    lft = Column(Integer)
    rgt = Column(Integer)
    bakdata = Column(VARCHAR(200))
    pinyin = Column(VARCHAR(50))

    def exist(self, value):
        '''check info is exist'''
        res = self.session.query(self.__class__).filter(self.__class__.linkage_name == value).first()
        if res:
            return True
        return False

    def getQuery(self):
        '''return query'''
        query = self.session.query(self.__class__)
        return query