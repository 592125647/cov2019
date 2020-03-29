## cov2019疫情追踪

### Python使用flask、echarts框架，搭配Mysql数据库

## 项目基本介绍

1、 爬虫爬取腾讯新闻数据并筛选关键数据

* 数据来源 
   
      https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5
      https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5
      https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign

2、 使用Mysql建立数据库和关键表，存储爬取的数据

3、 使用flask框架，templates目录下存放html模板，
static目录存放各类静态文件
(static/css存放css样式，static/js存放js文件)

4、 使用 echarts 框架绘制

* 中国疫情地图、中国疫情趋势图、
* 全球疫情地图、全球疫情趋势图、
* 国内城市累计确诊排行图、国外累计确诊排行图

5、 部署项目定时刷新页面数据，1小时使用一次爬虫刷新数据库数据，也可以手动ctrl+f5清除浏览器缓存达到刷新页面的效果

6、 启动项目前请仔细阅读注意事项！

***
### 基本函数名、文件名定义介绍

* ##### left--左侧、right--右侧、top-left--左上侧、bottom-left--左下侧、bottom-right--右下侧
* ##### china--中国疫情地图、国内城市排行
* ##### china-trend--中国疫情趋势、外国累计确诊排行
* ##### world--世界疫情地图
* ##### world-trend--国外疫情趋势，不含中国
 
***

## 注意事项（请仔细阅读!)

* 数据库相关操作封装于utils.py文件，连接数据库前，请仔细阅读下列注意事项

* 先建立一个数据库，名为 cov2019

* 建立history表，用于存放全国疫情历史数据

* 建立details表，用于存放当日全国各城市更新的疫情数据

* 建立fforeign表，用于存放国外疫情数据

* 建立global表，用于存放全球疫情趋势数据

* 上述所需建立表的sql语句，均存放tables.md文件中，也可于utils模块更新相应表方法中查找到

* 当然可以自行修改表名，只需要修改utils模块中所有涉及的sql语句中相应的表名

* 因此不推荐自定义表名

* 第一次启动项目(执行app.py)会报错，提示数据不存在，是因为数据库操作还未执行，数据表内容为空，属于正常现象

* 等待出现提示"数据库更新数据成功"后，重新启动项目就解决了

* 世界疫情地图(world)如若未显示数据，可能是数据加载缓慢，需要等待几秒，属于正常情况

* 数据刷新未生效，在浏览器中按 ctrl+f5 清除缓存，重新获取数据

* 下面具体介绍各模块

*** 

## 模块介绍

### utils模块

* 封装了所有的数据库操作和获取数据的方法

* 刷新时间 -- get_time

* 连接数据库和更新表数据
    * 连接和关闭数据库 -- get_conn，close_conn

    * 进行sql查询 -- query
    
    * 更新history表，更新历史疫情数据  -- update_history
    
    * 更新details表，更新当日疫情数据  -- update_details
    
    * 更新fforeign表，更新国外疫情数据  -- update_fforeign
    
    * 更新global表，更新国外疫情数据  -- update_global
    
* 查询各项数据
    * 执行sql语句，获取各页面对应区域所需的数据 
    * 获取china左侧数据，中国疫情地图 -- get_china_left,
    * 获取china右上侧数据，疫情数据 -- get_china_top_right
    * 获取china右下侧数据，城市排行 -- get_china_bottom_right
    * 获取china-trend左上侧数据，全国累计趋势 -- get_china_trend_top_left
    * 获取china-trend左下侧数据，全国新增趋势 -- get_china_trend_bottom_left
    * 获取china-trend右侧数据，国家排行 -- get_china_trend_right
    * 获取world数据，世界疫情地图 -- get_world
    * 获取world-trend数据，国外趋势 -- get_world_trend

***

### spider模块 -- 爬虫

* 获取腾讯新闻数据，筛选并返回疫情的历史数据、当日数据、国外数据、境外输入数据

***

### app模块 -- 路由介绍

* ####模板
    * 主页，即中国疫情地图、国内城市排行 -- '/'
    
    * 中国疫情趋势、外国累计确诊排行 -- '/china-trend'
    
    * 世界疫情地图 -- '/world'
    
    * 国外疫情趋势 -- '/world-trend'
       
* #### 数据库
    * 刷新数据库各表数据 -- '/update_sql'

* #### 数据获取    
    * 刷新时间 -- '/get_time'
    
    * 主页-国内累计确诊疑似、治愈、死亡人数 -- '/get_china_top_right'
    
    * 主页-中国各省累计确诊数据 -- '/get_china_left'
    
    * 主页-除湖北省外城市累计确诊排行数据 -- '/get_china_bottom_right'
    
    * 中国累计确诊趋势 -- '/get_china_trend_top_left'
    
    * 中国新增确诊趋势 -- '/get_china_trend_bottom_left'
    
    * 国外累计确诊排行 -- '/get_china_trend_right'
    
    * 世界疫情地图数据 -- '/get_world'
    
    * 国外疫情趋势 -- '/get_world_trend'

***

## 静态文件介绍

* 各页面模板 
    * china.html, trend.html, world.html, country.html
    * 位于templates目录
    
* jquery资源 
    * jquery.min.js

* echarts资源 
    * echarts.min.js, dark.js

* 数据动态刷新 
    * controller.js

* 中国疫情地图相关
    * china.js, china-left.js

* 除湖北省外城市累计确诊排行 
    * china-bottom-right.js

* 中国累计确诊趋势
    * china-trend-top-left.js

* 中国新增确诊趋势
    * china-trend-bottom-left.js

* 国外累计确诊排行数据图
    * china-trend-right.js

* 世界疫情地图
    * world.js, world-map.js
    
* 国外累计、新增趋势
    * world-trend.js

***  
## 效果预览

![imgs view1](https://raw.githubusercontent.com/huyinhao/cov2019/master/imgs/view1.png)

![imgs view2](https://raw.githubusercontent.com/huyinhao/cov2019/master/imgs/view2.png)

![imgs view3](https://raw.githubusercontent.com/huyinhao/cov2019/master/imgs/view3.png)

![imgs view4](https://raw.githubusercontent.com/huyinhao/cov2019/master/imgs/view4.png)