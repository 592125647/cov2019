import traceback
import pymysql
from spider import *
import nameMap


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


# 更新历史数据
def update_history():
    """
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
        sql = 'insert into fforeign(update_time,country,confirm,confirm_add,suspect,heal,dead) ' \
              'values(%s,%s,%s,%s,%s,%s,%s)'
        sql_query = 'select %s=(select update_time from fforeign ' \
                    'where update_time=(select update_time from fforeign order by update_time desc limit 1)limit 1)'
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


def update_global():
    """
    更新global表

    create table global(
    update_time datetime  comment '数据最后更新时间',
    confirm int(11) default null comment'累计确诊',
    confirm_add int(11) default null comment'新增确诊',
    heal int(11) default null comment'累计治愈',
    dead int(11) default null comment'累计死亡',
    primary key(update_time)
    )engine=InnoDB default charset=utf8mb4;
    """
    cursor = None
    conn = None
    try:
        li = get_tencent_data()[3]  # 0是历史数据，1是更新具体数据，2是外国数据，3是全球趋势数据
        conn, cursor = get_conn()
        sql = 'insert into global(update_time,confirm,confirm_add,heal,dead) values(%s,%s,%s,%s,%s)'
        sql_query = 'select confirm from global where update_time=%s'
        sql_update_query = 'select %s =(select confirm_add from global where update_time=%s)'
        update = 'update global set confirm_add=%s where update_time =%s'
        print(f'{time.asctime()}开始更新全球趋势数据')
        for item in li:  # 更新当日数据
            cursor.execute(sql_query, item[0])
            if not cursor.fetchone():
                cursor.execute(sql, item)
            else:
                for temp in li[len(li) - 4:]:  # 更新新增确诊数
                    update_temp = [temp[2], temp[0]]
                    cursor.execute(sql_update_query, update_temp)
                    if not cursor.fetchone()[0]:
                        cursor.execute(update, update_temp)
            conn.commit()  # 提交事务
        print(f'{time.asctime()}全球趋势数据更新完毕')
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


# 获取china左侧数据，中国疫情地图
def get_china_left():
    """

    :return:返回各省数据
    """
    sql = 'select province, sum(confirm) from details ' \
          'where update_time=(select update_time from details ' \
          'order by update_time desc limit 1) ' \
          'group by province'
    res = query(sql)
    return res


# 获取china右上侧数据，疫情数据
def get_china_top_right():
    """

    :return:返回全国累计数据
    """
    sql = 'select sum(confirm),' \
          '(select suspect from history order by ds desc limit 1),' \
          'sum(heal),' \
          'sum(dead)' \
          'from details ' \
          'where update_time=(select update_time from details order by update_time desc limit 1)'
    res1 = query(sql)

    # 获取境外输入的累计确诊和新增确诊
    sql_import = 'SELECT sum(confirm),sum(confirm_add) FROM details WHERE city = "境外输入" ' \
                 'and update_time=(select update_time from details order by update_time desc limit 1)'
    res2 = query(sql_import)
    return res1[0], res2[0]


# 获取china右下侧数据，城市排行
def get_china_bottom_right():
    """

    :return:返回城市排行数据
    """
    sql = 'select city,confirm from ' \
          '(select city,confirm from details where update_time =' \
          '(select update_time from details order by update_time desc limit 1)' \
          'and province not in ("湖北","北京","上海","重庆","天津")and city != "地区待确认" ' \
          'union all select province as city,sum(confirm) as confirm from details ' \
          'where update_time =(select update_time from details order by update_time desc limit 1) ' \
          'and province in("北京","上海","重庆","天津") group by province) ' \
          'as a order by confirm desc limit 12'

    res = query(sql)
    return res


# 获取china-trend左上侧数据，全国累计趋势
def get_china_trend_top_left():
    """

    :return:返回全国累计趋势
    """
    sql = 'select ds,confirm,suspect,heal,dead from history'
    res = query(sql)
    return res


# 获取china-trend左下侧数据，全国新增趋势
def get_china_trend_bottom_left():
    """

    :return:返回全国新增趋势
    """
    sql = 'select ds,confirm_add,suspect_add from history'
    res = query(sql)
    return res


# 获取china-trend右侧数据，国家排行
def get_china_trend_right():
    """

    :return:返回国外排行数据
    """
    sql = 'select country, confirm ,confirm_add, heal, dead  from fforeign ' \
          'where update_time =(select update_time from fforeign ' \
          'order by update_time desc limit 1) order by confirm  desc limit 7'

    res = query(sql)
    return res


# 获取world数据，世界疫情地图
def get_world():
    """

    :return:返回世界各国数据
    """
    conn, cursor = get_conn()
    country_list = list(nameMap.namemap.values())
    global_dict = {}
    for item in country_list:
        sql = 'select confirm from fforeign where country = %s order by update_time desc limit 1'
        if cursor.execute(sql, item):
            res = cursor.fetchall()
            global_dict[item] = res[0][0]
    close_conn(conn, cursor)
    return global_dict


# 获取world-trend数据，世界趋势
def get_world_trend():
    """

    :return:返回世界趋势数据
    """
    # sql = 'select update_time,sum(confirm),sum(heal),sum(dead) from fforeign group by update_time'
    sql = 'SELECT * FROM global'
    res = query(sql)
    return res


if __name__ == '__main__':
    data, confirm = get_china_top_right()
    print(data, confirm)