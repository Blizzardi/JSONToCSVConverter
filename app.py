from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

@app.route('/jsonParser')
def jsonParser(methods=['GET', 'POST']):
    return "successfully downloaded"



if __name__ == "__main__":
    app.run(debug=True)
