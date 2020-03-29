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

// 启动时获取数据
update_sql();
get_time();

// 启动之后之后，每隔1小时刷新数据一次
setInterval(update_sql,1000*60*60);
setInterval(get_time,1000);