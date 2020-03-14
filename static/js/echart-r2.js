var ec_r2 = echarts.init(document.getElementById('r2'),'dark')

var seriesLabel = {
    normal: {
        show: true,
        textBorderColor: '#434343',
        textBorderWidth: 3
    }
}

ec_r2_option = {
    title: {
        text: '国外疫情严重国家排行',
        left: 15 ,
        textStyle:{
            fontSize: 24,
        }
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['累计确诊', '累计治愈', '累计死亡'],
        right:0,
        textStyle:{
            fontSize : 16,
        } ,
    },
    grid: {
        left: 60,
        bottom:30,
        right:40
    },

    xAxis: {
        type: 'value',
        name: '人',
        axisLabel: {
            formatter: '{value}'
        }
    },
    yAxis: {
        type: 'category',
        inverse: true,
        data: ['意大利', '伊朗', '韩国'],
        axisLabel:{
            fontSize : 16,
        } ,
    },
    series: [
        {
            name: '累计确诊',
            type: 'bar',
            data: [165, 170, 30],
            label: seriesLabel,
        },
        {
            name: '累计治愈',
            type: 'bar',
            label: seriesLabel,
            data: [150, 105, 110],
            markPoint: {
                symbolSize: 1,
                symbolOffset: [0, '50%'],
                label: {
                    formatter: '{a|累计治愈}\n{b|{b} }{c|{c}}',
                    backgroundColor: 'rgb(242,242,242)',
                    borderColor: '#aaa',
                    borderWidth: 1,
                    borderRadius: 4,
                    padding: [4, 10],
                    lineHeight: 26,
                    shadowBlur: 15,
                    shadowColor: '#000',
                    shadowOffsetX: 0,
                    shadowOffsetY: 1,
                    position: 'right',
                    distance: 20,
                    width:80,
                    height:45,
                    rich: {
                        a: {
                            align: 'center',
                            color: '#fff',
                            fontSize: 16,
                            textShadowBlur: 2,
                            textShadowColor: '#000',
                            textShadowOffsetX: 0,
                            textShadowOffsetY: 1,
                            textBorderColor: '#333',
                            textBorderWidth: 2
                        },
                        b: {
                            color: '#333',
                            fontSize:14
                        },
                        c: {
                            color: '#ff8811',
                            textBorderColor: '#000',
                            textBorderWidth: 1,
                            fontSize: 16
                        }
                    }
                },
                data: [
                    {type: 'max', name: 'max:'},
                ]
            }
        },
        {
            name: '累计死亡',
            type: 'bar',
            label: seriesLabel,
            data: [220, 82, 63],
            markPoint: {
                symbolSize: 1,
                symbolOffset: [0, '50%'],
                label: {
                    formatter: '{a|累计死亡}\n{b|{b} }{c|{c}}',
                    backgroundColor: 'rgb(242,242,242)',
                    borderColor: '#aaa',
                    borderWidth: 1,
                    borderRadius: 4,
                    padding: [4, 10],
                    lineHeight: 26,
                    shadowBlur: 15,
                    shadowColor: '#000',
                    shadowOffsetX: 0,
                    shadowOffsetY: 1,
                    position: 'right',
                    distance: 20,
                    width:70,
                    height:45,
                    rich: {
                        a: {
                            align: 'center',
                            color: '#fff',
                            fontSize: 16,
                            textShadowBlur: 2,
                            textShadowColor: '#000',
                            textShadowOffsetX: 0,
                            textShadowOffsetY: 1,
                            textBorderColor: '#333',
                            textBorderWidth: 2
                        },
                        b: {
                            color: '#333',
                            fontSize:14
                        },
                        c: {
                            color: '#ff8811',
                            textBorderColor: '#000',
                            textBorderWidth: 1,
                            fontSize: 16
                        }
                    }
                },
                data: [
                    {type: 'max', name: 'max:'},
                ]
            }
        }
    ]
};

ec_r2.setOption(ec_r2_option)