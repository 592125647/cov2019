var r2 = echarts.init(document.getElementById('r2'), 'dark')
var dataAxis = ['点', '击', '柱', '子', '或', '两', '指', '缩', '放'];
var data = [220, 182, 191, 234, 290, 330, 334, 198, 123, 125, 220];
var yMax = 100;
var dataShadow = [];
r2.data = [];

for (var i = 0; i < data.length; i++) {
    dataShadow.push(yMax);
}

r2_option = {
    title: {
        text: '累计境外输入城市排行',
        left:'center',
        top:'1%',
        textStyle:{
            fontSize : 22,
		},
    },
    tooltip:{
		axisPointer:{
			type:'cross',
			lineStyle:{
				color:'#7171C6'
			},
            crossStyle:{
			    type:'dashed',
            }
		},
    },
    //图形位置
	grid: {
		left: '1',
		right:'1',
		bottom:'0%',
		containLable:true
	},
    xAxis: {
        data: dataAxis,
        type:'category',
        axisLabel: {
            inside: true,
            textStyle: {
                color: '#fff'
            }
        },
        axisTick: {
            show: false
        },
        axisLine: {
            show: false
        },
        z: 10,
        axisPointer:{
            type: 'none',
        }
    },
    yAxis: {
        axisLine: {
            show: false
        },
        axisTick: {
            show: false
        },
        axisLabel: {
            textStyle: {
                color: '#999'
            }
        },
        splitLine:{
			show:false,
		},

    },
    dataZoom: [
        {
            type: 'inside'
        }
    ],

    series: [
        { // For shadow
            type: 'bar',
            itemStyle: {
                color: 'rgba(0,0,0,0.05)'
            },
            barGap: '-100%',
            barCategoryGap: '40%',
            data: dataShadow,
            animation: false
        },
        {
            type: 'bar',
            itemStyle: {
                color: new echarts.graphic.LinearGradient(
                    0, 0, 0, 1,
                    [
                        // {offset: 0, color: '#83bff6'},
                        // {offset: 0.5, color: '#188df0'},
                        // {offset: 1, color: '#188df0'}
                        {offset: 0, color: '#D1D9E0'},
                        {offset: 0.5, color: '#B0A4E3'},
                        {offset: 1, color: '#4C8DAE'}
                    ]
                )
            },
            emphasis: {
                itemStyle: {
                    color: new echarts.graphic.LinearGradient(
                        0, 0, 0, 1,
                        [
                            // {offset: 0, color: '#2378f7'},
                            // {offset: 0.7, color: '#2378f7'},
                            // {offset: 1, color: '#83bff6'}
                            {offset: 0, color: '#4C8DAE'},
                            {offset: 0.7, color: '#B0A4E3'},
                            {offset: 1, color: '#D1D9E0'}
                        ]
                    )
                }
            },
            data: data
        }
    ]
};

// Enable data zoom when user click bar.
var zoomSize = 6;
r2.on('click', function (params) {
    console.log(params)
    console.log(r2.data[Math.max(params.dataIndex - zoomSize / 2, 0)]);

    r2.dispatchAction({
        type: 'dataZoom',
        startValue: r2.data[Math.max(params.dataIndex - zoomSize / 2, 0)],
        endValue: r2.data[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
    });
});
r2.setOption(r2_option)