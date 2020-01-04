from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

@app.route('/jsonParser')
def jsonParser(methods=['GET', 'POST']):
    #download_url = "https://open-to-cors.s3.amazonaws.com/users.json"
    #r = requests.get(download_url)
    return "successfully downloaded"



if __name__ == "__main__":
    app.run(debug=True)
