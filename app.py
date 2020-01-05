from flask import Flask,render_template,send_file,request
import requests
import os
import csv
import json
#import urllib.request



app = Flask(__name__,template_folder='templates')

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) #this gets us to SRC

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/import/')
def importe():
    return render_template('import.html')

@app.route('/upload',methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT,'textcsv/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target,"ourfile.csv"])
        print(destination)
        file.save(destination)

    return render_template('complete.html')

@app.route('/readng')
def readng():
    target = os.path.join(APP_ROOT,"textcsv/ourfile.csv")
    log = open(target,"r")
    output=''
    for line in log:
        output=output+line
    return output
    
    

@app.route('/jsonParser')
def jsonParser():
    download_url = "https://open-to-cors.s3.amazonaws.com/users.json"
    #response = urllib.request.urlopen("https://open-to-cors.s3.amazonaws.com/users.json")
    #html = response.read()

    r = requests.get(download_url)
    #with open("testerss.json","wb") as f:
      #  f.write(r.content)

   # with open('testerss.json') as f:
    x = json.loads(r.content)
   # return x
    #f = csv.writer(open("jsontocsvconverted.csv", "w", newline=''))
    
    
    outputArray =  ["id", "phones", "email", "firstname", "lastname","role","username","isActive","_created_at","_updated_at"]
    output = ','.join(outputArray)
    i = 0
    #return output
    for x in x:
        #try:
            #return x["id"]
        try:
            idValue = x["id"] or x["_id"]
           # if type(idValue) == <type 'int'>:
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
            
        #output = output + "\n' + output2 

        output =  output + "<br>" + output2 #'\n'.join([output, output2])
        i = i + 1
            
          
       # except:
                #return x["_id"]
                #return  ",".join([x["_id"],
                        #x["phones"] or "",
                        #x["email"] or "",
                        #x["firstname"] or "",
                        #x["lastname"] or "",
                        #x["role"] or "",
                        #x["username"] or "",
                        #x["isActive"] or "",
                        #x["_created_at"] or ""
                       # x["_updated_at"] or "" ]
                        #])

    #return send_from_directory(directory='/smartservprojects',filename='testlol.csv', as_attachment=True)
    #return "downloading.."
    #return send_file('/Users/shahzinsajid/SmartServProjects/testlol.csv',attachment_filename='testlol.csv')
    #return render_template('downloads.html')
    return output
    #return render_template('downloads.html')
    #return "hey"

@app.route('/return-file/')
def return_file():
    return send_file('/Users/shahzinsajid/SmartServProjects/jsontocsvconverted.csv',attachment_filename='jsontocsvconverted.csv')
    #return "hey"

if __name__ == "__main__":
    app.run(debug=True,threaded=True)
