# -*- coding: utf-8 -*- 
from views.views import *
from views.api import *
from views.worker import *
from views.auth import *
from views.add import *
import os.path

STATIC_PATH   = os.path.join(os.path.dirname(__file__), "../static")
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "../templates")
HANDLERS =[(r"/" ,				Index_Handler),

	######文员Url路由

	   (r"/api/wenyuan/add/", 	WenYuanAdd_handler ),
	   (r"/api/wenyuan/delete/", 	WenYuandelete_handler ),
	   (r"/iframe/(?P<page>\d*)" ,          Iframe_Handler),
	   (r"/wenyuan/", 		wenyuan_handler ),
	   (r"/wenyuan/modify/",	wenyuan_modify_handler ),
	   (r"/customer_alter/(.*)", 	customer_alter_handler ),
	######财务URL路由
	   (r"/caiwu/", 			caiwu_handler ),
	   (r"/caiwu/add/", 	caiwu_add_handler ),
	   (r"/caiwu/xiugai/(.*)", 	caiwu_xiugai_handler ),
	   (r"/api/caiwu/delete/", 	Caiwudelete_handler ),
	   (r"/api/caiwuqianyue/add/", 	CaiWuAdd_handler ),
	   (r"/api/caiwuticheng/add/", 	CaiWuAdd_handler ),
           (r"/financeleft/(?P<page>\d*)",		financeleft_handler),
	######竞价URL路由

	   (r"/api/biddingleft/delete/", 	biddingleftdelete_handler ),
	   (r"/api/jingjia/add/",	JingJiaAdd_handler ),
	   (r"/jingjia/", 	jingjia_handler ),
           (r"/biddingleft/(?P<page>\d*)",		biddingleft_handler),
           (r"/biddingleft/add/",		biddingleft_add_handler),
           (r"/biddingleft/modify/",	biddingleft_modify_handler),


	######临时测试路由
	   (r"/test/", 		test_handler ),
		
	###用户认证登录
           (r"/login/",                 Login_Handler),
           (r"/logout/",                Logout_Handler),
           (r"/adduser/",               Adduser_Handler),
           (r"/addrole/",               Addrole_Handler),
           (r"/role/get_user/",         getuser_Handler),

	######用工管理路由

       (r"/employeeleft/",	employeeleft_handler),
	######销售路由
       (r"/saleleft/",		saleleft_handler),
       (r"/sale/add/",		sale_add_handler),
       (r"/sale/modify/",		sale_modify_handler),
       (r"/api/sale/add/",       SaleAdd_handler ),
       (r"/api/sale/delete/",        saledelete_handler ),
	#######系统设置路由
       (r"/systemleft/"  ,	systemleft_handler),


	]
