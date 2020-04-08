import requests
import json
import time


# 发送请求
def get_url(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.132 Safari/537.36 '
    }
    res = requests.get(url, headers=header)
    res = json.loads(res.text)  # 转换json内容为字典
    return res


# 获取历史数据
def get_history_data():
    # 请求历史数据
    url_history = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
    data_history = get_url(url_history)
    data_history = json.loads(data_history['data'])  # 筛选历史数据

    history = {}  # 存放历史数据
    # 用于插入历史数据
    for i in data_history['chinaDayList']:
        ds = '2020' + i['date']  # data格式为'01.20'
        tup = time.strptime(ds, '%Y%m.%d')
        ds = time.strftime('%Y-%m-%d', tup)  # 改变时间格式为'2020-01-20'，不然插入数据库会报错
        confirm = i['confirm']  # 累计确诊
        heal = i['heal']  # 累计治愈
        dead = i['dead']  # 累计死亡
        now_confirm = i['nowConfirm']  # 现有确诊
        imported_case = i['importedCase']  # 累计境外输入
        no_infect = i['noInfect']  # 累计无症状感染者
        history[ds] = {'confirm': confirm, 'heal': heal, 'dead': dead, 'now_confirm': now_confirm,
                       'imported_case': imported_case, 'no_infect': no_infect}

    # 用于更新历史数据
    for i in data_history['chinaDayAddList']:
        ds = '2020' + i['date']  # data格式为'01.20'
        tup = time.strptime(ds, '%Y%m.%d')
        ds = time.strftime('%Y-%m-%d', tup)  # 改变时间格式为'2020-01-20'，不然插入数据库会报错
        confirm = i['confirm']  # 新增确诊
        heal = i['heal']  # 新增治愈
        dead = i['dead']  # 新增死亡
        history[ds].update({'confirm_add': confirm, 'heal_add': heal, 'dead_add': dead})

    return history


# 当日各城市数据
def get_details_data():
    # 请求各省详细数据
    url_details = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    data_details = get_url(url_details)
    data_details = json.loads(data_details['data'])  # 筛选当日全国数据

    details = []  # 存放当日详细数据
    update_time = data_details['lastUpdateTime']  # 更新日期
    data_country = data_details['areaTree']  # 其余国家和地区
    data_province = data_country[0]['children']  # 获取中国各省

    # 用于插入各省详细数据
    for pro_infos in data_province:
        provice = pro_infos['name']
        for city_infos in pro_infos['children']:  # 获取各省下的各市
            city = city_infos['name']  # 城市名称
            confirm = city_infos['total']['confirm']
            confirm_add = city_infos['today']['confirm']
            heal = city_infos['total']['heal']
            dead = city_infos['total']['dead']
            details.append([update_time, provice, city, confirm, confirm_add, heal, dead])
    return details


# 发送请求，获取各国数据
def get_url_country(url, country):
    url = url + country  # 拼接url
    #     print(url)
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.132 Safari/537.36 '
    }
    res = requests.get(url, headers=header)
    res = json.loads(res.text)  # 转换json内容为字典
    return res['data']


# 处理外国各国数据
def get_country_data(country):
    url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country='
    country_dict = {}
    # 请求各国数据
    data = get_url_country(url, country)  # url 拼接
    country_dict[country] = data  # 返回各国数据，存储到字典
    country_daily_data = []
    if country_dict.get(country):  # 不为空则进行数据处理
        for value in country_dict.get(country):  # 数据处理
            # value 格式{'date': '02.01', 'confirm_add': 0, 'confirm': 2, 'heal': 0, 'dead': 0}
            ds = '2020' + value['date']
            tup = time.strptime(ds, '%Y%m.%d')
            update_time = time.strftime('%Y-%m-%d', tup)  # 改变时间格式，不然插入数据库会报错
            value['date'] = update_time
            country_daily_data.append(list(value.values()))
        country_daily_data.append(country)  # 添加国家
    else:  # 为空跳过
        pass
    # 将最新日期放在首部，以便数据库更新查询
    country_daily_data.reverse()
    return country_daily_data


# 获取全球统计数据
def get_global_data():
    # 请求全球数据
    url_global = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,' \
                 'FAutoGlobalDailyList '
    global_data = get_url(url_global)
    global_today_data = global_data['data']['FAutoGlobalStatis']  # 筛选当日全球统计数据
    global_data = global_data['data']['FAutoGlobalDailyList']  # 筛选全球历史数据

    # 用于补充当日日期
    today = time.strftime("%Y-%m-%d", time.localtime())
    global_list = []
    for i in global_data:
        ds = '2020' + i['date']
        tup = time.strptime(ds, '%Y%m.%d')
        update_time = time.strftime('%Y-%m-%d', tup)  # 改变时间格式，不然插入数据库会报错
        confirm = i['all']['confirm']
        confirm_add = i['all']['newAddConfirm']
        heal = i['all']['heal']
        dead = i['all']['dead']
        global_list.append([update_time, confirm, confirm_add, heal, dead])
    global_list.append(
        [today, global_today_data['confirm'], global_today_data['nowConfirmAdd'], global_today_data['heal'],
         global_today_data['dead'], ])
    return global_list


# 获取境外输入数据
def get_import_case():
    url_today = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    data_today = get_url(url_today)
    data_today = json.loads(data_today['data'])  # 筛选当日数据

    now_confirm_add = data_today['chinaAdd']['nowConfirm']  # 新增现有确诊
    imported_case_add = data_today['chinaAdd']['importedCase']  # 新增境外输入
    no_infect_add = data_today['chinaAdd']['noInfect']  # 新增无症状感染者
    day_add = [now_confirm_add, imported_case_add, no_infect_add]
    return day_add


