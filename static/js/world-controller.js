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
            world_option.series[0].nameMap = data.name
            world_option.series[0].data = data.data
		    world.setOption(world_option)
        },
        error:function f() {

        }
    })
}

update_sql();
get_time();

setInterval(update_sql,1000*60*60);
setInterval(get_time,1000);
get_world();
setInterval(get_world,1000*60*60);