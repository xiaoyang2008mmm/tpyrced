#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
from  base  import *
import fenye
import MySQLdb

class wenyuan_handler(BaseHandler):
    """返回文员html页面"""

    def get(self, *args, **kwargs):
        self.render("customer_a.html")


class customer_alter_handler(BaseHandler):
    """返回文员html页面"""

    def get(self, *args, **kwargs):
        self.render("customer_alter.html")


class jingjia_handler(BaseHandler):
    """返回竞价html页面"""

    def get(self, *args, **kwargs):
        self.render("jingjia.html")




class caiwu_handler(BaseHandler):
    """返回财务html页面"""

    def get(self, *args, **kwargs):
        self.render("caiwu.html")


class customerleft_handler(BaseHandler):

    def get(self,page):
        db = MySQLdb.connect("localhost","root","zkeys","tpyrced" )
        cursor = db.cursor()
        sql = "SELECT * FROM tpyrced_clerk"
        cursor.execute(sql)
        SHUJU  = cursor.fetchall()

        fen_ye = fenye.fen_ye_lei(page,SHUJU,10,11,5,'/customerleft/')       #执行分页对象

        if fen_ye.dang_qian_ye > fen_ye.zong_ye_ma:             #判断分页对象里的当前页码如果大于总页码
            zfchdqy = str(fen_ye.zong_ye_ma)                    #将总页码转换成字符串
            self.redirect("/customerleft/" + zfchdqy)                  #跳转到总页码
        else:
            self.render("customerleft.html",dqy=fen_ye.dang_qian_ye,shuju=fen_ye.shu_ju_fan_wei(),yem=fen_ye.xian_shi_ye_ma())


class employeeleft_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("employeeleft.html")


class saleleft_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("saleleft.html")

class financeleft_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("financeleft.html")

class biddingleft_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("biddingleft.html")
class systemleft_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("systemleft.html")

class caiwu_add_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("finance_a.html.html")

class caiwu_modify_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("finance_alter.html.html")




class biddingleft_add_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("bidding_a.html.html")
class biddingleft_modify_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("bidding_alter.html")
