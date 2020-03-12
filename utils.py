import time
import pymysql


# 获取时间
def get_time():
    time_str = time.strftime('%Y{}%m{}%d{} %X')
    return time_str.format('年', '月', '日')


# 连接数据库
def get_conn():
    '''
    return:连接，游标
    '''
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
    sql ='select city,confirm from ' \
         '(select city,confirm from details where update_time =' \
         '(select update_time from details order by update_time desc limit 1)' \
         'and province not in ("湖北","北京","上海","重庆","天津") union all ' \
         'select province as city,sum(confirm) as confirm from details ' \
         'where update_time =(select update_time from details order by update_time desc limit 1) ' \
         'and province in("北京","上海","重庆","天津") group by province) ' \
         'as a order by confirm desc limit 10'

    res = query(sql)
    return res


# 获取第二页右侧国外排行数据
def get_r2_data():
    """

    :return:返回各省数据
    """
    sql ='select country, confirm ,confirm_add, heal, dead  from fforeign ' \
         'where update_time =(select update_time from fforeign ' \
         'order by update_time desc limit 1) order by confirm  desc limit 5'

    res = query(sql)
    return res


if __name__ == '__main__':
    # 测试sql查询返回的数据
    data = get_c2_data()
    print(data)

