from flask import Flask,render_template,send_file
import requests
import os
import csv
import json
#import urllib.request



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jsonParser')
def jsonParser():
    download_url = "https://open-to-cors.s3.amazonaws.com/users.json"
    #response = urllib.request.urlopen("https://open-to-cors.s3.amazonaws.com/users.json")
    #html = response.read()

    r = requests.get(download_url)
    with open("testerss.json","wb") as f:
        f.write(r.content)

    with open('testerss.json') as f:
        x = json.load(f)

    f = csv.writer(open("jsontocsvconverted.csv", "w", newline=''))

    f.writerow(["id", "phones", "email", "firstname", "lastname","role","username","isActive","_created_at","_updated_at"])

    for x in x:
        try:
            f.writerow([x["id"],
                        x["phones"],
                        x["email"],
                        x["firstname"],
                        x["lastname"],
                        x["role"],
                        x["username"],
                        x["isActive"],
                        x["_created_at"],
                        x["_updated_at"]])
        except:
            f.writerow([x["_id"],
                        x["phones"],
                        x["email"],
                        x["firstname"],
                        x["lastname"],
                        x["role"],
                        x["username"],
                        x["isActive"],
                        x["_created_at"],
                        x["_updated_at"]])

    #return send_from_directory(directory='/smartservprojects',filename='testlol.csv', as_attachment=True)
    #return "downloading.."
    #return send_file('/Users/shahzinsajid/SmartServProjects/testlol.csv',attachment_filename='testlol.csv')
    #return render_template('downloads.html')
    return render_template('downloads.html')

@app.route('/return-file/')
def return_file():
    return send_file('/Users/shahzinsajid/SmartServProjects/jsontocsvconverted.csv',attachment_filename='jsontocsvconverted.csv')
    #return "hey"

if __name__ == "__main__":
    app.run(debug=True,threaded=True)
