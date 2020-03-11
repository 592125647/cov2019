## 2019新冠病毒疫情追踪

#### 使用flask、echarts框架，搭配Mysql数据库

### 数据来源

以腾讯新闻动态疫情作为来源
https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5

***
##### l1--左上页面，l2--左下页面
##### c1--中上页面，c2--中上页面
##### r1--右上页面，r2--右上页面
***
### utils函数介绍

* 动态刷新时间 -- get_time

* 连接和关闭数据库 -- get_conn，close_conn

* 进行sql查询 -- query

* 获取对应页面的数据 -- get_l1_data, get_l2_data...
