#!/usr/bin/python3

__author__ = "Brandon Rickman <brandon.rickman@snhu.edu>"
__version__ = "0.1.0"
__title__ = "Biz System Ops RESTful API"
__license__ = "MIT"


import datetime, json
from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo 
from documents import Document
from bson import json_util


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/city.db"
mongo = PyMongo(app)

'''
# Database connection and selection
connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']
'''


@app.route('/')
def home():
	bizName = mongo.db.inspections.find({'business_name': 'New ACME Explozives'})
	return render_template('index.html', bizName=bizName)


@app.route('/currentTime', methods=['GET'])
def get_currentTime():
	dateString = datetime.datetime.now().strftime('%Y-%m-%d')
	timeString = datetime.datetime.now().strftime('%H:%M:%S')
	string = '{ date : ' + dateString + ', time : ' + timeString + ' }'
	return json.loads(json.dumps(string, indent=4, default=json_util.default))


@app.route('/read/<ID>', methods=['GET'])
def getDocument(ID):
	read = mongo.db.inspections
	doc = read.find_one({ 'id' : ID })
	return jsonify({'result' : doc})


if __name__ == '__main__':
	app.run(debug=True, reloader=True)