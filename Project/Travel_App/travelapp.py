from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/login")
def hello():
    return "<h1>About Page!</h1>"

@app.route("/travel")
def hello():
    return "<h1>Travel Page</h1>"


if __name__ = '__main__':
    app.run(debug=True)