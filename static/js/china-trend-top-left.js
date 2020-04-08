var l1 = echarts.init(document.getElementById('l1'),'dark')

var l1_option = {
    title:{
        text:'全国累计确诊、疑似、治愈、死亡',
        textStyle:{
			fontSize:22,
		},
		left:'left',
	},
    tooltip:{
        trigger:'axis',
		axisPointer:{
			type:'line',
			lineStyle:{
				color:'#7171C6'
			}
		},
    },
	legend:{
		data:['累计确诊','现有疑似','累计治愈','累计死亡'],
		left:'right',
		textStyle:{
            fontSize : 14,
        } ,
	},
	//图形位置
	grid: {
		left: '8%',
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
				type:'solid',
			}
		}
	}],
	series:[{
		name:'累计确诊',
		type:'line',
		smooth:true,
		data:[260,406,529]
	},{
		name:'现有疑似',
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
    
l1.setOption(l1_option)
