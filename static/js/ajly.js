$(document).ready(function() {

    $("#wenyuan_save").click(function() {
        /////文员添加
        var save_time = (Date.parse(new Date())) / 1000;
        var client_tel = $('#client_tel').val();
        var client_name = $('#c_name').val();;
        var is_send = $('#is_send').val();
        var is_valid = $('#is_valid').val();
        var key_words = $('#key_words').val();
        var tel_where = $('#tel_where option:selected').val();
        var tl_area = $('#tl_area option:selected').val();
        var invite = $('#invite').val();
        var subscribe = $('#subscribe').val();
        var remark_text = $('#remark_text').val();

        var wenyuan_obj = {};

        wenyuan_obj.save_time = save_time;
        wenyuan_obj.client_tel = client_tel;
        wenyuan_obj.client_name = client_name;
        wenyuan_obj.is_send = is_send;
        wenyuan_obj.is_valid = is_valid;
        wenyuan_obj.key_words = key_words;
        wenyuan_obj.tel_where = tel_where;
        wenyuan_obj.tl_area = tl_area;
        wenyuan_obj.invite = invite;
        wenyuan_obj.subscribe = subscribe;
        wenyuan_obj.remark_text = remark_text;
	
	var error_msg = "客户电话  和 发给销售人员   两项为必填项目!!!"  ;	
	(client_tel == "" && is_send == "") ? alert(error_msg) : (
        $.post("/api/wenyuan/add/", wenyuan_obj,
        function(data) {
            alert(data);

        })
	)
        });


    ////竞价添加
    var area = 'area';
    var area_cost = 'area_cost';
    var jingjia_number = 'jingjia_number';

    var jingjia_obj = {};
    jingjia_obj.area = area;
    jingjia_obj.area_cost = area_cost;
    jingjia_obj.jingjia_number = jingjia_number;

    $.post("/api/jingjia/add/", jingjia_obj,
    function(data) {
        alert(data);

    })

    /////财务预约数据添加
    var user = 'user';
    var rengou_riqi = 'rengou_riqi';
    var qianyue_riqi = 'qianyue_riqi';
    var kehuxiangming = 'kehuxiangming';
    var xiangmuminchen = 'xiangmuminchen';
    var chengjiaozhuangtai = 'chengjiaozhuangtai';
    var jieyongbiaozhun = 'jieyongbiaozhun';
    var youhui = 'youhui';
    var shijifashenge = 'shijifashenge';
    var chengjiaozhuren = 'chengjiaozhuren';
    var bili = 'bili';
    var fendanzhuren = 'fendanzhuren';
    var bili2 = 'bili2';
    var chengjialaiyuan = 'chengjialaiyuan';
    var beizhu = beizhu;

    var caiwuqy_obj = {};

    caiwuqy_obj.user = user;
    caiwuqy_obj.rengou_riqi = rengou_riqi;
    caiwuqy_obj.qianyue_riqi = qianyue_riqi;
    caiwuqy_obj.kehuxiangming = kehuxiangming;
    caiwuqy_obj.xiangmuminchen = xiangmuminchen;
    caiwuqy_obj.chengjiaozhuangtai = chengjiaozhuangtai;
    caiwuqy_obj.jieyongbiaozhun = jieyongbiaozhun;
    caiwuqy_obj.youhui = youhui;
    caiwuqy_obj.shijifashenge = shijifashenge;
    caiwuqy_obj.chengjiaozhuren = chengjiaozhuren;
    caiwuqy_obj.bili = bili;
    caiwuqy_obj.fendanzhuren = fendanzhuren;
    caiwuqy_obj.bili2 = bili2;
    caiwuqy_obj.chengjialaiyuan = chengjialaiyuan;
    caiwuqy_obj.beizhu = beizhu;

    $.post("/api/caiwuqianyue/add/", caiwuqy_obj,
    function(data) {
        alert(data);

    })
    /////财务提成数据添加
    var tuandui = 'tuandui';
    var qianyueyuefen = 'qianyueyuefen';
    var kehuxingmin = 'kehuxingmin';
    var chengjiaozhuangtai = 'chengjiaozhuangtai';
    var rengogriqi = 'rengogriqi';
    var qianyueriq = 'qianyueriq';
    var xiaoshouzhuren = 'xiaoshouzhuren';
    var fendanzhuren = 'fendanzhuren';
    var huikuanjine = 'huikuanjine';
    var youhui = 'youhui';
    var shijiticheng = 'shijiticheng';
    var xiaoshouticheng = 'xiaoshouticheng';
    var taoshu = 'taoshu';
    var zhuguangongyong = 'zhuguangongyong';
    var jingligongyong = 'jingligongyong';
    var zongjiangongyong = 'zongjiangongyong';

    var caiwutc_obj = {};

    caiwutc_obj.tuandui = tuandui;
    caiwutc_obj.qianyueyuefen = qianyueyuefen;
    caiwutc_obj.kehuxingmin = kehuxingmin;
    caiwutc_obj.chengjiaozhuangtai = chengjiaozhuangtai;
    caiwutc_obj.rengogriqi = rengogriqi;
    caiwutc_obj.qianyueriq = qianyueriq;
    caiwutc_obj.xiaoshouzhuren = xiaoshouzhuren;
    caiwutc_obj.fendanzhuren = fendanzhuren;
    caiwutc_obj.huikuanjine = huikuanjine;
    caiwutc_obj.youhui = youhui;
    caiwutc_obj.shijiticheng = shijiticheng;
    caiwutc_obj.xiaoshouticheng = xiaoshouticheng;
    caiwutc_obj.taoshu = taoshu;
    caiwutc_obj.zhuguangongyong = zhuguangongyong;
    caiwutc_obj.jingligongyong = jingligongyong;
    caiwutc_obj.zongjiangongyong = zongjiangongyong;

    $.post("/api/caiwuticheng/add/", caiwutc_obj,
    function(data) {
        alert(data);

    })

})
