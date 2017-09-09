#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
from  base  import *
from models.db  import *
import fenye
import MySQLdb


"""财务数据添加"""
class caiwu_add_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("finance_a.html")
    def post(self, *args, **kwargs):
        request_dict = self.request.arguments

	save_time  = request_dict['save_time'][0]
        team_name  = request_dict['team_name'][0]
        ord_num  =request_dict['ord_num'][0]
        card_date = request_dict['card_date'][0]
        sub_date = request_dict['sub_date'][0]
        cus_name = request_dict['cus_name'][0]
        pro_name = request_dict['pro_name'][0]
        tran_status = request_dict['tran_status'][0]
        com_stand = request_dict['com_stand'][0]
        fav_able = request_dict['fav_able'][0]
        act_amount = request_dict['act_amount'][0]
        tran_dire = request_dict['tran_dire'][0]
        prop_tion = request_dict['prop_tion'][0]
        sep_dire = request_dict['sep_dire'][0]
        inve_prop = request_dict['inve_prop'][0]
        source_tran = request_dict['source_tran'][0]
        com_form = request_dict['com_form'][0]

	try:
	    q =TpyrcedFinadd.insert(save_time= save_time ,team_name = team_name,ord_num = ord_num,card_date = card_date,sub_date = sub_date,cus_name = cus_name,pro_name = pro_name,tran_status = tran_status,com_stand = com_stand,fav_able = fav_able,act_amount = act_amount,  tran_dire = tran_dire , prop_tion=prop_tion, sep_dire=sep_dire, inve_prop=inve_prop,source_tran=source_tran, com_form=com_form )
	    q.execute()
	    self.write("数据写入成功!!")
	except:
	    self.write("数据写入失败,请联系管理员!!")








class biddingleft_add_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("bidding_a.html")
    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
       
        save_time  =request_dict['save_time'][0]
        area_main  = request_dict['area_main'][0]
        area_cons  = request_dict['area_cons'][0]
        bid_elec  =request_dict['bid_elec'][0]

      	q =TpyrcedBidadd.insert(save_time= save_time ,area_main = area_main,area_cons = area_cons,bid_elec = bid_elec )
        q.execute()
        self.write("数据写入成功!!")


class biddingleft_modify_handler(BaseHandler):

    def get(self, *args, **kwargs):
        b_id = int(self.request.arguments['b_id'][0])
        #st2 = TpyrcedBidadd.get(TpyrcedBidadd.id == b_id)
        #__dict = {"st2":st2}
        self.render("bidding_alter.html")
    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        db_key  = request_dict['db_key'][0]
        db_id  = int(request_dict['db_id'][0])
        bid_val = request_dict['bid_val'][0]

        dd ={db_key:bid_val}
        try:
            TpyrcedBidadd.update(**dd).where(TpyrcedBidadd.id == db_id).execute()
            self.write("数据录入成功!!!!!!")
        except:
            self.write("数据写入失败,请联系管理员!!!!!")

class sale_add_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("sale_a.html")
    def post(self, *args, **kwargs):
        request_dict = self.request.arguments

        save_time  =request_dict['save_time'][0]
        re_area  = request_dict['re_area'][0]
        re_team  = request_dict['re_team'][0]
        re_group  =request_dict['re_group'][0]
        re_peop  =request_dict['re_peop'][0]

        q =TpyrcedSaleadd.insert(save_time= save_time ,re_area = re_area,re_team = re_team,re_group = re_group,re_peop = re_peop )
        q.execute()
        t =TpyrcedArea.insert(save_time= save_time ,re_area = re_area,re_team = re_team )
        t.execute()
        self.write("数据写入成功!!")

class caiwu_modify_handler(BaseHandler):

    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        db_key  = request_dict['db_key'][0]
        db_id  = int(request_dict['db_id'][0])
        fin_val = request_dict['fin_val'][0]

        dd ={db_key:fin_val}
        try:
            TpyrcedClerk.update(**dd).where(TpyrcedClerk.id == db_id).execute()
            self.write("数据录入成功!!!!!!")
        except:
            self.write("数据写入失败,请联系管理员!!!!!")


class sale_modify_handler(BaseHandler):
        
    def get(self, *args, **kwargs):
        self.render("sale_alter.html")
    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        db_key  = request_dict['db_key'][0] 
        db_id  = int(request_dict['db_id'][0])
        sale_val = request_dict['sale_val'][0]

        dd ={db_key:sale_val} 
        try:
            TpyrcedSaleadd.update(**dd).where(TpyrcedSaleadd.id == db_id).execute()
            self.write("数据录入成功!!!!!!")
        except:
            self.write("数据写入失败,请联系管理员!!!!!")
