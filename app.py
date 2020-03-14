from flask import Flask
from flask import render_template
from flask import jsonify
from datetime import timedelta
import utils
import nameMap

app = Flask(__name__)


@app.route('/')
def hello_index():
    return render_template('index.html')


@app.route('/updatedata')
def update_data():
    utils.update_history()
    utils.update_details()
    utils.update_fforeign()
    print('数据库更新数据成功')
    return render_template('index.html')


@app.route('/time')
def get_time():
    # 获取当地时间
    # print(utils.get_time())
    return utils.get_time()


@app.route('/c1')
def get_c1_data():
    # 获取累计确诊疑似、治愈、死亡人数
    data = utils.get_c1_data()
    return jsonify({'confirm': int(data[0]), 'suspect': int(data[1]), 'heal': int(data[2]), 'dead': int(data[3])})


@app.route('/c2')
def get_c2_data():
    # 获取中国各省累计确诊人数
    res = []
    for tup in utils.get_c2_data():
        # print(tup)
        res.append({'name': tup[0], 'value': int(tup[1])})
    return jsonify({'data': res})


@app.route('/r1')
def get_r1_data():
    # 获取除湖北省外累计确诊最多的10个城市
    data = utils.get_r1_data()
    city, confirm = [], []
    for i in data:
        city.append(i[0])  # 城市
        confirm.append(int(i[1]))  # 累计确诊人数
        # print(city, confirm)
    return jsonify({'city': city, 'confirm': confirm})


@app.route('/l1')
def get_l1_data():
    # 获取累计新增、疑似、治愈、死亡人数
    data = utils.get_l1_data()
    day, confirm, suspect, heal, dead = [], [], [], [], []
    for a, b, c, d, e in data[7:]:  # 前七天为0,去掉前7天,从1.20号开始获取数据
        day.append(a.strftime('%m-%d'))  # a是datatime类型
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({'day': day, 'confirm': confirm, 'suspect': suspect, 'heal': heal, 'dead': dead})


@app.route('/l2')
def get_l2_data():
    # 获取每日新增确诊、疑似人数
    data = utils.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:  # 前七天为0,去掉前7天,从1.20号开始获取数据
        day.append(a.strftime('%m-%d'))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({'day': day, 'confirm_add': confirm_add, 'suspect_add': suspect_add})


@app.route('/r2')
def get_r2_data():
    # 获取国外确诊人数最多的10个国家
    data = utils.get_r2_data()
    country, confirm, confirm_add, heal, dead = [], [], [], [], []
    for i in data:
        country.append(i[0])  # 国家
        confirm.append(int(i[1]))  # 累计确诊
        confirm_add.append(int(i[2]))  # 新增确诊
        heal.append(int(i[3]))  # 治愈
        dead.append(int(i[4]))  # 死亡
        # print(country, confirm, confirm_add, heal, dead)
    return jsonify({'country': country, 'confirm': confirm, 'confirm_add': confirm_add, 'heal': heal, 'dead': dead})


@app.route('/world')
def get_world_data():
    # 获取除中国外各国累计确诊人数
    res = []
    for tup in utils.get_world_data():
        # print(tup)
        res.append({'name': tup[0], 'value': int(tup[1])})
    # 获取中国累计确诊人数
    data = utils.get_c1_data()
    res.append({'name': '中国', 'value': int(data[0])})
    return jsonify({'data': res, 'name': nameMap.namemap})


if __name__ == '__main__':
    app.debug = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    app.run()
