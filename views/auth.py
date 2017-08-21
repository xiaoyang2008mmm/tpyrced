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
	try:
            name = self.get_argument("login_username").encode("utf-8")
	except:
            self.write({'status':'error','msg':'用户名错误!!!'})
	try:
             password = self.get_argument("login_password").encode("utf-8")
	except:
            self.write({'status':'error','msg':'密码错误!!!!'})
		
	try:
            get_user = TpyrcedUser.get(TpyrcedUser.user == name)
	    print name
	except:
            self.write({'status':'error','msg':'没有此用户!!!!'})
	    return

        if  get_user:
            get_pwd = (TpyrcedUser.get(TpyrcedUser.user == name)).password
	    lens = len(get_pwd)
	    lenx = lens - (lens % 4 if lens % 4 else 4)
    	    result = base64.decodestring(get_pwd[:lenx])

	    if  password == result:

        	url_index = (self.privilege_check(name)[0])[0]

        	self.set_cookie("anju_user", name)
        	self.write({'status':'ok','msg':url_index})
            else:
            	self.write({'status':'error','msg':'密码不对!!!!'})




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
	self.write("用户添加完成！！")





class Addrole_Handler(BaseHandler):
    """添加角色"""

    def post(self):
        role = self.get_argument("role").encode("utf-8")
	TpyrcedSysRole.create(role = role)
	self.write("角色添加完成！！")




class getuser_Handler(BaseHandler):
    """根据角色得到该角色下的所有用户和URl"""

    def post(self):
        role = self.get_argument("role").encode("utf-8")
	userlist = TpyrcedUser.select().where(TpyrcedUser.role == role)
	role_id = TpyrcedSysRole.get(TpyrcedSysRole.role == role)

	st4 = TpyrcedUrlRole.select().where(TpyrcedUrlRole.role == role_id.id)
	aa = TpyrcedUrl.select().where(TpyrcedUrl.id.in_([i.url for i in st4]))

	msg = [u.user for u in userlist]
	msg_role = [i.url for i in aa]

	self.write({'status':'ok','msg': msg ,'msg_role':msg_role})





class delroleuser_Handler(BaseHandler):
    """删除指定角色下的指定用户"""

    def post(self):
        role = self.get_argument("role_name").encode("utf-8")
        user = self.get_argument("user").encode("utf-8")
	TpyrcedUser.update(role='').where(TpyrcedUser.user == user).execute()
	self.write('删除完成！！')

class delroleurl_Handler(BaseHandler):
    """删除指定角色下的指定URL"""

    def post(self):
        role = self.get_argument("role_name").encode("utf-8")
        url = self.get_argument("url").encode("utf-8")
	url_id = TpyrcedUrl.get(TpyrcedUrl.url == url)
	role_id = TpyrcedSysRole.get(TpyrcedSysRole.role == role)
	st = TpyrcedUrlRole.get(role=url_id.id , url= role_id.id)
	st.delete_instance()





class addroleurl_Handler(BaseHandler):
    """增加URL到角色里"""

    def post(self):
        role = self.get_argument("role_name").encode("utf-8")
        url = self.get_argument("url").encode("utf-8")
	if len(url) >1:
	    url = url.split(",")

	role_id = TpyrcedSysRole.get(TpyrcedSysRole.role == role)

	for u in url:
	    url_id = TpyrcedUrl.get(TpyrcedUrl.url == u)
	    rid = role_id.id 
	    uid = url_id.id
	    TpyrcedUrlRole.insert(role = rid , url=uid).execute()
	self.write('添加完成！！！')

class addroleuser_Handler(BaseHandler):
    """增加用户到角色里"""

    def post(self):
        role = self.get_argument("role_name").encode("utf-8")
        user = self.get_argument("user").encode("utf-8")
	if len(user) >1:
	    user = user.split(",")

	for u in user:
	    TpyrcedUser.update(role=role).where(TpyrcedUser.user == u).execute()
	self.write('添加完成！！！')

