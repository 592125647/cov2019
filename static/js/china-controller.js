// 更新中国疫情地图
function get_china_left() {
    $.ajax({
        url:'/get_china_left',
        success:function(data){
           ec_center_option.series[0].data = data.data
		   ec_center.setOption(ec_center_option)
        },
        error:function f() {

        }
    })
}

// 更新中国累计数据
function get_china_top_right() {
    $.ajax({
        url:'/get_china_top_right',
        success:function(data){
            $('.num h1').eq(0).text(data.confirm)
            $('.num h1').eq(1).text(data.heal)
            $('.num h1').eq(2).text(data.dead)
            $('.num h1').eq(3).text(data.confirm_add)
            $('.num h1').eq(4).text(data.import_confirm)
            $('.num h1').eq(5).text(data.import_confirm_add)
        },
        error:function f() {

        }
    })
}

// 更新城市疫情排行
function get_china_bottom_right() {
    $.ajax({
        url:'/get_china_bottom_right',
        success:function(data){
            ec_r1.data = data.city
            ec_r1_option.xAxis.data = data.city
            ec_r1_option.series[1].data = data.confirm
		    ec_r1.setOption(ec_r1_option)
        },
        error:function f() {

        }
    })
}

get_china_left();
get_china_top_right();
get_china_bottom_right();

setInterval(get_china_left,1000*60*60);
setInterval(get_china_top_right,1000*60*60);
setInterval(get_china_bottom_right,1000*60*60);