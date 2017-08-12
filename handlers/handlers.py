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
	   (r"/iframe/(?P<page>\d*)" ,          Iframe_Handler),
	   ##信息录入接口
	   (r"/api/wenyuan/add/", 	WenYuanAdd_handler ),
	   (r"/api/wenyuan/delete/", 	WenYuandelete_handler ),
	   (r"/api/caiwu/delete/", 	Caiwudelete_handler ),
	   (r"/api/jingjia/add/",	JingJiaAdd_handler ),
	   (r"/api/caiwuqianyue/add/", 	CaiWuAdd_handler ),
	   (r"/api/caiwuticheng/add/", 	CaiWuAdd_handler ),


	   #请求返回页面
	   (r"/wenyuan/", 	wenyuan_handler ),
	   (r"/customer_alter/(.*)", customer_alter_handler ),
	   (r"/jingjia/", 	jingjia_handler ),
	   (r"/caiwu/", 	caiwu_handler ),
	   (r"/caiwu/add/", 	caiwu_add_handler ),
	   (r"/caiwu/modify/", 	caiwu_modify_handler ),
	   (r"/wenyuan/modify/",wenyuan_modify_handler ),
	   #文员
 


	   (r"/test/", 		test_handler ),
		
	    ###用户登录
           (r"/login/",                 Login_Handler),
           (r"/logout/",                Logout_Handler),


       (r"/customerleft/(?P<page>\d*)",		customerleft_handler),
       (r"/employeeleft/",	employeeleft_handler),
       (r"/saleleft/",		saleleft_handler),
       (r"/sale/add/",		saleadd_handler),
       (r"/sale/modify/",		salemodify_handler),
       (r"/financeleft/(?P<page>\d*)",		financeleft_handler),
       (r"/biddingleft/(?P<page>\d*)",		biddingleft_handler),
       (r"/biddingleft/add/",		biddingleft_add_handler),
       (r"/biddingleft/modify/",	biddingleft_modify_handler),
       (r"/systemleft/"  ,	systemleft_handler),


	]
