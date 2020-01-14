from flask import Flask,render_template,send_file,request,Response
from io import StringIO
import requests
import os
import csv
import json
import pandas as pd



new = ""
x=[]
app = Flask(__name__,template_folder='templates')

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) #this gets us to SRC


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yoyo')
def yoyo():
    return request.form['right_list']


@app.route('/import/')
def importe():
    return render_template('import.html')

@app.route('/checkbox/')
def checkbox():
    return render_template('checkbox.html')

@app.route('/table/')
def tablee():
    return render_template('table.html')

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
        output=output+line #  
        output=output+"<br>"

    usecolz=['firstname', 'lastname','phones','email','role','isActive']
    length_usecols = len(usecolz)
    myVar = pd.read_csv(target, sep = ",",usecols=usecolz)[usecolz]
   

    y = myVar.columns 
 
    z = myVar.values.T.tolist()
    print(z)
    
    length = len(z)
    
   
    lengthofx=len(myVar.values.T.tolist()[0])
    print(lengthofx)
    return render_template('table.html',x=myVar.values.T.tolist(),y=y,length=length_usecols,lengthofx=lengthofx)


    
    
    

@app.route('/jsonParser')
def jsonParser():
    download_url = "https://open-to-cors.s3.amazonaws.com/users.json"
    r = requests.get(download_url)
    x = json.loads(r.content)
    outputArray =  ["id", "phones", "email", "firstname", "lastname","role","username","isActive","_created_at","_updated_at"]
    output = ','.join(outputArray)
    i = 0
    
    for x in x:
     
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
        output =  output + "\n" + output2
        i = i + 1
        
    string_out = StringIO()
    string_out.write(output)
    returnfile = string_out.getvalue()
    return Response(returnfile, mimetype="text/plain", headers={"Content-disposition": "attachment; filename=output.txt"})
    
@app.route('/return-file/')
def return_file():
    return send_file('/Users/shahzinsajid/SmartServProjects/jsontocsvconverted.csv',attachment_filename='jsontocsvconverted.csv')
 

if __name__ == "__main__":
    app.run(debug=True,threaded=True)
