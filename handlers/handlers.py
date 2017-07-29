# -*- coding: utf-8 -*- 
from views.views import *
from views.api import *
import os.path

STATIC_PATH   = os.path.join(os.path.dirname(__file__), "../static")
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "../templates")
HANDLERS =[(r"/" ,		Index_Handler),

	   (r"/api/wenyuan/add/", WenYuanAdd_handler ),
	]
