#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
from  base  import *

class wenyuan_handler(BaseHandler):
    """返回文员html页面"""

    def get(self, *args, **kwargs):
        self.render("customer_a.html")




class jingjia_handler(BaseHandler):
    """返回竞价html页面"""

    def get(self, *args, **kwargs):
        self.render("jingjia.html")




class caiwu_handler(BaseHandler):
    """返回财务html页面"""

    def get(self, *args, **kwargs):
        self.render("caiwu.html")




