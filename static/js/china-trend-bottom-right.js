var r3 = echarts.init(document.getElementById('r3'),'dark')
r3_option = {
    title: {
        text: '累计境外输入省市排行',
        left: 'center',
        textStyle:{
            fontSize : 22,
		},
    },
    //图形位置
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
    // 图注
    legend: {
        type: 'scroll',
        orient: 'vertical',
        right: 5,
        top: '32%',
        bottom: 20,
        data: ['上海','黑龙江'],
    },
    series: [
        {
            name: '城市',
            type: 'pie',
            radius: '75%',
            center: ['47%', '58%'],
            label: {
                fontSize: 16,
                color: '#83bff6'
            },
            labelLine: {
                lineStyle: {
                    color: '#235894'
                }
            },
            data:[{name:'上海',value:90},{name:'黑龙江',value:67}],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                },
                label: {
                    fontSize : 22,
                    color:'#F8EFBA',
                }
            },

        }
    ]
};
r3.setOption(r3_option)