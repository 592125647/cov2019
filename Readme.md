## 2019新冠病毒疫情追踪

#### 使用flask、echarts框架，搭配Mysql数据库

### 数据来源

以腾讯新闻动态疫情作为来源
https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5

***
##### l1--第二页左上页面，l2--第二页左下页面
##### c1--第一页疫情信息页面，c2--第一页中国地图页面
##### r1--第一页城市排行页面，r2--第二页国外排行页面
***

### 项目基本介绍

1、 爬虫爬取腾讯新闻数据并筛选关键数据

2、 使用Mysql建立数据库和关键表，存储爬取的数据

*  数据库相关操作封装于utils.py文件，进行连接数据库前，
需要自行更改get_conn()方法中的参数（host,user,password,db,charset）
之后也会展示utils模块的具体介绍

3、 使用了flask框架，../templates存放html模板，
../static存放各类静态文件
(/css存放css样式，/js存放js文件)

4、 启动app.py，访问index.html页面
将会读取数据库中的数据，使用 echarts 框架绘制中国疫情地图，
全国疫情累计趋势图、全国疫情新增趋势图、
除湖北省外城市累计确诊排行图、以及国外累计确诊排行图

5、 部署项目定时刷新页面数据，达到实时获取的目的

### 函数介绍

#### utils模块

* 动态刷新时间 -- get_time

* 连接和关闭数据库 -- get_conn，close_conn

* 进行sql查询 -- query

* 获取对应页面的数据 -- get_l1_data, get_l2_data,...get_r2_data

#### app模块--路由介绍

* 访问主页 -- '//'index.html

* 使用ajax技术刷新时间 -- '/time'

* 返回第一页中国累计疫情各项数据 -- '/c1'

* 返回第一页中国疫情地图数据 -- '/c2'

* 返回第一页除湖北省外城市累计确诊排行数据 -- '/r1'

* 返回第二页中国累计确诊数据 -- '/l1'

* 返回第二页中国新增确诊数据 -- '/l2'

* 返回第二页国外累计确诊排行数据 -- '/r2'

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

