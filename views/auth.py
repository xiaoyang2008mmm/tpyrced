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
	if  name =="admin":
	    if password == "admin":
		self.set_cookie("anju_user", name)
		self.write("ok")
	    else:
	        self.write("密码不对!!!")
	else:
	    self.write("用户名不对!!!")

class Logout_Handler(BaseHandler):
    """退出"""
    def get(self):
        self.set_cookie("anju_user","")
        self.clear_cookie("anju_user")
	self.clear_all_cookies()
        self.redirect('/login/', permanent=True)


