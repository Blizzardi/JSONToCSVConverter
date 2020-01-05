from flask import Flask,render_template,send_file
import requests
import os
import csv
import json
#import urllib.request



app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jsonParser')
def jsonParser():
    download_url = "https://open-to-cors.s3.amazonaws.com/users.json"
  
    r = requests.get(download_url)
    x = json.loads(r.content)
    outputArray =  ["id", "phones", "email", "firstname", "lastname","role","username","isActive","_created_at","_updated_at"]
    output = ','.join(outputArray)
    i = 0
        try:
            idValue = x["id"] or x["_id"]
            idValue = str(idValue)
        except:
            idValue = x["_id"] or "nil"

        output2 =   ",".join([ idValue ,
                        x["phones"] or "nil",
                        x["email"] or "nil",
                        x["firstname"] or "nil",
                        x["lastname"] or "nil",
                        str(x["role"]) or "nil",
                        x["username"] or "nil",
                       str(x["isActive"]) or "nil" ,
                        
                        str(x["_created_at"]) or "",
                        str(x["_updated_at"]) or ""]) 
        output =  output + "<br>" + output2 #'\n'.join([output, output2])
        i = i + 1
            
    return output
    #return send_from_directory(directory='/smartservprojects',filename='testlol.csv', as_attachment=True)
    #return "downloading.."
    #return send_file('/Users/shahzinsajid/SmartServProjects/testlol.csv',attachment_filename='testlol.csv')
    #return render_template('downloads.html')
    #return render_template('downloads.html')
    

@app.route('/return-file/')
def return_file():
    return send_file('/SmartServProjects/jsontocsvconverted.csv',attachment_filename='jsontocsvconverted.csv')

if __name__ == "__main__":
    app.run(debug=True,threaded=True)
