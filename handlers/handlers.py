# -*- coding: utf-8 -*- 
from views.views import *
from views.api import *
from views.worker import *
import os.path

STATIC_PATH   = os.path.join(os.path.dirname(__file__), "../static")
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "../templates")
HANDLERS =[(r"/" ,		Index_Handler),

	   ##信息录入接口
	   (r"/api/wenyuan/add/", 	WenYuanAdd_handler ),
	   (r"/api/jingjia/add/",	JingJiaAdd_handler ),
	   (r"/api/caiwu/add/", 	CaiWuAdd_handler ),


	   #请求返回页面
	   (r"/wenyuan/", 	wenyuan_handler ),
	   (r"/jingjia/", 	jingjia_handler ),
	   (r"/caiwu/", 	caiwu_handler ),

	]
