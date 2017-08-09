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
        $('.customerframeset01').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');
        $('.customerframeset02').children('div').eq(ind).css('display', 'block').siblings('div').css('display', 'none');

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

function openbidalter(){
  window.open ("/biddingleft/modify/,"竞价表-修改", "height=450, width=850, top=350, left=650, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
    }
}

function openfinalter(){
  window.open ("/caiwu/modify/,"财务表-修改", "height=450, width=850, top=350, left=650, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
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
