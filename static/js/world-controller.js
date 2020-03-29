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

get_world();
setInterval(get_world,1000*60*60);