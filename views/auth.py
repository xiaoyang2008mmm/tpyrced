# -*- coding: utf-8 -*- 
import tornado.web
from models.db  import *
from  base  import  *
import base64

class Login_Handler(BaseHandler):
    """登录验证"""
    def get(self):
        self.render('userlogin.html')
    def post(self):
        name = self.get_argument("login_username").encode("utf-8")
        password = self.get_argument("login_password").encode("utf-8")
        get_user = TpyrcedUser.get(TpyrcedUser.user == name)

        if  get_user:
            get_pwd = TpyrcedUser.select(TpyrcedUser.password).where(TpyrcedUser.user == name)

	    if password == get_pwd or password == base64.decodestring(get_pwd):

        	url_index = (self.privilege_check(name)[0])[0]

        	self.set_cookie("anju_user", name)
        	self.write(url_index)
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


class Adduser_Handler(BaseHandler):
    """添加用户"""
    def post(self):
        name = self.get_argument("user").encode("utf-8")
        password = self.get_argument("pwd").encode("utf-8")
        role = self.get_argument("role").encode("utf-8")
	base_passwd = base64.encodestring(password)

	TpyrcedUser.create(user=name , password=base_passwd ,role = role)
	print  name,base_passwd,role
	self.write("用户添加完成！！")





class Addrole_Handler(BaseHandler):
    """添加角色"""

    def post(self):
        role = self.get_argument("role").encode("utf-8")
	TpyrcedSysRole.create(role = role)
	self.write("角色添加完成！！")




class getuser_Handler(BaseHandler):
    """根据角色得到该角色下的所有用户"""

    def post(self):
        role = self.get_argument("role").encode("utf-8")
	userlist = TpyrcedUser.select().where(TpyrcedUser.role == role)
	msg = []
	for u in userlist:
	    msg.append(u.user)
	self.write({'status':'ok','msg': msg})
