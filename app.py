from flask import Flask, render_template, request, jsonify
from relaciones import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    data  = request.get_json(force=False, silent=False, cache=False)
    print(data)
    arr = []
    for pair in data:
        pair = pair.split(',')
        arr.append(pair)

    results = initMatrix(arr)
    return jsonify(data=results)


if __name__ == '__main__':
    app.run()