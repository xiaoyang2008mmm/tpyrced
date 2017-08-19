// 主页导航js   start

$(function() {

    $('.nav ul li').click(function()

    {

        var ind = $(this).index();

        $(this).css('background', '#a6c5e1').siblings('li').css('background', '#fff');
        $(this).children('a').css('color', '#fff');
        $(this).siblings('li').children('a').css('color', '#000');
        // $('.frameset').children('div').eq(ind).css('display', 'inline-block').siblings('div').css('display', 'none');
        // $ ('.frameset02').children('div').eq(ind).css('display', 'inline-block').siblings('div').css('display','none');
    });

    $('#customerleft li').click(function()

    {

        var ind = $(this).index();
	if ( ind == 0){
		location.href = '/iframe/?index=0&page=1';
 	}	
	if ( ind == 1){
		location.href = '/iframe/?index=1&page=1';
 	}	

    });
    $('#employeeleft li').click(function()

    {

        var ind = $(this).index();
        $('.employeeframeset01').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');
        $('.employeeframeset02').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');

    });
    $('#saleleft li').click(function()

    {

        var ind = $(this).index();
        $('.saleframeset01').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');
        $('.saleframeset02').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');

    });
    $('#systemleft li').click(function()

    {

        var ind = $(this).index();
        $('.systemframeset01').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');
        $('.systemframeset02').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');

    });
    $('#biddingleft li').click(function()

    {

        var ind = $(this).index();
        $('.biddingframeset01').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');
        $('.biddingframeset02').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');

    });
    $('#financeleft li').click(function()

    {

        var ind = $(this).index();
        $('.financeframeset01').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');
        $('.financeframeset02').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');

    });

});
// 主页导航js  end

// 左侧框架js  start
$(function() {

    $('#employeeleft li a').click(function()

    {

        $(this).css('color', '#00144c').siblings('a').css('color', '#fff');

    });

});

$(function() {

    $('#customerleft li a').click(function()

    {

        $(this).css('color', '#00144c').siblings('a').css('color', '#fff');

    });

});

$(function() {

    $('#saleleft li a').click(function()

    {

        $(this).css('color', '#00144c').siblings('a').css('color', '#fff');

    });

});

$(function() {
    $('#systemleft li a').click(function()
    {
        $(this).css('color', '#00144c').siblings('a').css('color', '#fff');
    });
});

$(function() {
    $('#biddingleft li a').click(function()
    {
        $(this).css('color', '#00144c').siblings('a').css('color', '#fff');
    });
});

$(function() {
    $('#financeleft li a').click(function()
    {
        $(this).css('color', '#00144c').siblings('a').css('color', '#fff');
    });
});
// 左侧框架js  end

