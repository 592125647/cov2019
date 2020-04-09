// 更新时间戳
function get_time(){
    $.ajax({
        url:'/get_time_global',
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
        url:'/update_world',
        success:function (data) {

        },error:function () {

        }
    })
}

// 更新世界疫情地图
function get_world() {
    $.ajax({
        url:'/get_world',
        success:function(data){
            worldMap_option.series[0].nameMap = data.name
            worldMap_option.series[0].data = data.data
		    worldMap.setOption(worldMap_option)
        },
        error:function f() {

        }
    })
}

//访问时获取数据
update_sql();
get_time();
get_world();

//停留页面时每一小时刷新一次数据
setInterval(update_sql,1000*60*60);
setInterval(get_time,1000*60*60);
setInterval(get_world,1000*60*60);