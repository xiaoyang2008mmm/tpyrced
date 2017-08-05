# -*- coding: utf-8 -*- 
from models.db  import *
import fenye
import MySQLdb
from base  import *
class Index_Handler(BaseHandler):

    def get(self,*args,**kwargs):
        current_user=self.get_current_user()
        self.render("base.html",current_user=current_user)



class Iframe_Handler(BaseHandler):



    def get(self,page):                                              #get()方法，接收get方式请求
	db = MySQLdb.connect("localhost","root","zkeys","tpyrced" )
	cursor = db.cursor()
	sql = "SELECT * FROM tpyrced_clerk"
	cursor.execute(sql)
	SHUJU  = cursor.fetchall()

        fen_ye = fenye.fen_ye_lei(page,SHUJU,10,11,5,'/iframe/')       #执行分页对象

        if fen_ye.dang_qian_ye > fen_ye.zong_ye_ma:             #判断分页对象里的当前页码如果大于总页码
            zfchdqy = str(fen_ye.zong_ye_ma)                    #将总页码转换成字符串
            self.redirect("/iframe/" + zfchdqy)                  #跳转到总页码
        else:
            self.render("iframe.html",dqy=fen_ye.dang_qian_ye,shuju=fen_ye.shu_ju_fan_wei(),yem=fen_ye.xian_shi_ye_ma())



class test_handler(BaseHandler):

    def get(self,*args,**kwargs):
        self.render('customer_b.html')

