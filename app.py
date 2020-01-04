from flask import Flask,render_template
from flask import send_file,send_from_directory
import os
import requests
import csv
import json
import sys

app = Flask(__name__)

@app.route('/')
def index():
    #return render_template('index.html')
    return "hey"

@app.route('/return-file/')
def return_file():
    #return send_file('/Users/shahzinsajid/SmartServProjects/jsontocsvconverted.csv',attachment_filename='jsontocsvconverted.csv')
    return "hey"

@app.route('/jsonParser2')
def jsonParser(methods=['GET', 'POST']):
    return "success"



if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    #print('hello', file=sys.stderr)
    app.run()
    
