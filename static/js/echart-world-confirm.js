var world_confirm = echarts.init(document.getElementById('world_confirm'),'dark')
var world_confirm_option = {
    title:{
        text:'国外累计趋势',
        textStyle:{
			fontSize:28,
		},
		left:'5%',
        top:50,
	},
    backgroundColor:'#666',
    tooltip:{
        trigger:'axis',
		axisPointer:{
			type:'line',
			lineStyle:{
				color:'#7171C6'
			}
		},
        textStyle:{
            fontSize : 16,
        } ,
    },
	legend:{
		data:['累计确诊','新增确诊','累计治愈','累计死亡'],
		left:'right',
		textStyle:{
            fontSize : 18,
        } ,
        top:50,
	},
	//图形位置
	grid: {
		left: '6%',
		right:'6%',
		bottom:'6%',
		top:100,
		containLable:true
	},
	xAxis: [{
	    type:'category',
		data:['01.20','01.21','01.22'],

	}],
	yAxis: [{
		type:'value',
		axisLabel:{
			show:true,
			color:'black',
			fontSize:16,
			formatter: function(value){
				if(value >= 1000)
				{
					value = value / 1000 + 'k'
				}
				return value;
			}
		},
		axisLine:{
			show:true,

		},
		splitLine:{
			show:true,
			lineStyle:{
				color:'#83bff6',
				width:2,
				type:'dashed',
			}
		}
	}],
	series:[{
		name:'累计确诊',
		type:'line',
		smooth:true,
		data:[260,406,529]
	},{
		name:'新增确诊',
		type:'line',
		smooth:true,
		data:[52,37,3935]
	},
	{
		name:'累计治愈',
		type:'line',
		smooth:true,
		data:[26,26,26]
	},
	{
		name:'累计死亡',
		type:'line',
		smooth:true,
		data:[6,9,17]
	}],
};

world_confirm.setOption(world_confirm_option)
