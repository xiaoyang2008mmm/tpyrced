# -*- coding: utf-8 -*- 
import tornado.web
from models.db  import *


class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        if not self.request.uri.startswith(self.get_login_url()) and self.current_user is  None:
            self.redirect(self.get_login_url())

    def get_current_user(self):
        user_cookie = self.get_cookie("anju_user")
        if user_cookie:
            return user_cookie
        return None

    def privilege_check(self,user):
	urllist = self.get_urllist(self.get_role(user))
	return   urllist

    def get_template_namespace(self):
        namespace = {}
        namespace = super(BaseHandler,self).get_template_namespace()
        uimethods={
            "privilege_check": self.privilege_check
        }
        namespace.update(uimethods)
        return namespace


    def get_role(self,user):
	rolelist = TpyrcedSysRole.select(TpyrcedSysRole.role)
	d={}
	for i in rolelist:
	    userlist = TpyrcedUser.select().where(TpyrcedUser.role == i.role)
	    luser = []
	    for s in userlist:
	        luser.append(s.user)
	    d[i.role]=luser

		
	for r in d:
	    if user in  d[r]:
	         return r 

	return 'admin'


    def get_urllist(self,role):
	rolelist = TpyrcedSysRole.select(TpyrcedSysRole.role)
	rurl={}

        admin_path  = [   ('/iframe/','客户管理'),
                          ('/saleleft/','销售情况查询'),
                          ('/financeleft/','财务管理'),
                          ('/biddingleft/','竞价管理'),
                          ('/systemleft/','系统管理') ]
	filter_url = {
             'admin'  : admin_path,
	     'system' : [('/systemleft/','系统管理')],
	     'caiwu'  : [('/financeleft/','财务管理')],
	     'sale'  : [('/saleleft/','销售情况查询')],
	     'wenyuan' : [('/iframe/','客户管理'),('/employeeleft/','员工管理')]
	}

	return filter_url[role]
