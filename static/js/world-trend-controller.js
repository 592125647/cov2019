// 更新国外趋势图
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

get_world_trend();
setInterval(get_world_trend,1000*60*60);