// 主页导航js   start
$(function() {

    $('.nav ul li').click(function()

    {

        var ind = $(this).index();

        $(this).css('background', '#a6c5e1').siblings('li').css('background', '#fff');
        $(this).children('a').css('color', '#fff');
        $(this).siblings('li').children('a').css('color', '#000');
        $('.frameset').children('div').eq(ind).css('display', 'inline-block').siblings('div').css('display', 'none');
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
// 弹出窗口  end
//

// 删除文员录入数据
//
function delete_data() {

	var client_telphone = '123456789' ;

        var msg = "确定要删除吗?";
        if (confirm(msg) == true) {
            $.post("/api/wenyuan/delete/", {
                client_telphone: client_telphone,
            },
            function(data) {
                alert(data);
            });
            location.href = '/iframe/';
        } else {
            return false;
        }

}






