from flask import Flask, render_template, request
from pymongo import MongoClient
from bson.objectid import ObjectId
import csv
import json

app = Flask(__name__)
mongodb = MongoClient('mongodb').lottery_db
documentid = ''

@app.route("/table", methods=["GET"])
def show_tables():
    data = parseCSV('temp.csv')
    print (data[0]["Name"])
    return render_template('index.html', my_list=data)

@app.route("/", methods=["POST", "GET"])
def index():
    args = {"method": "GET"}
    if request.method == "POST":
        file = request.files["file"]
        if bool(file.filename):
            file_bytes = file.read()
            writeCSV('temp.csv',file_bytes)
            data = parseCSV('temp.csv')
            documentid = mongoWrite('participants',{"devops_list": data}).inserted_id
            return render_template('index.html', my_list=mongoRead('participants',documentid)['devops_list'],)
        args["method"] = "POST"
    return render_template("index.html", args=args)

def mongoWrite(collection,doc):
    return mongodb[collection].insert_one(doc)

def mongoRead(collection,id):
    return mongodb[collection].find_one({'_id': ObjectId(id)})

    # return obj

def writeCSV(filename,bytes):
    ofile  = open(filename, "wb")
    ofile.write(bytes)
    ofile.close()

def parseCSV(csvfile):
    jsonform = []
    fields = ["Name" , "Email"]
    with open(csvfile, 'r') as file:
        reader = csv.DictReader(file, fieldnames=fields)
        for i, row in enumerate(reader):
            row['id'] = i
            jsonform.append(row)
    return jsonform

if __name__ == "__main__":
    app.run(host= '0.0.0.0',debug=True)