// 弹出窗口  start
function openwin() {
    window.open("/wenyuan/", "客户资料", "height=700, width=850, top=200, left=650, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
}

function openbid() {
    window.open("/biddingleft/add/", "竞价表", "height=450, width=850, top=350, left=650, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
}

function openfin() {
    window.open("/caiwu/add/", "财务表", "height=700, width=850, top=200, left=650, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
}
function opensale() {
    window.open("/sale/add/", "销售资料", "height=700, width=850, top=200, left=650, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
}

//文员修改录入数据
//
//
function  get_cli_id(){
    var $chkBoxes = $('#tab_form').find('input:checked');   
    if ($chkBoxes.length == 0) {         
      alert('请至少选择一个数据集');
      return false;
    }
 var ids_id=  $($chkBoxes).attr('data-id') ;  
 return ids_id;
}


function openalter(){
	var id_data = get_cli_id()
  if (id_data){
  window.open ("/customer_alter/?client_id=" + id_data,"客户资料-修改", "height=700, width=850, top=200, left=650, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
    }
}

//竞价修改录入数据
//
//
function  get_bli_id(){
    var $chkBoxes = $('#tab_bid_form').find('input:checked');
    if ($chkBoxes.length == 0) {
      alert('请至少选择一个数据集');
      return false;
    }
 var ids_id=  $($chkBoxes).attr('data-id') ;
 return ids_id;
}

function openbidalter(){
   var id_data = get_bli_id()
   if (id_data){
   window.open ("/biddingleft/modify/?b_id=" + id_data,"客户资料-修改", "height=700, width=850, top=200, left=650, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
    }
}

//财务修改录入数据
//
//
function  get_fin_id(){
    var $chkBoxes = $('#tab_ff_form').find('input:checked');
    if ($chkBoxes.length == 0) {
      alert('请至少选择一个数据集');
      return false;
    }
 var ids_id=  $($chkBoxes).attr('data-id') ;
 return ids_id;
}

function openfinalter(){
    var id_data = get_fin_id()
    if (id_data){
       window.open ("/caiwu/xiugai/?f_id=" + id_data,"财务表-修改", "height=450, width=850, top=350, left=650, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
    }
}


//销售修改录入数据
//
//
function  get_sale_id(){
    var $chkBoxes = $('#tab_sl_form').find('input:checked');
    if ($chkBoxes.length == 0) {
      alert('请至少选择一个数据集');
      return false;
    }
    var ids_id=  $($chkBoxes).attr('data-id') ;
    return ids_id;
}

function opensalealter(){
    var id_data = get_sale_id()
    if (id_data){
       window.open ("/sale/modify/?s_id=" + id_data,"销售表-修改", "height=450, width=850, top=350, left=650, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
    }
}

function export_excel(){
$('#tab_form').tableExport({ type: 'excel', separator: ';', escape: 'false' });
}

// 弹出窗口  end
//

// 删除文员录入数据
//
//

function  get_id(){
var $ids = [];   
    var $chkBoxes = $('#tab_form').find('input:checked');   
    if ($chkBoxes.length == 0) {         
      alert('请至少选择一个数据集');
      return false;
    }

  $($chkBoxes).each(function () { 
      	$ids.push( $(this).attr('data-id') );  
    });

var $ids_str = $ids.join(',');    
        return $ids_str;
}

function delete_data() {
	var id_data = get_id()
	if (id_data){
        var msg = "确定要删除吗?";
        if (confirm(msg) == true) {
            $.post("/api/wenyuan/delete/", {
                client_telphone: id_data,
            },
            function(data) {
                alert(data);
            });
            location.href = '/iframe/';
        } else {
            return false;
        }
        }

}

////财务数据删除
//
function  get_f_id(){
var $ids = [];
    var $chkBoxes = $('#tab_ff_form').find('input:checked');
    if ($chkBoxes.length == 0) {
      alert('请至少选择一个数据集');
      return false;
    }

  $($chkBoxes).each(function () {
        $ids.push( $(this).attr('data-id') );
    });

var $ids_str = $ids.join(',');
        return $ids_str;
}


function d_finance_data() {
        var id_data = get_f_id()
        if (id_data){
        var msg = "确定要删除吗?";
        if (confirm(msg) == true) {
            $.post("/api/caiwu/delete/", {
                pro_name: id_data,
            },
            function(data) {
                alert(data);
            });
            location.href = '/financeleft/';
        } else {
            return false;
        }
        }

}
////竞价数据删除
//
function  get_bid(){
var $ids = [];
    var $chkBoxes = $('#tab_bid_form').find('input:checked');
    if ($chkBoxes.length == 0) {
      alert('请至少选择一个数据集');
      return false;
    }

  $($chkBoxes).each(function () {
        $ids.push( $(this).attr('data-id') );
    });

var $ids_str = $ids.join(',');
        return $ids_str;
}


function delbid_data() {
        var id_data = get_bid()
        if (id_data){
        var msg = "确定要删除吗?";
        if (confirm(msg) == true) {
            $.post("/api/biddingleft/delete/", {
                pro_name: id_data,
            },
            function(data) {
                alert(data);
            });
            location.href = '/biddingleft/';
        } else {
            return false;
        }
        }

}



////销售数据删除
//
function  get_s_bid(){
var $ids = [];
    var $chkBoxes = $('#tab_sl_form').find('input:checked');
    if ($chkBoxes.length == 0) {
      alert('请至少选择一个数据集');
      return false;
    }

  $($chkBoxes).each(function () {
        $ids.push( $(this).attr('data-id') );
    });

var $ids_str = $ids.join(',');
        return $ids_str;
}


function delsale_data() {
        var id_data = get_s_bid()
        if (id_data){
        var msg = "确定要删除吗?";
        if (confirm(msg) == true) {
            $.post("/api/sale/delete/", {
                pro_name: id_data,
            },
            function(data) {
                alert(data);
            });
            location.href = '/iframe/?index=1';
        } else {
            return false;
        }
        }

}
