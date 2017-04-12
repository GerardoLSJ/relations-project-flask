from flask import Flask, render_template, request, jsonify
from relaciones import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/<name>')
def hello_name(name):
    return jsonify(asdf=name)

@app.route('/api', methods=['POST'])
def api():
    data  = request.get_json(force=False, silent=False, cache=False)
    print(data)
    initMatrix(data)
    return jsonify(yourData=data)


if __name__ == '__main__':
    app.run()