#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
       return self.application.db
class Index_Handler(BaseHandler):

    def get(self,*args,**kwargs):
        self.render('index.html') 


