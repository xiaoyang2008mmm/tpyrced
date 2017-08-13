# -*- coding: utf-8 -*- 
import tornado.web
from models.db  import *
from  base  import  *

class Login_Handler(BaseHandler):
    """登录验证"""
    def get(self):
        self.render('userlogin.html')
    def post(self):
        name = self.get_argument("login_username").encode("utf-8")
        password = self.get_argument("login_password").encode("utf-8")
	try:
	    get_user = TpyrcedUser.get(TpyrcedUser.user == name)
	    if  get_user:
	    	get_pwd = TpyrcedUser.get(TpyrcedUser.password == password)
	        if get_pwd:
		    url_index = (self.privilege_check(name)[0])[0]
		    self.set_cookie("anju_user", name)
		    self.write(url_index)
	        else:
	            self.write("密码不对!!!")
	    else:
	        self.write("用户名不对!!!")
	except:
	    self.write("没有此用户!!!")
	

class Logout_Handler(BaseHandler):
    """退出"""
    def get(self):
        self.set_cookie("anju_user","")
        self.clear_cookie("anju_user")
	self.clear_all_cookies()
        self.redirect('/login/', permanent=True)


