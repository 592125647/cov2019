var world_confirm = echarts.init(document.getElementById('world_confirm'),'dark')
var world_confirm_option = {
    title:{
        text:'国外各项累计趋势',
        textStyle:{
			fontSize:20,
			color:'#D4F2E7',
		},
		left:'2%',
        top:'0%'
	},
    backgroundColor:'#333',
    tooltip:{
        trigger:'axis',
		axisPointer:{
			type:'line',
			lineStyle:{
				color:'#7171C6'
			}
		},
        textStyle:{
            fontSize : 14,
        } ,
    },
	legend:{
		data:['累计确诊'],
		textStyle:{
            fontSize : 14,
			color:'#D4F2E7',
        } ,
        top:'0%',
		left:'right',
	},
	//图形位置
	grid: {
		left: '10%',
		right:'0.5%',
        top:'10%',
		// bottom:'6%',
		containLable:true,

	},
	xAxis: [{
	    type:'category',
		data:['01.20','01.21','01.22'],

	}],
	yAxis: [{
		type:'value',
		axisLabel:{
			show:true,
			color:'#D4F2E7',
			fontSize:14,
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
				color:['#83bff6','#D4F2E7','#25F8CB','#EACD76'],
				width:2,
				type:'solid',
			}
		}
	}],
	series:[{
		name:'累计确诊',
		type:'line',
		smooth:true,
		data:[260,406,529]
	}],
};

world_confirm.setOption(world_confirm_option)
