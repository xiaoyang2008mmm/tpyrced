# -*- coding: utf-8 -*- 
import tornado.web
from models.db  import *

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
       return self.application.db

class WenYuanAdd_handler(BaseHandler):
    """获取文员录入的信息并且入库"""

    def post(self, *args, **kwargs):
	request_dict = self.request.arguments
	print request_dict

	save_time  = request_dict['save_time'][0]
	client_tel =request_dict['client_tel'][0]
	client_name= request_dict['client_name'][0]
	is_send = request_dict['is_send'][0]
	is_valid = request_dict['is_valid'][0]
	key_words = request_dict['key_words'][0]
	tel_where = request_dict['tel_where'][0]
	tl_area = request_dict['tl_area'][0]
	invite = request_dict['invite'][0]
	subscribe =  request_dict['subscribe'][0]
	remark_text = request_dict['remark_text'][0]

	
	try:
	    q =TpyrcedClerk.insert(save_time = save_time,client_tel = client_tel,client_name = client_name,is_send = is_send,is_valid = is_valid,key_words = key_words,tel_where = tel_where,tl_area = tl_area,invite = invite,subscribe = subscribe, remark_text=remark_text)
	    q.execute()
	    self.write("数据写入成功!!")
	except:

	    self.write("电话号码在数据库中已经有记录,请联系管理员!!!")



class JingJiaAdd_handler(BaseHandler):
    """获取竞价录入的信息并且入库"""

    def post(self, *args, **kwargs):
	request_dict = self.request.arguments
	print request_dict



class CaiWuAdd_handler(BaseHandler):
    """获取财务录入的信息并且入库"""

    def post(self, *args, **kwargs):
	request_dict = self.request.arguments
	print request_dict



