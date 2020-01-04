from flask import Flask,render_template
from flask import send_file,send_from_directory
import requests
import csv
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/return-file/')
def return_file():
    #return send_file('/Users/shahzinsajid/SmartServProjects/jsontocsvconverted.csv',attachment_filename='jsontocsvconverted.csv')
    return "hey"

@app.route('/jsonParser')
def jsonParser(methods=['GET', 'POST']):
    


    download_url = "https://open-to-cors.s3.amazonaws.com/users.json"
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
    return render_template('downloads.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
