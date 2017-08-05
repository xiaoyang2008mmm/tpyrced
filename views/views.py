# -*- coding: utf-8 -*- 
from models.db  import *
import tornado.web
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
       return self.application.db
class Index_Handler(BaseHandler):

    def get(self,*args,**kwargs):
        self.render('base.html') 


class Iframe_Handler(BaseHandler):

    def get(self,*args,**kwargs):

	all_clerk = TpyrcedClerk.select()
	_dict = {"all_clerk" : all_clerk}
        self.render('iframe.html', **_dict) 

class test_handler(BaseHandler):

    def get(self,*args,**kwargs):
        self.render('customer_b.html')

