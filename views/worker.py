#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
       return self.application.db

class wenyuan_handler(BaseHandler):
    """返回文员html页面"""

    def get(self, *args, **kwargs):
        self.render("employee_a.html")




class jingjia_handler(BaseHandler):
    """返回竞价html页面"""

    def get(self, *args, **kwargs):
        self.render("jingjia.html")




class caiwu_handler(BaseHandler):
    """返回财务html页面"""

    def get(self, *args, **kwargs):
        self.render("caiwu.html")




