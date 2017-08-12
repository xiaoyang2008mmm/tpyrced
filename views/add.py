#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
from  base  import *
from models.db  import *
import fenye
import MySQLdb


"""财务数据添加"""
class caiwu_add_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("finance_a.html")

    def post(self, *args, **kwargs):
        request_dict = self.request.arguments

	save_time  = request_dict['save_time'][0]
        team_name  = request_dict['team_name'][0]
        ord_num  =request_dict['ord_num'][0]
        card_date = request_dict['card_date'][0]
        sub_date = request_dict['sub_date'][0]
        cus_name = request_dict['cus_name'][0]
        pro_name = request_dict['pro_name'][0]
        tran_status = request_dict['tran_status'][0]
        com_stand = request_dict['com_stand'][0]
        fav_able = request_dict['fav_able'][0]
        act_amount = request_dict['act_amount'][0]
        tran_dire = request_dict['tran_dire'][0]
        prop_tion = request_dict['prop_tion'][0]
        sep_dire = request_dict['sep_dire'][0]
        inve_prop = request_dict['inve_prop'][0]
        source_tran = request_dict['source_tran'][0]
        com_form = request_dict['com_form'][0]

	try:
	    q =TpyrcedFinadd.insert(save_time= save_time ,team_name = team_name,ord_num = ord_num,card_date = card_date,sub_date = sub_date,cus_name = cus_name,pro_name = pro_name,tran_status = tran_status,com_stand = com_stand,fav_able = fav_able,act_amount = act_amount,  tran_dire = tran_dire , prop_tion=prop_tion, sep_dire=sep_dire, inve_prop=inve_prop,source_tran=source_tran, com_form=com_form )
	    q.execute()
	    self.write("数据写入成功!!")
	except:
	    self.write("数据写入失败,请联系管理员!!")






class caiwu_modify_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("finance_alter.html")




class biddingleft_add_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("bidding_a.html")
    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
	print request_dict

class biddingleft_modify_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("bidding_alter.html")
