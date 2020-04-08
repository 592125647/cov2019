var ec_l2 = echarts.init(document.getElementById('l2'),'dark')

var ec_l2_option = {
    title:{
        text:'全国新增确诊、疑似趋势',
        textStyle:{
            fontSize : 22,
		},
		left:'left',
	},
    tooltip:{
        trigger:'axis',
		axisPointer:{
			type:'line',
			lineStyle:{
				color:'#7171C6',
			}

		},
    },
	legend:{
		data:['新增确诊','新增疑似'],
		left:'right',
		textStyle:{
            fontSize : 14,
        } ,
	},
	//图形位置
	grid: {
		left: '7%',
		right:'4%',
		bottom:'8%',
		top:50,
		containLable:true
	},
	xAxis: [{
	    type:'category',
		data:['01.20','01.21','01.22']
	}],
	yAxis: [{
		type:'value',
		axisLabel:{
			show:true,
			color:'white',
			fontSize:12,
			formatter: function(value){
				if(value >= 1000)
				{
					value = value / 1000 + 'k'
				}
				return value;
			}
		},
		axisLine:{
			show:true
		},
		splitLine:{
			show:true,
			lineStyle:{
				color:['#82ccdd','#b8e994','#78e08f','#38ada9','#079992'],
				width:1,
				type:'solid'
			}
		}
	}],
	series:[{
		name:'新增确诊',
		type:'line',
		smooth:true,
		color:'#B33771',
		data:[260,406,529]
	},{
		name:'新增疑似',
		type:'line',
		smooth:true,
		color:'#F8EFBA',
		data:[52,37,3935]
	}],
};

ec_l2.setOption(ec_l1_option)
