from peewee import *

database = MySQLDatabase('tpyrced', **{'host': 'localhost', 'password': 'zkeys', 'port': 3306, 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class TpyrcedBidadd(BaseModel):
    area_cons = CharField(null=True)
    area_main = CharField(null=True)
    bid_elec = CharField(null=True)
    save_time = BigIntegerField(null=True)

    class Meta:
        db_table = 'tpyrced_bidadd'

class TpyrcedClerk(BaseModel):
    client_name = CharField(null=True)
    client_tel = CharField(null=True, unique=True)
    invite = CharField(null=True)
    is_send = CharField(null=True)
    is_valid = CharField(null=True)
    key_words = CharField(null=True)
    remark_text = CharField(null=True)
    save_time = BigIntegerField(null=True)
    subscribe = CharField(null=True)
    tel_where = CharField(null=True)
    tl_area = CharField(null=True)

    class Meta:
        db_table = 'tpyrced_clerk'

class TpyrcedFinadd(BaseModel):
    act_amount = CharField(null=True)
    card_date = CharField(null=True)
    com_form = CharField(null=True)
    com_stand = CharField(null=True)
    cus_name = CharField(null=True)
    fav_able = CharField(null=True)
    inve_prop = CharField(null=True)
    ord_num = CharField(null=True)
    pro_name = CharField(null=True)
    prop_tion = CharField(null=True)
    save_time = BigIntegerField(null=True)
    sep_dire = CharField(null=True)
    source_tran = CharField(null=True)
    sub_date = CharField(null=True)
    team_name = CharField(null=True)
    tran_dire = CharField(null=True)
    tran_status = CharField(null=True)

    class Meta:
        db_table = 'tpyrced_finadd'

class TpyrcedFinanceQianyue(BaseModel):
    beizhu = CharField(null=True)
    bili = CharField(null=True)
    bili2 = CharField(null=True)
    chengjialaiyuan = CharField(null=True)
    chengjiaozhuangtai = CharField(null=True)
    chengjiaozhuren = CharField(null=True)
    fendanzhuren = CharField(null=True)
    id = IntegerField(null=True)
    jieyongbiaozhun = CharField(null=True)
    kehuxiangming = CharField(null=True)
    qianyue_riqi = CharField(null=True)
    rengou_riqi = CharField(null=True)
    shijifashenge = CharField(null=True)
    user = CharField(null=True)
    xiangmuminchen = CharField(null=True)
    youhui = CharField(null=True)

    class Meta:
        db_table = 'tpyrced_finance_qianyue'
        primary_key = False

class TpyrcedFinanceTicheng(BaseModel):
    chengjiaozhuangtai = CharField(null=True)
    fendanzhuren = CharField(null=True)
    huikuanjine = CharField(null=True)
    id = IntegerField(null=True)
    jingligongyong = CharField(null=True)
    kehuxingmin = CharField(null=True)
    qianyueriq = CharField(null=True)
    qianyueyuefen = CharField(null=True)
    rengogriqi = CharField(null=True)
    shijiticheng = CharField(null=True)
    taoshu = CharField(null=True)
    tuandui = CharField(null=True)
    xiaoshouticheng = CharField(null=True)
    xiaoshouzhuren = CharField(null=True)
    youhui = CharField(null=True)
    zhuguangongyong = CharField(null=True)
    zongjiangongyong = CharField(null=True)

    class Meta:
        db_table = 'tpyrced_finance_ticheng'
        primary_key = False

class TpyrcedSaleadd(BaseModel):
    re_area = CharField(null=True)
    re_group = CharField(null=True)
    re_peop = CharField(null=True)
    re_team = CharField(null=True)
    save_time = BigIntegerField(null=True)

    class Meta:
        db_table = 'tpyrced_saleadd'

class TpyrcedUser(BaseModel):
    password = CharField(null=True)
    save_time = BigIntegerField(null=True)
    user = CharField(null=True)

    class Meta:
        db_table = 'tpyrced_user'

class TpyrcedVie(BaseModel):
    area = CharField(null=True)
    area_cost = CharField(null=True)
    jingjia_number = CharField(null=True)

    class Meta:
        db_table = 'tpyrced_vie'

