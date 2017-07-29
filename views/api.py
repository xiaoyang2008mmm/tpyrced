#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
       return self.application.db

class WenYuanAdd_handler(BaseHandler):
    """获取文员录入的信息并且入库"""

    def post(self, *args, **kwargs):
	request_dict = self.request.arguments
	print request_dict



