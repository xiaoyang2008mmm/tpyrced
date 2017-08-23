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




class employeeleft_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("employeeleft.html")


class saleleft_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("saleleft.html")

class financeleft_handler(BaseHandler):

    def get(self,*args,**kwargs):
        try:
            index = int(self.request.arguments['index'][0])
            page = int(self.request.arguments['page'][0])
        except:
            index = 0
            page = 1



        if index == 0 :
            req = self.request.arguments
            data={}
            if req.has_key('f_card_date'):
                card_date = req['f_card_date'][0]
                if card_date : data['card_date'] = card_date

            if req.has_key('f_sub_date'):
                sub_date = req['f_sub_date'][0]
                if sub_date : data['sub_date'] = sub_date

            if req.has_key('f_cus_name'):
                cus_name = req['f_cus_name'][0]
                if cus_name : data['cus_name'] = cus_name

            if req.has_key('f_pro_name'):
                pro_name = req['f_pro_name'][0]
                if pro_name : data['pro_name'] = pro_name

            if data:
                SHUJU  = TpyrcedFinadd.select().filter(**data).order_by(TpyrcedFinadd.id.desc())
                for i in SHUJU:
                     i.card_date
            else:
                SHUJU  = TpyrcedFinadd.select().order_by(TpyrcedFinadd.id.desc())

        if index == 1 :
            SHUJU  = TpyrcedSaleadd.select().order_by(TpyrcedSaleadd.id.desc())

        fen_ye = fenye.fen_ye_lei(page,SHUJU,10,11,5,'/financeleft/')       #执行分页对象


        if fen_ye.dang_qian_ye > fen_ye.zong_ye_ma:             #判断分页对象里的当前页码如果大于总页码
            zfchdqy = str(fen_ye.zong_ye_ma)                    #将总页码转换成字符串
            self.redirect("/financeleft/" + zfchdqy)                  #跳转到总页码
        else:
            self.render("financeleft.html",dqy=fen_ye.dang_qian_ye,shuju=fen_ye.shu_ju_fan_wei(),yem=fen_ye.xian_shi_ye_ma())

        

class biddingleft_handler(BaseHandler):

    def get(self,*args,**kwargs):
        try:
            index = int(self.request.arguments['index'][0])
            page = int(self.request.arguments['page'][0])
        except:
            index = 0
            page = 1



        if index == 0 :
            req = self.request.arguments
            data={}
            if req.has_key('b_area_main'):
                area_main = req['b_area_main'][0]
                if area_main : data['area_main'] = area_main

            if req.has_key('b_area_cons'):
                area_cons = req['b_area_cons'][0]
                if area_cons : data['area_cons'] = area_cons

            if req.has_key('b_bid_elec'):
                bid_elec = req['b_bid_elec'][0]
                if bid_elec : data['bid_elec'] = b_bid_elec

            if data:
                SHUJU  = TpyrcedBidadd.select().filter(**data).order_by(TpyrcedBidadd.id.desc())
                for i in SHUJU:
                     i.area_main
            else:
                SHUJU  = TpyrcedBidadd.select().order_by(TpyrcedBidadd.id.desc())
                   
        if index == 1 :
            SHUJU  = TpyrcedSaleadd.select().order_by(TpyrcedSaleadd.id.desc())
                    
        fen_ye = fenye.fen_ye_lei(page,SHUJU,10,11,5,'/biddingleft/')       #执行分页对象


        if fen_ye.dang_qian_ye > fen_ye.zong_ye_ma:             #判断分页对象里的当前页码如果大于总页码
            zfchdqy = str(fen_ye.zong_ye_ma)                    #将总页码转换成字符串
            self.redirect("/biddingleft/" + zfchdqy)                  #跳转到总页码
        else:
            self.render("biddingleft.html",dqy=fen_ye.dang_qian_ye,shuju=fen_ye.shu_ju_fan_wei(),yem=fen_ye.xian_shi_ye_ma())
class systemleft_handler(BaseHandler):

    def get(self, *args, **kwargs):
	role = TpyrcedSysRole.select()
	url = TpyrcedUrl.select()
	user = TpyrcedUser.select()
	__dict = {'allrole':role, 'alluser':user, 'allurl':url}
        self.render("systemleft.html",**__dict)




class caiwu_xiugai_handler(BaseHandler):
    def get(self, *args, **kwargs):
        f_id = int(self.request.arguments['f_id'][0])
        #st2 = TpyrcedFinadd.get(TpyrcedFinadd.id == f_id)
        #__dict = {"st2":st2}
        self.render("finance_alter.html")
    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        db_key  = request_dict['db_key'][0]
        db_id  = int(request_dict['db_id'][0])
        fin_val = request_dict['fin_val'][0]

        dd ={db_key:fin_val}
        try:
            TpyrcedFinadd.update(**dd).where(TpyrcedFinadd.id == db_id).execute()
            self.write("数据录入成功!!!!!!")
        except:
            self.write("数据写入失败,请联系管理员!!!!!")



class wenyuan_modify_handler(BaseHandler):

    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        db_key  = request_dict['db_key'][0]
	db_id  = int(request_dict['db_id'][0])
	cus_val = request_dict['cus_val'][0]

	dd ={db_key:cus_val}
	try:
	    TpyrcedClerk.update(**dd).where(TpyrcedClerk.id == db_id).execute()
	    self.write("数据录入成功!!!!!!")
	except:
	    self.write("数据写入失败,请联系管理员!!!!!")
class biddingleftdelete_handler(BaseHandler):

    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        bid = request_dict['pro_name'][0]


        if isinstance(bid,int):
                st = TpyrcedBidadd.get(id = int(bid))
                st.delete_instance()
        else:
            for cid in (bid).split(","):
                st = TpyrcedBidadd.get(id = int(cid))
                st.delete_instance()

        self.write("删除成功!!!")

