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
        url:'/update_china',
        success:function (data) {

        },error:function () {

        }
    })
}

// 更新中国疫情地图
function get_china_left() {
    $.ajax({
        url:'/get_china_left',
        success:function(data){
           chinaMap_option.series[0].data = data.data
		   chinaMap.setOption(chinaMap_option)
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
            $('.num h1').eq(3).text(data.now_confirm)
            $('.num h1').eq(4).text(data.imported_case)
            $('.num h1').eq(5).text(data.no_infect)
            $('.new h4').eq(0).text(data.confirm_add)
            $('.new h4').eq(1).text(data.heal_add)
            $('.new h4').eq(2).text(data.dead_add)
            $('.new h4').eq(3).text(data.now_confirm_add)
            $('.new h4').eq(4).text(data.imported_case_add)
            $('.new h4').eq(5).text(data.no_infect_add)
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
            city.data = data.city
            city_option.xAxis.data = data.city
            city_option.series[1].data = data.confirm
		    city.setOption(city_option)
        },
        error:function f() {

        }
    })
}

//访问时获取数据
update_sql();
get_time();
get_china_left();
get_china_top_right();
get_china_bottom_right();

//停留页面时每一小时刷新一次数据
setInterval(update_sql,1000*60*60);
setInterval(get_time,1000*60*60);
setInterval(get_china_left,1000*60*60);
setInterval(get_china_top_right,1000*60*60);
setInterval(get_china_bottom_right,1000*60*60);