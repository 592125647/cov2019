import requests
import json
import time


# 发送请求
def get_url(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    res = requests.get(url, headers=header)
    res = json.loads(res.text)  # 转换json内容为字典
    data = json.loads(res['data'])  # 筛选历史数据
    return data


# 获取境外输入数据
def get_import_case():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    data = get_url(url)
    import_confirm = data['chinaTotal']['importedCase']  # 累计境外输入
    import_confirm_add = data['chinaAdd']['importedCase']  # 新增境外输入
    return import_confirm, import_confirm_add


# 获取更新数据
def get_tencent_data():
    # 当日之前的历史数据
    url_history = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
    # 当日更新数据
    url_details = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    # 全球数据
    url_global = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign'

    data_history = get_url(url_history)
    data_details = get_url(url_details)
    data_global = get_url(url_global)

    # 历史数据
    history = {}  # 存放历史数据
    # 用于插入历史数据
    for i in data_history['chinaDayList']:
        ds = '2020' + i['date']  # data格式为'01.20'
        tup = time.strptime(ds, '%Y%m.%d')
        ds = time.strftime('%Y-%m-%d', tup)  # 改变时间格式为'2020-01-20'，不然插入数据库会报错
        confirm = i['confirm']  # 累计确诊
        suspect = i['suspect']  # 累计疑似
        heal = i['heal']  # 累计治愈
        dead = i['dead']  # 累计死亡
        history[ds] = {'confirm': confirm, 'suspect': suspect, 'heal': heal, 'dead': dead}

    # 用于更新历史数据
    for i in data_history['chinaDayAddList']:
        ds = '2020' + i['date']  # data格式为'01.20'
        tup = time.strptime(ds, '%Y%m.%d')
        ds = time.strftime('%Y-%m-%d', tup)  # 改变时间格式为'2020-01-20'，不然插入数据库会报错
        confirm = i['confirm']  # 累计确诊
        suspect = i['suspect']  # 累计疑似
        heal = i['heal']  # 累计治愈
        dead = i['dead']  # 累计死亡
        history[ds].update({'confirm_add': confirm, 'suspect_add': suspect, 'heal_add': heal, 'dead_add': dead})

    # 当日各城市数据
    details = []  # 存放当日详细数据
    update_time = data_details['lastUpdateTime']

    data_country = data_details['areaTree']  # 其余国家和地区
    data_province = data_country[0]['children']  # 获取中国各省
    for pro_infos in data_province:
        provice = pro_infos['name']
        for city_infos in pro_infos['children']:  # 获取各省下的各市
            city = city_infos['name']
            confirm = city_infos['total']['confirm']
            confirm_add = city_infos['today']['confirm']
            heal = city_infos['total']['heal']
            dead = city_infos['total']['dead']
            details.append([update_time, provice, city, confirm, confirm_add, heal, dead])

    # 国外数据
    fforeign = []  # 存放国外数据
    for i in data_global['foreignList']:  # 外国列表
        ds = '2020' + i['date']  # data格式为'01.20'
        tup = time.strptime(ds, '%Y%m.%d')
        update_time = time.strftime('%Y-%m-%d', tup)  # 改变时间格式为'2020-01-20'，不然插入数据库会报错
        country = i['name']
        confirm = i['confirm']
        confirm_add = i['confirmAdd']
        suspect = i['suspect']
        heal = i['heal']
        dead = i['dead']
        fforeign.append([update_time, country, confirm, confirm_add, suspect, heal, dead])

    global_dict = []
    for i in data_global['globalDailyHistory']:
        ds = '2020' + i['date']
        tup = time.strptime(ds, '%Y%m.%d')
        update_time = time.strftime('%Y-%m-%d', tup)  # 改变时间格式，不然插入数据库会报错
        confirm = i['all']['confirm']
        confirm_add = i['all']['newAddConfirm']
        heal = i['all']['heal']
        dead = i['all']['dead']
        global_dict.append([update_time, confirm, confirm_add, heal, dead])

    return history, details, fforeign, global_dict


if __name__ == '__main__':
    print(get_tencent_data()[2])
