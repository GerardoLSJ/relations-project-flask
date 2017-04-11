from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello motherfucker. Sebastián is in the house"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()