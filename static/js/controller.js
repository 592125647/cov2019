//更新数据库(history、details、fforeign三张表)
function update_sql(){
    $.ajax({
        url:'/update_sql',
        success:function (data) {

        },error:function () {

        }
    })
}

// 更新时间戳
function get_time(){
    $.ajax({
        url:'/get_time',
        timeout: 10000,
        success:function (data) {
            $('#time').html(data)
        },error:function () {

        }
    })
}

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
            $('.num h1').eq(1).text(data.suspect)
            $('.num h1').eq(2).text(data.heal)
            $('.num h1').eq(3).text(data.dead)
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

function get_world() {
    $.ajax({
        url:'/get_world',
        success:function(data){
            world_option.series[0].nameMap = data.name
            world_option.series[0].data = data.data
		    world.setOption(world_option)
        },
        error:function f() {

        }
    })
}

function get_world_trend() {
    $.ajax({
        url:'/get_world_trend',
        success:function(data){
            world_confirm_option.xAxis[0].data = data.day
            world_confirm_option.series[0].data = data.confirm
            world_confirm_option.series[1].data = data.heal
            world_confirm_option.series[2].data = data.dead
            world_confirm_option.series[3].data = data.confirm_add
		    world_confirm.setOption(world_confirm_option)
        },
        error:function f() {

        }
    })
}

// 启动时获取数据
update_sql()
// get_time()
// get_china_top_right();
// get_china_left();
// get_china_trend_top_left();
// get_china_trend_bottom_left();
// get_china_bottom_right();
// get_china_trend_right();
// get_world();
// get_world_trend();

// 启动之后之后，每隔1小时刷新数据一次
// setInterval(update_sql,1000*60*60);
// setInterval(get_time,1000);
// setInterval(get_china_top_right,1000*60*60);
// setInterval(get_china_left,1000*60*60);
// setInterval(get_china_bottom_right,1000*60*60);
// setInterval(get_china_trend_top_left,1000*60*60);
// setInterval(get_china_trend_bottom_left,1000*60*60);
// setInterval(get_china_trend_right,1000*60*60);
// setInterval(get_world,1000*60*60);
// setInterval(get_world_trend,1000*60*60);

