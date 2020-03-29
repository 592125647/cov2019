
// 更新累计疫情趋势图
function get_china_trend_top_left() {
    $.ajax({
        url:'/get_china_trend_top_left',
        success:function(data){
            ec_l1_option.xAxis[0].data = data.day
            ec_l1_option.series[0].data = data.confirm
            ec_l1_option.series[1].data = data.suspect
            ec_l1_option.series[2].data = data.heal
            ec_l1_option.series[3].data = data.dead
		    ec_l1.setOption(ec_l1_option)
        },
        error:function f() {

        }
    })
}

// 更新疫情更新图
function get_china_trend_bottom_left() {
    $.ajax({
        url:'/get_china_trend_bottom_left',
        success:function(data){
            ec_l2_option.xAxis[0].data = data.day
            ec_l2_option.series[0].data = data.confirm_add
            ec_l2_option.series[1].data = data.suspect_add
		    ec_l2.setOption(ec_l2_option)
        },
        error:function f() {

        }
    })
}

// 更新国外疫情排行
function get_china_trend_right() {
    $.ajax({
        url:'/get_china_trend_right',
        success:function(data){
            ec_r2_option.yAxis.data = data.country
            ec_r2_option.series[0].data = data.confirm
            ec_r2_option.series[1].data = data.heal
            ec_r2_option.series[2].data = data.dead
		    ec_r2.setOption(ec_r2_option)
        },
        error:function f() {

        }
    })
}

get_china_trend_top_left();
get_china_trend_bottom_left();
get_china_trend_right();

setInterval(get_china_trend_top_left,1000*60*60);
setInterval(get_china_trend_bottom_left,1000*60*60);
setInterval(get_china_trend_right,1000*60*60);