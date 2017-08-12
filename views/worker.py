#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
from  base  import *
from models.db  import *
import fenye
import MySQLdb

class wenyuan_handler(BaseHandler):
    """返回文员html页面"""

    def get(self, *args, **kwargs):
        self.render("customer_a.html")


class customer_alter_handler(BaseHandler):
    """返回文员html页面"""

    def get(self, *args, **kwargs):
        client_id = int(self.request.arguments['client_id'][0])
	st2 = TpyrcedClerk.get(TpyrcedClerk.id == client_id)
	__dict = {"st2":st2}
        self.render("customer_alter.html",**__dict)


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

    def get(self,page):
        db = MySQLdb.connect("localhost","root","zkeys","tpyrced" )
        cursor = db.cursor()
        sql = "SELECT * FROM tpyrced_finadd"
        cursor.execute(sql)
        SHUJU  = cursor.fetchall()

        fen_ye = fenye.fen_ye_lei(page,SHUJU,10,11,5,'/financeleft/')       #执行分页对象

        if fen_ye.dang_qian_ye > fen_ye.zong_ye_ma:             #判断分页对象里的当前页码如果大于总页码
            zfchdqy = str(fen_ye.zong_ye_ma)                    #将总页码转换成字符串
            self.redirect("/financeleft/" + zfchdqy)                  #跳转到总页码
        else:
            self.render("financeleft.html",dqy=fen_ye.dang_qian_ye,shuju=fen_ye.shu_ju_fan_wei(),yem=fen_ye.xian_shi_ye_ma())



class biddingleft_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("biddingleft.html")
class systemleft_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("systemleft.html")




class caiwu_modify_handler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("finance_alter.html")




class wenyuan_modify_handler(BaseHandler):

    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        db_key  = request_dict['db_key'][0]
	db_id  = int(request_dict['db_id'][0])
	cus_val = request_dict['cus_val'][0]

	if db_key == "client_tel":
	    TpyrcedClerk.update(client_tel=cus_val).where(TpyrcedClerk.id == db_id).execute()
	if db_key == "client_name":
	    TpyrcedClerk.update(client_name=cus_val).where(TpyrcedClerk.id == db_id).execute()
	if db_key == "is_send":
	    TpyrcedClerk.update(is_send=cus_val).where(TpyrcedClerk.id == db_id).execute()
	if db_key == "is_valid":
	    TpyrcedClerk.update(is_valid=cus_val).where(TpyrcedClerk.id == db_id).execute()
	if db_key == "key_words":
	    TpyrcedClerk.update(key_words=cus_val).where(TpyrcedClerk.id == db_id).execute()
	if db_key == "tel_where":
	    TpyrcedClerk.update(tel_where=cus_val).where(TpyrcedClerk.id == db_id).execute()
	if db_key == "tl_area":
	    TpyrcedClerk.update(tl_area=cus_val).where(TpyrcedClerk.id == db_id).execute()
	if db_key == "invite":
	    TpyrcedClerk.update(invite=cus_val).where(TpyrcedClerk.id == db_id).execute()
	if db_key == "subscribe":
	    TpyrcedClerk.update(subscribe=cus_val).where(TpyrcedClerk.id == db_id).execute()
	if db_key == "remark_text":
	    TpyrcedClerk.update(remark_text=cus_val).where(TpyrcedClerk.id == db_id).execute()
