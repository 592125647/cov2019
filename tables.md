# 存放各表建立语句

# history

create table history(
ds datetime not null comment'日期',
confirm int(11) default null comment'累计确诊',
confirm_add int(11) default null comment'当日新增确诊',
suspect int(11) default null comment'剩余疑似',
suspect_add int(11) default null comment'当日新增疑似',
heal int(11) default null comment'累计治愈',
heal_add int(11) default null comment'当日新增治愈',
dead int(11) default null comment'累计死亡',
dead_add int(11) default null comment'当日新增死亡',
primary key(ds) using btree
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

***
# details

create table details(
id int(11) not null auto_increment,
update_time datetime default null comment '数据最后更新时间',
province varchar(50) default null comment'省',
city varchar(50) default null comment'市',
confirm int(11) default null comment'累计确诊',
confirm_add int(11) default null comment'新增确诊',
heal int(11) default null comment'累计治愈',
dead int(11) default null comment'累计死亡',
primary key(id) 
)engine=InnoDB default charset=utf8mb4;

***
# fforeign

create table fforeign(
id int(11) not null auto_increment,
update_time datetime default null comment '数据最后更新时间',
country varchar(50) not null comment'国',
confirm int(11) default null comment'累计确诊',
confirm_add int(11) default null comment'新增确诊',
suspect int(11) default null comment'累计疑似',
heal int(11) default null comment'累计治愈',
dead int(11) default null comment'累计死亡',
primary key(id) 
)engine=InnoDB default charset=utf8mb4;

***

# global

create table global(
update_time datetime  comment '数据最后更新时间',
confirm int(11) default null comment'累计确诊',
confirm_add int(11) default null comment'新增确诊',
heal int(11) default null comment'累计治愈',
dead int(11) default null comment'累计死亡',
primary key(update_time)
)engine=InnoDB default charset=utf8mb4;

***