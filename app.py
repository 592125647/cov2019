from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from datetime import timedelta
import utils

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/ajax', methods=['get', 'post'])
def ajax():
    name = request.values.get('name')
    score = request.values.get('score')
    print(f'name:{name}, score:{score}')
    return '10000'


@app.route('/time')
def get_time():
    # print(utils.get_time())
    return utils.get_time()


@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({'confirm': int(data[0]), 'suspect': int(data[1]), 'heal': int(data[2]), 'dead': int(data[3])})


@app.route('/c2')
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        # print(tup)
        res.append({'name': tup[0], 'value': int(tup[1])})
    return jsonify({'data': res})


@app.route('/test')
def test():
    # print(utils.get_time())
    return render_template('test.html')


if __name__ == '__main__':
    app.debug = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    app.run()