class SaleAdd_handler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("sale_a.html")
    def post(self, *args, **kwargs):
	request_dict = self.request.arguments
      
class ApiGetSaleData_handler(BaseHandler):

    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        db_key  = request_dict['db_key'][0] 
        db_id  = int(request_dict['db_id'][0])
	st2 = TpyrcedSaleadd.get(TpyrcedSaleadd.id == db_id )
	ss=(st2.__dict__)['_data']
	self.write(ss[db_key])

class ApiGetCustomerData_handler(BaseHandler):

    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        db_key  = request_dict['db_key'][0]
        db_id  = int(request_dict['db_id'][0])
        st2 = TpyrcedClerk.get(TpyrcedClerk.id == db_id )
        ss=(st2.__dict__)['_data']
        self.write(ss[db_key])

class ApiGetCaiwuData_handler(BaseHandler):

    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        db_key  = request_dict['db_key'][0]
        db_id  = int(request_dict['db_id'][0])
        st2 = TpyrcedFinadd.get(TpyrcedFinadd.id == db_id )
        ss=(st2.__dict__)['_data']
        self.write(ss[db_key])

class ApiGetBiddingData_handler(BaseHandler):

    def post(self, *args, **kwargs):
        request_dict = self.request.arguments
        db_key  = request_dict['db_key'][0]
        db_id  = int(request_dict['db_id'][0])
        st2 = TpyrcedBidadd.get(TpyrcedBidadd.id == db_id )
        ss=(st2.__dict__)['_data']
        self.write(ss[db_key])

