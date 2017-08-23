# -*- coding: utf-8 -*- 
from models.db  import *
import fenye
from models.db  import *
from base  import *
class Index_Handler(BaseHandler):

    def get(self,*args,**kwargs):
        current_user=self.get_current_user()
        self.render("base.html",current_user=current_user)



class Iframe_Handler(BaseHandler):

    def get(self,*args,**kwargs):                                              
	try:
	    index = int(self.request.arguments['index'][0])
	    page = int(self.request.arguments['page'][0])
	except:
	    index = 0
	    page = 1



	if index == 0 : 
	    req = self.request.arguments
	    print  req
	    data={}
	    if req.has_key('cname'):
		client_name = req['cname'][0]
		if client_name : data['client_name'] = client_name 

	    if req.has_key('ctel'):
		client_tel = req['ctel'][0]
		if client_tel : data['client_tel'] = client_tel 

	    if req.has_key('c_telfrom'):
		tel_where = req['c_telfrom'][0]
		if tel_where : data['tel_where'] = tel_where 

	    if req.has_key('c_tel_area'):
		tl_area = req['c_tel_area'][0]
		if tl_area : data['tl_area'] = tl_area

	    if data:
	        SHUJU  = TpyrcedClerk.select().filter(**data).order_by(TpyrcedClerk.id.desc())
		for i in SHUJU:
		    print i.client_name
	    else:
	        SHUJU  = TpyrcedClerk.select().order_by(TpyrcedClerk.id.desc())

	if index == 1 :
	    SHUJU  = TpyrcedSaleadd.select().order_by(TpyrcedSaleadd.id.desc())

        fen_ye = fenye.fen_ye_lei(page,SHUJU,10,11,5,'/iframe/?index=%s&page='%(str(index)))       #执行分页对象


        if fen_ye.dang_qian_ye > fen_ye.zong_ye_ma:             #判断分页对象里的当前页码如果大于总页码
            zfchdqy = str(fen_ye.zong_ye_ma)                    #将总页码转换成字符串
            self.redirect("/iframe/?index=%s"%str(index) + zfchdqy)                  #跳转到总页码
        else:
            self.render("iframe.html",dqy=fen_ye.dang_qian_ye,shuju=fen_ye.shu_ju_fan_wei(),yem=fen_ye.xian_shi_ye_ma(),index=index)







class test_handler(BaseHandler):

    def get(self,*args,**kwargs):
        self.render('test.html')

