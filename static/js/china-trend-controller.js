// 更新时间戳
function get_time(){
    $.ajax({
        url:'/get_time_china',
        timeout: 10000,
        success:function (data) {
            $('#time').html(data)
        },error:function () {

        }
    })
}

//更新数据库(history、details、fforeign三张表)
function update_sql(){
    $.ajax({
        url:'/update_china_trend',
        success:function (data) {

        },error:function () {

        }
    })
}

// 更新累计疫情趋势图
function get_china_trend_top_left() {
    $.ajax({
        url:'/get_china_trend_top_left',
        success:function(data){
            l1_option.xAxis[0].data = data.day
            l1_option.series[0].data = data.confirm
            l1_option.series[1].data = data.suspect
            l1_option.series[2].data = data.heal
            l1_option.series[3].data = data.dead
		    l1.setOption(l1_option)
        },
        error:function f() {

        }
    })
}

// 更新疫情更新图
function get_china_trend_top_center() {
    $.ajax({
        url:'/get_china_trend_top_center',
        success:function(data){
            l2_option.xAxis[0].data = data.day
            l2_option.series[0].data = data.confirm_add
            l2_option.series[1].data = data.suspect_add
		    l2.setOption(l2_option)
        },
        error:function f() {

        }
    })
}

// 治愈、死亡趋势
function get_china_trend_top_right() {
    $.ajax({
        url:'/get_china_trend_top_right',
        success:function(data){
            l3_option.xAxis[0].data = data.day
            l3_option.series[0].data = data.heal_add
            l3_option.series[1].data = data.dead_add
		    l3.setOption(l3_option)
        },
        error:function f() {

        }
    })
}

// 更新境外输入、无症状感染者累计趋势
function get_china_trend_bottom_left() {
    $.ajax({
        url:'/get_china_trend_bottom_left',
        success:function(data){

            r1_option.xAxis[0].data = data.day
            r1_option.series[0].data = data.imported_case
            r1_option.series[1].data = data.no_infect
		    r1.setOption(r1_option)
        },
        error:function f() {

        }
    })
}

// 更新城市疫情排行
function get_china_trend_bottom_center() {
    $.ajax({
        url:'/get_china_trend_bottom_center',
        success:function(data){
            r2.data = data.city
            r2_option.xAxis.data = data.city
            r2_option.series[1].data = data.imported_case
		    r2.setOption(r2_option)
        },
        error:function f() {

        }
    })
}

// 更新城市疫情排行饼图
function get_china_trend_bottom_right() {
    $.ajax({
        url:'/get_china_trend_bottom_right',
        success:function(data){
            r3_option.legend.data = data.city
            r3_option.series[0].data = data.imported_case
		    r3.setOption(r3_option)
        },
        error:function f() {

        }
    })
}

//访问时获取数据
// update_sql();
// get_time();
// get_china_trend_top_left();
// get_china_trend_top_center();
// get_china_trend_top_right();
// get_china_trend_bottom_left();
get_china_trend_bottom_center();
get_china_trend_bottom_right();

//停留页面时每一小时刷新一次数据
// setInterval(update_sql,1000*60*60);
// setInterval(get_time,1000*60*60);
// setInterval(get_china_trend_top_left,1000*60*60);
// setInterval(get_china_trend_top_center,1000*60*60);
// setInterval(get_china_trend_top_right,1000*60*60);
// setInterval(get_china_trend_bottom_center,1000*60*60);
// setInterval(get_china_trend_bottom_right,1000*60*60);