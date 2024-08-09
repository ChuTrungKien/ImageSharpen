from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

# init Flask server:
app = Flask(__name__)

# apply:
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# root:
@app.route('/add', methods=['POST'])
@cross_origin(origins='*')
def add_process():
    a = int(request.form.get('x'))
    b = int(request.form.get('y'))
    return "Add Func: " + str(a + b)


@app.route('/minus', methods=['POST', 'GET'])
@cross_origin(origins='*')
def minus_process():
    return "Minus Func"


@app.route('/multi', methods=['POST', 'GET'])
@cross_origin(origins='*')
def multi_process():
    return "Multi Func"


@app.route('/div', methods=['POST', 'GET'])
@cross_origin(origins='*')
def div_process():
    return "Div Func"


# start:
if __name__ == '__main__':
    app.run(port=6868, host='0.0.0.0')
