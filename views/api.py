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
	
	q =TpyrcedClerk.insert(client_name="wqwdqwqw")
	q.execute()



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



