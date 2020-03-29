from flask import Flask
from flask import render_template
from flask import jsonify
from datetime import timedelta
import utils
import nameMap

app = Flask(__name__)

# 更新数据库各表
@app.route('/update_sql')
def update_sql():
    utils.update_history()
    utils.update_details()
    utils.update_fforeign()
    utils.update_global()
    print('数据库更新数据成功')
    return render_template('china.html')


# 主页，中国疫情地图、国内城市排行
@app.route('/')
def hello_index():
    return render_template('china.html')


# 动态刷新时间
@app.route('/get_time')
def get_time():
    # 获取当地时间
    return utils.get_time()


# 获取china左侧数据，中国疫情地图
@app.route('/get_china_left')
def get_china_left():
    # 获取中国各省累计确诊人数
    res = []
    for tup in utils.get_china_left():
        # print(tup)
        res.append({'name': tup[0], 'value': int(tup[1])})
    return jsonify({'data': res})


# 获取china右上侧数据，疫情数据
@app.route('/get_china_top_right')
def get_china_top_right():
    # 获取累计确诊疑似、治愈、死亡人数
    data, import_confirm, import_confirm_add = utils.get_china_top_right()
    return jsonify({'confirm': int(data[0]), 'heal': int(data[2]), 'dead': int(data[3]), 'confirm_add': int(data[1]),
                    'import_confirm': int(import_confirm), 'import_confirm_add': int(import_confirm_add)})


# 获取china右下侧数据，城市排行
@app.route('/get_china_bottom_right')
def get_china_bottom_right():
    # 获取除湖北省外累计确诊最多的10个城市
    data = utils.get_china_bottom_right()
    city, confirm = [], []
    for i in data:
        city.append(i[0])  # 城市
        confirm.append(int(i[1]))  # 累计确诊人数
        # print(city, confirm)
    return jsonify({'city': city, 'confirm': confirm})


# 中国新增、累计确诊趋势，国外累计确诊排行
@app.route('/china-trend')
def china_trend():
    return render_template('china-trend.html')


# 获取china-trend左上侧数据，全国累计趋势
@app.route('/get_china_trend_top_left')
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


# 获取china-trend左下侧数据，全国新增趋势
@app.route('/get_china_trend_bottom_left')
def get_china_trend_bottom_left():
    # 获取每日新增确诊、疑似人数
    data = utils.get_china_trend_bottom_left()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:  # 前七天为0,去掉前7天,从1.20号开始获取数据
        day.append(a.strftime('%m-%d'))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({'day': day, 'confirm_add': confirm_add, 'suspect_add': suspect_add})


# 获取china-trend右侧数据，国家排行
@app.route('/get_china_trend_right')
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
    return jsonify({'country': country, 'confirm': confirm, 'confirm_add': confirm_add, 'heal': heal, 'dead': dead})


# 世界疫情地图
@app.route('/world')
def world():
    return render_template('world.html')


# 获取world数据，世界疫情地图
@app.route('/get_world')
def get_world():
    res = []
    global_dict = utils.get_world()
    for tup in global_dict:
        # print(tup)
        res.append({'name': tup, 'value': global_dict[tup]})
    # 获取中国累计确诊人数
    china_data = utils.get_china_top_right()[0]
    res.append({'name': '中国', 'value': int(china_data[0])})
    return jsonify({'data': res, 'name': nameMap.namemap})


# 获取world-trend数据，世界趋势
@app.route('/world-trend')
def world_trend():
    return render_template('world-trend.html')


# 国外累计确诊、新增确诊、累计死亡、累计治愈数据
@app.route('/get_world_trend')
def get_world_trend():
    # 获取国外累计确诊、新增确诊、累计治愈、累计死亡人数
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
