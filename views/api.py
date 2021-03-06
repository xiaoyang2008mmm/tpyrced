# -*- coding: utf-8 -*- 
import tornado.web
from models.db  import *
from base import *


class WenYuanAdd_handler(BaseHandler):
    """获取文员录入的信息并且入库"""

    def post(self, *args, **kwargs):
	request_dict = self.request.arguments

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

class WenYuandelete_handler(BaseHandler):
    """删除文员录入的数据"""

    def post(self, *args, **kwargs):
	request_dict = self.request.arguments
	client_telphone  = request_dict['client_telphone'][0]


	if ',' not in (client_telphone) :
	        st = TpyrcedClerk.get(id = int(client_telphone))
	        st.delete_instance()
	else:
	    for cid in (client_telphone).split(","):
	        st = TpyrcedClerk.get(id = int(cid))
	        st.delete_instance()

	self.write("删除成功!!!")


class Caiwudelete_handler(BaseHandler):
    """删除财务录入的数据"""

    def post(self, *args, **kwargs):
	request_dict = self.request.arguments
	pro_name = request_dict['pro_name'][0]


	if isinstance(pro_name,int):
	        st = TpyrcedFinadd.get(id = int(pro_name))
	        st.delete_instance()
	else:
	    for cid in (pro_name).split(","):
	        st = TpyrcedFinadd.get(id = int(cid))
	        st.delete_instance()

	self.write("删除成功!!!")



class JingJiaAdd_handler(BaseHandler):
    """获取竞价录入的信息并且入库"""


class JingJiaAdd_handler(BaseHandler):
    """获取竞价录入的信息并且入库"""

    def post(self, *args, **kwargs):
	request_dict = self.request.arguments



class CaiWuAdd_handler(BaseHandler):
    """获取财务录入的信息并且入库"""

    def post(self, *args, **kwargs):
	request_dict = self.request.arguments

class saledelete_handler(BaseHandler):
    """删除销售录入的数据"""

    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        sa_le = request_dict['pro_name'][0]


        if isinstance(sa_le,int):
                st = TpyrcedSaleadd.get(id = int(sa_le))
                st.delete_instance()
        else:
            for cid in (sa_le).split(","):
                st = TpyrcedSaleadd.get(id = int(cid))
                st.delete_instance()

        self.write("删除成功!!!")
