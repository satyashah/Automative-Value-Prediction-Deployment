import os
from results import get
from getSims import sims
from flask import Flask, request, render_template
# from os import system
# system("pkill -9 python")



app = Flask(__name__) 
@app.route('/') 
def index(): 
  return render_template('landingPage.php')

@app.route('/inputs') 
def inputs(): 
  return render_template('inputPage.php')

@app.route('/results', methods=['post', 'get'])
def res():
	dataDict = {}

	components =["miles","year","make","model","transmission","drive","exteriorColor","interiorColor","mileage","engineSize","engineCylinders"]

	for component in components:
		dataDict[component] = request.form.get(component)

	# print(dataDict)

	
	price = sims(dataDict)
	
	return render_template('resultsPage.php', message=price)

app.run('0.0.0.0',8080) 