## cov2019疫情追踪

### Python使用flask、echarts框架，搭配Mysql数据库

## 项目基本介绍

1、 爬虫爬取腾讯新闻数据并筛选关键数据

* 数据来源 https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5

2、 使用Mysql建立数据库和关键表，存储爬取的数据

3、 使用flask框架，templates目录下存放html模板，
static目录存放各类静态文件
(static/css存放css样式，static/js存放js文件)

4、 使用 echarts 框架绘制中国疫情地图，
全国疫情累计趋势图、全国疫情新增趋势图、
除湖北省外城市累计确诊排行图、以及国外累计确诊排行图

5、 部署项目定时刷新页面数据，1小时使用一次爬虫刷新数据库数据

6、 启动项目前请仔细阅读注意事项！

***
### 基本函数名、文件名定义介绍
##### c1--第一页累计数据页面，c2--第一页中国地图
##### r1--第一页城市排行图，l1--第二页累计数据图
##### l2--第二页当日新增图，r2--第二页国外排行图
***

## 注意事项（必读!)

* 数据库相关操作封装于utils.py文件，连接数据库前，请仔细阅读下列注意事项

* 先建立一个数据库，名为 cov2019

* 建立history表，用于存放全国疫情历史数据

* 建立details表，用于存放当日全国各城市更新的疫情数据

* 建立fforeign表，用于存放国外疫情数据

* 上述所需建立表的sql语句，均存放于utils模块中

* 当然可以自行修改表名，只需要修改utils模块中所有涉及的sql语句中相应的表名

* 因此不推荐自定义表名

* 启动项目前，必须先初始化history表

* 具体操作：先执行一次utils模块中的insert_history()方法，使history表不为空，
后续更新history会自动调用更新方法

* 注意：执行两次即以上insert_history()会提示数据已存在报错信息

* 下面具体介绍各模块

*** 

### 模块介绍

#### utils模块

* 存放了数据库操作的所有方法

* 动态刷新时间 -- get_time

* 连接和关闭数据库 -- get_conn，close_conn

* 进行sql查询 -- query

* 初始化history表，插入历史数据，只需执行一次 -- insert_history

* 在初始化后history表后，后续更新会自动调用此方法，更新历史疫情数据  -- update_history

* 更新details表，更新当日疫情数据  -- update_details

* 更新fforeign表，更新国外疫情数据  -- update_fforeign

* 执行sql语句，获取相应页面所需的数据 -- get_l1_data, get_l2_data,...get_r2_data

***

#### spider模块 -- 爬虫

* 获取腾讯新闻数据，筛选并返回疫情的历史数据、当日数据、国外数据

***

#### app模块 -- 路由介绍

* 访问主页，即根目录 -- '/'

* 刷新数据库数据 -- '/updatedata'

* 使用ajax技术刷新时间 -- '/time'

* 返回第一页中国累计疫情各项数据 -- '/c1'

* 返回第一页中国疫情地图数据 -- '/c2'

* 返回第一页除湖北省外城市累计确诊排行数据 -- '/r1'

* 返回第二页中国累计确诊数据 -- '/l1'

* 返回第二页中国新增确诊数据 -- '/l2'

* 返回第二页国外累计确诊排行数据 -- '/r2'

***

### 静态文件介绍

* 主页 -- index.html

* 导入jquery资源 -- jquery.min.js

* 导入echarts资源 -- echarts.min.js, dark.js

* 使用ajax技术动态刷新各类数据 -- controller.js

* 中国疫情地图 -- china.js, echart-c2.js

* 除湖北省外城市累计确诊排行图 -- echart-r1.js

* 中国累计确诊数据图 -- echart-l1.js

* 中国新增确诊数据图 -- echart-l2.js

* 国外累计确诊排行数据图 -- echart-r2.js

***  


