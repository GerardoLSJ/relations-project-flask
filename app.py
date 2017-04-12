from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()