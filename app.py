from flask import Flask
import requests
import os
import csv
#import urllib.request



app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

@app.route('/jsonParser')
def jsonParser():
    download_url = "https://open-to-cors.s3.amazonaws.com/users.json"
    #response = urllib.request.urlopen("https://open-to-cors.s3.amazonaws.com/users.json")
    #html = response.read()

    r = requests.get(download_url)
    return "successfully downloaded"



if __name__ == "__main__":
    app.run(debug=True,threaded=True)
