import traceback
import pymysql
from spider import *


# 获取时间
def get_time():
    time_str = time.strftime('%Y{}%m{}%d{} %X')
    return time_str.format('年', '月', '日')


# 连接数据库
def get_conn():
    """
    return:连接，游标

    先建立mysql数据库, 库名(cov2019)
    """

    # 创建连接
    conn = pymysql.connect(host='127.0.0.1',
                           user='root', password='123456',
                           db='cov2019', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor


# 关闭数据库连接
def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


#  插入历史数据
def insert_history():
    """
    初始化数据库和表后，插入历史数据，只需执行一次，执行第二次就会报错

    mysql建立history表的sql语句

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

    :return:
    """
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]  # 0是历史数据，1是当日更新具体数据, 2是外国数据
        print(f'{time.asctime()}开始插入历史数据')
        conn, cursor = get_conn()
        sql = 'insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for k, v in dic.items():
            # item{'2020-1-20':{'confirm':,'suspect':,'heal':,'dead':}}
            cursor.execute(sql, [k, v.get('confirm'), v.get('confirm_add'),
                                 v.get('suspect'), v.get('suspect_add'),
                                 v.get('heal'), v.get('heal_add'),
                                 v.get('dead'), v.get('dead_add')
                                 ])

        conn.commit()  # 提交事务
        print(f'{time.asctime()}插入历史数据完毕')
    except:
        traceback.print_exc()

    finally:
        close_conn(conn, cursor)


# 更新历史数据
def update_history():
    """
    先执行插入历史数据操作(insert_history)，之后每次更新历史数据，只需执行此方法

    mysql建立history表的sql语句

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

    :return:
    """
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]
        print(f'{time.asctime()}开始更新历史数据')
        conn, cursor = get_conn()
        sql = 'insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        sql_query = 'select confirm from history where ds=%s'
        for k, v in dic.items():
            # item{'2020-1-20':{'confirm':,'suspect':,'heal':,'dead':}}
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get('confirm'), v.get('confirm_add'),
                                     v.get('suspect'), v.get('suspect_add'),
                                     v.get('heal'), v.get('heal_add'),
                                     v.get('dead'), v.get('dead_add')
                                     ])
        conn.commit()  # 提交事务
        print(f'{time.asctime()}历史数据更新完毕')
    except:
        traceback.print_exc()

    finally:
        close_conn(conn, cursor)


# 更新当日各城市数据
def update_details():
    """
    更新details表，更新当日各城市数据

    mysql建立details表的sql语句:

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

    """

    cursor = None
    conn = None
    try:
        li = get_tencent_data()[1]  # 0是历史数据，1是当日更新具体数据, 2是外国数据
        conn, cursor = get_conn()
        sql = 'insert into details(update_time,province,city,confirm,confirm_add,heal,dead) values(%s,%s,%s,%s,%s,%s,%s)'
        sql_query = 'select %s=(select update_time from details order by id desc limit 1)'
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f'{time.asctime()}开始更新今日最新数据')
            for item in li:
                cursor.execute(sql, item)
            conn.commit()  # 提交事务
            print(f'{time.asctime()}今日最新数据更新完毕')
        else:
            print(f'{time.asctime()}已是今日最新数据')
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


# 更新外国数据
def update_fforeign():
    """
    插入国外数据，更新当日国外各数据

    mysql建立表fforeign的sql语句：

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

    :return:
    """
    cursor = None
    conn = None
    try:
        li = get_tencent_data()[2]  # 0是历史数据，1是当日更新具体数据, 2是外国数据
        conn, cursor = get_conn()
        sql = 'insert into fforeign(update_time,country,confirm,confirm_add,suspect,heal,dead) values(%s,%s,%s,%s,%s,%s,%s)'
        sql_query = 'select %s=(select update_time from fforeign order by id desc limit 1)'
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f'{time.asctime()}开始更新国外数据')
            for item in li:
                cursor.execute(sql, item)
            conn.commit()  # 提交事务
            print(f'{time.asctime()}国外数据更新完毕')
        else:
            print(f'{time.asctime()}已是国外最新数据')
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


# sql查询
def query(sql, *args):
    """
    :param sql:
    :param args:
    :return:
    """

    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


# 获取第一页疫情情况数据
def get_c1_data():
    """

    :return:返回全国数据
    """
    sql = 'select sum(confirm),' \
          '(select suspect from history order by ds desc limit 1),' \
          'sum(heal),' \
          'sum(dead) ' \
          'from details ' \
          'where update_time=(select update_time from details order by update_time desc limit 1)'
    res = query(sql)
    return res[0]


# 获取第一页中国地图数据
def get_c2_data():
    """

    :return:返回各省数据
    """
    sql = 'select province, sum(confirm) from details ' \
          'where update_time=(select update_time from details ' \
          'order by update_time desc limit 1) ' \
          'group by province'
    res = query(sql)
    return res


# 获取第一页右侧城市排行数据
def get_r1_data():
    """

    :return:返回各省数据
    """
    sql = 'select city,confirm from ' \
          '(select city,confirm from details where update_time =' \
          '(select update_time from details order by update_time desc limit 1)' \
          'and province not in ("湖北","北京","上海","重庆","天津") union all ' \
          'select province as city,sum(confirm) as confirm from details ' \
          'where update_time =(select update_time from details order by update_time desc limit 1) ' \
          'and province in("北京","上海","重庆","天津") group by province) ' \
          'as a order by confirm desc limit 10'

    res = query(sql)
    return res


# 获取第二页左上角数据
def get_l1_data():
    """

    :return:
    """
    sql = 'select ds,confirm,suspect,heal,dead from history'
    res = query(sql)
    return res


# 获取第二页左下角数据
def get_l2_data():
    """

    :return:
    """
    sql = 'select ds,confirm_add,suspect_add from history'
    res = query(sql)
    return res


# 获取第二页右侧国外排行数据
def get_r2_data():
    """

    :return:返回国外数据
    """
    sql = 'select country, confirm ,confirm_add, heal, dead  from fforeign ' \
          'where update_time =(select update_time from fforeign ' \
          'order by update_time desc limit 1) order by confirm  desc limit 5'

    res = query(sql)
    return res


# 获取第三页世界地图数据
def get_world_data():
    """

    :return:返回世界各国数据
    """
    sql = 'select country,confirm from fforeign ' \
          'where update_time=' \
          '(select update_time from fforeign order by update_time desc limit 1) '

    res = query(sql)
    return res


# 获取第三页世界地图数据
def get_world_confirm():
    """

    :return:返回世界各国数据
    """
    sql = 'select update_time,sum(confirm),sum(heal),sum(dead) from fforeign group by update_time'

    res = query(sql)
    return res


if __name__ == '__main__':
    # 测试sql查询返回的数据
    # update_details()
    # update_history()
    # update_fforeign()
    data = get_world_confirm()
    print(data)

    # 建立好数据库和表后，执行插入历史数据， 只需执行一次！
    insert_history()
