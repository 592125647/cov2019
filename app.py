from flask import Flask
from flask import render_template
from flask import jsonify
from datetime import timedelta
import utils
import nameMap

app = Flask(__name__)


@app.route('/')
def hello_index():
    return render_template('china.html')


@app.route('/updatedata')
def update_data():
    utils.update_history()
    utils.update_details()
    utils.update_fforeign()
    utils.update_global()
    print('数据库更新数据成功')
    return render_template('china.html')


@app.route('/time')
def get_time():
    # 获取当地时间
    return utils.get_time()


@app.route('/c2')
def get_china_left():
    # 获取中国各省累计确诊人数
    res = []
    for tup in utils.get_china_left():
        # print(tup)
        res.append({'name': tup[0], 'value': int(tup[1])})
    return jsonify({'data': res})


@app.route('/c1')
def get_china_top_right():
    # 获取累计确诊疑似、治愈、死亡人数
    data = utils.get_china_top_right()
    return jsonify({'confirm': int(data[0]), 'suspect': int(data[1]), 'heal': int(data[2]), 'dead': int(data[3])})


@app.route('/r1')
def get_china_bottom_right():
    # 获取除湖北省外累计确诊最多的10个城市
    data = utils.get_china_bottom_right()
    city, confirm = [], []
    for i in data:
        city.append(i[0])  # 城市
        confirm.append(int(i[1]))  # 累计确诊人数
        # print(city, confirm)
    return jsonify({'city': city, 'confirm': confirm})


@app.route('/trend')
def trend():
    return render_template('china-trend.html')


@app.route('/l1')
def get_china_trend_top_left():
    # 获取累计新增、疑似、治愈、死亡人数
    data = utils.get_china_trend_top_left()
    day, confirm, suspect, heal, dead = [], [], [], [], []
    for a, b, c, d, e in data[7:]:  # 前七天为0,去掉前7天,从1.20号开始获取数据
        day.append(a.strftime('%m-%d'))  # a是datatime类型
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({'day': day, 'confirm': confirm, 'suspect': suspect, 'heal': heal, 'dead': dead})


@app.route('/l2')
def get_china_trend_bottom_left():
    # 获取每日新增确诊、疑似人数
    data = utils.get_china_trend_bottom_left()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:  # 前七天为0,去掉前7天,从1.20号开始获取数据
        day.append(a.strftime('%m-%d'))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({'day': day, 'confirm_add': confirm_add, 'suspect_add': suspect_add})


@app.route('/r2')
def get_china_trend_right():
    # 获取国外确诊人数最多的10个国家
    data = utils.get_china_trend_right()
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
def world():
    return render_template('world.html')


@app.route('/worlddata')
def get_world():
    res = []
    global_dict = utils.get_world()
    for tup in global_dict:
        # print(tup)
        res.append({'name': tup, 'value': global_dict[tup]})
    # 获取中国累计确诊人数
    data = utils.get_china_top_right()
    res.append({'name': '中国', 'value': int(data[0])})
    return jsonify({'data': res, 'name': nameMap.namemap})


@app.route('/country')
def country():
    return render_template('world-trend.html')


@app.route('/worldconfirm')
def get_world_trend():
    # 获取世界累计新增治愈死亡人数
    data = utils.get_world_trend()
    day, confirm, confirm_add, heal, dead = [], [], [], [], []
    for a, b, c, d, e in data:
        day.append(a.strftime('%m-%d'))  # a是datatime类型
        confirm.append(int(b))
        confirm_add.append(int(c))
        heal.append(int(d))
        dead.append(int(e))
    return jsonify({'day': day, 'confirm': confirm, 'confirm_add': confirm_add,  'heal': heal, 'dead': dead})


if __name__ == '__main__':
    app.debug = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    app.run()
