//更新数据库(history、details、fforeign三张表)
function update_time(){
    $.ajax({
        url:'/updatedata',
        success:function (data) {

        },error:function () {

        }
    })
}

// 更新时间戳
function get_time(){
    $.ajax({
        url:'/time',
        timeout: 10000,
        success:function (data) {
            $('#time').html(data)
        },error:function () {

        }
    })
}

// 更新中国累计数据
function get_c1_data() {
    $.ajax({
        url:'/c1',
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

// 更新中国疫情地图
function get_c2_data() {
    $.ajax({
        url:'/c2',
        success:function(data){
           ec_center_option.series[0].data = data.data
		   ec_center.setOption(ec_center_option)
        },
        error:function f() {

        }
    })
}

// 更新城市疫情排行
function get_r1_data() {
    $.ajax({
        url:'/r1',
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
function get_l1_data() {
    $.ajax({
        url:'/l1',
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
function get_l2_data() {
    $.ajax({
        url:'/l2',
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
function get_r2_data() {
    $.ajax({
        url:'/r2',
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

get_time()  // 启动时获取数据
get_c1_data()
get_c2_data()
get_l1_data()
get_l2_data()
get_r1_data()
get_r2_data()
update_time()

setInterval(get_time,1000);
setInterval(get_c1_data,1000*60*60);  // 启动之后之后，每隔1小时刷新数据一次
setInterval(get_c2_data,1000*60*60);
setInterval(get_r1_data,1000*60*60);
setInterval(get_l1_data,1000*60*60);
setInterval(get_l2_data,1000*60*60);
setInterval(get_r2_data,1000*60*60);
setInterval(update_time,1000*60*60);