class Salequery_handler(BaseHandler):

    def post(self, *args, **kwargs):
        request_dict = eval(self.request.body)
        '''查询全部'''
	if not (request_dict['sale_peop'] or request_dict['sale_area'] or  request_dict['sale_team'] or request_dict['sale_group']):
            ret = []
            all_area = self.get_teamarea()
            data = TpyrcedSaleadd.select(TpyrcedSaleadd.re_team, TpyrcedSaleadd.re_group)
            l1 = [i.re_team for i in data]
            team_list = sorted(set(l1),key=l1.index)

            l3 = [i.re_group for i in data]
            group_list = sorted(set(l3),key=l3.index)
            for area in all_area:
                for team in team_list:
                    for group in group_list:
                        s = [area, team, group]
			ret.append(s)
	
            ###消费
            area_group = {}    
            for area in all_area:
                area_telnum = TpyrcedClerk.select(TpyrcedClerk.client_tel).where(TpyrcedClerk.tl_area == area).count()
                area_count = TpyrcedBidadd.select(TpyrcedBidadd.area_cons).where(TpyrcedBidadd.area_main == area)
		s = [i.area_cons for i in area_count] 
	  	try:
		    d = ((s[0]).encode("utf8"))
                    area_xiaofei = float(d)
                    area_avrg=area_xiaofei / area_telnum
                    area_group[area] = area_avrg
		except:
		    #print "没有区域成本"
		    pass


            team_group = {}
	    sale_list = {}
	    invite_count_group = {}
            subscribe_count_group = {}
            for group in group_list:
                gg = TpyrcedSaleadd.select(TpyrcedSaleadd.re_peop).where(TpyrcedSaleadd.re_group == group).count()
		sale_list[group] = gg
		
                group_peop = TpyrcedSaleadd.select(TpyrcedSaleadd.re_peop).where(TpyrcedSaleadd.re_group == group)
                tel_count = 0
                ini_count = 0
		invite_count = 0
                subscribe_count = 0 
                for p in group_peop:
                    peop_telnum = TpyrcedClerk.select(TpyrcedClerk.client_tel).where(TpyrcedClerk.is_send == p.re_peop).count()              
            
                    p_invite = TpyrcedClerk.select(TpyrcedClerk.invite).where(TpyrcedClerk.is_send == p.re_peop)
                    
                    peop_invite = []
                    for i in p_invite:
                        try:
                            peop_invite.append(int((i.invite).encode("utf8")))
                        except:
                            pass

                    if any(peop_invite):                      
                        print peop_invite
                        peop_invite = sum(peop_invite)

                    else:
                        peop_invite = 0                   
                    p_subscribe = TpyrcedClerk.select(TpyrcedClerk.subscribe).where(TpyrcedClerk.is_send == p.re_peop)                         
                    
                    peop_subscribe = []
                    for i in p_subscribe:
                        try:
                            peop_subscribe.append(int((i.subscribe).encode("utf8")))
                        except:
                            pass

                    if any(peop_subscribe):
                        print peop_subscribe
                        peop_subscribe = sum(peop_subscribe)

                    else:
                        peop_subscribe = 0

                    invite_count += peop_invite
                    subscribe_count += peop_subscribe
                    tel_count += peop_telnum 

                team_group[group] = tel_count
		invite_count_group[group] = invite_count 
                subscribe_count_group[group] = subscribe_count
            
            for r in ret:
                s = r
                a, g = s[0], s[2]
		try:
                    group_count = team_group[g] * area_group[a]
                    if team_group[g] == 0:
                        invite_rate = 0
                        subscribe_rate = 0
                    else:
                        invite_rate = ('%.2f%%' % (invite_count_group[g] * 100 / (team_group[g])))
                        subscribe_rate = ('%.2f%%' % (subscribe_count_group[g] * 100 / (team_group[g])))
		    index = ret.index(r)
		    r.append(group_count)
		    r.append(team_group[g])
		    r.append(area_group[a])
		    r.append(sale_list[g])
		    r.append(invite_count_group[g])
                    r.append(subscribe_count_group[g])
                    r.append(invite_rate)
                    r.append(subscribe_rate)
		    ret[index] = r
		    
		except:
		    #print "竞价没有数据"
		    r.append('消费列没有数据!!!')
		    r.append(group_count)
		    r.append("套电成本数据不全!!")
		    r.append(sale_list[g])
		    r.append("没有约访!")
                    r.append("没有认购!")
                    r.append('约访率为0!')
                    r.append('认购率为0!')
		    ret[index] = r

	
	    msg = {'status':'ok','data':ret}	
	    self.write(msg)
             

        def get(self,page):               
	    req = self.request.arguments   
            data={}
            if req.has_key('group_count'):
                group_count = req['group_count'][0]
                if group_count : data['group_count'] = group_count
            if req.has_key('team_group[g]'):
                team_group[g] = req['team_group[g]'][0]
                if team_group[g] : data['team_group[g]'] = team_group[g]
            if req.has_key('area_group[a]'):
                area_group[a] = req['area_group[a]'][0]
                if area_group[a] : data['area_group[a]'] = area_group[a]
            if req.has_key('sale_list[g]'):
                sale_list[g] = req['sale_list[g]'][0]
                if sale_list[g] : data['sale_list[g]'] = sale_list[g]
            if req.has_key('invite_count_group[g]'):
                invite_count_group[g] = req['invite_count_group[g]'][0]
                if invite_count_group[g] : data['invite_count_group[g]'] = invite_count_group[g]
            if req.has_key('subscribe_count_group[g]'):
                subscribe_count_group[g] = req['subscribe_count_group[g]'][0]
                if subscribe_count_group[g] : data['subscribe_count_group[g]'] = subscribe_count_group[g]
            if req.has_key('invite_rate'):
                invite_rate = req['invite_rate'][0]
                if invite_rate : data['invite_rate'] = invite_rate
            if req.has_key('subscribe_rate'):
                subscribe_rate = req['subscribe_rate'][0]
                if subscribe_rate : data['subscribe_rate'] = subscribe_rate

            if data:
                SHUJU  = TpyrcedSaleadd.select().filter(**data).order_by(TpyrcedSaleadd.id.desc())
                for i in SHUJU:
                     i.re_area
            else:
                SHUJU  = TpyrcedSaleadd.select().order_by(TpyrcedSaleadd.id.desc())

            fen_ye = fenye.fen_ye_lei(page,SHUJU,10,11,5,'/saleleft/')       #执行分页对象


            if fen_ye.dang_qian_ye > fen_ye.zong_ye_ma:             #判断分页对象里的当前页码如果大于总页码
                zfchdqy = str(fen_ye.zong_ye_ma)                    #将总页码转换成字符串
                self.redirect("/saleleft/" + zfchdqy)                  #跳转到总页码
            else:
                self.render("saleleft.html",dqy=fen_ye.dang_qian_ye,shuju=fen_ye.shu_ju_fan_wei(),yem=fen_ye.xian_shi_ye_ma())



        '''
        sale_date  = request_dict['sale_date'][0]
        sale_peop  = request_dict['sale_peop'][0]
        sale_area = request_dict['sale_area'][0]
        sale_team = request_dict['sale_team'][0]
        sale_group = request_dict['sale_group'][0]

        try:
            q =TpyrcedSaleadd.select(sale_date = sale_date,sale_peop = sale_peop,sale_area = sale_area,sale_team = sale_team,sale_group= sale_group)
            q.execute()
            self.write("数据查询成功!!")
        except:

            self.write("请联系管理员!!!")
        '''
 
