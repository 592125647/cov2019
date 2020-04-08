var chinaMap = echarts.init(document.getElementById('chinaMap'),'dark')

var mydata = [{'name':'上海','value':318},{'name':'北京','value':170}]

var chinaMap_option = {
    title:{
        text:'',
        subtext:'',
        x: 'left'
    },
    tooltip:{
        trigger:'item'
    },
    // 左侧小导航图标
    visualMap:{
        show:true,
        x:'20%',
        y:'80%',
        textStyle:{
            fontSize:18,
        },
        splitList:[
            {start:1,end:9},
            {start:10,end:99},
            {start:100,end:999},
            {start:1000,end:9999},
            {start:10000}
        ],
        color:['#CA1110','#C63920','#E55b25','#F2AD92','#F9DCD1']
    },

    series:[{
        name:'累计确诊人数',
        type:'map',
        mapType:'china',
        zoom : 1.1,
        roam:false, //拖放和缩放
        // 地图区域的多边形 图形样式
        itemStyle:{
            normal:{
                borderWidth:.5, // 区域边框宽度
                borderColor:'#009fe8', //区域边框颜色
                areaColor:'#ffefd5', //区域颜色
            },
            emphasis:{ //鼠标滑过地图高亮的相关设置
                borderWidth:.5,
                borderColor:'#4b0082',
                areaColor:'#fff',
            }
        },
        label:{
            normal:{
                show :true,//省份名称
                fontSize:18,
            },
            emphasis:{
                show :true,
                fontSize:18,
            }
        },
        data: mydata //数据
    }]
};
chinaMap.setOption(chinaMap_option)