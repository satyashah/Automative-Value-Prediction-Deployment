import pandas as pd
import numpy as np
import random

dataDict = {'miles': '76766', 'year': '2014', 'make': 'Nissan', 'model': 'Altima', 'transmission': 'automatic', 'drive': '4WD', 'exteriorColor': 'Black', 'interiorColor': 'Black', 'mileage': '26', 'engineSize': '2.5', 'engineCylinders': '6'}
def find_nearest(array, value):
	array = np.asarray(array)
	idx = (np.abs(array - value)).argmin()
	return array[idx]
	
def sims(data):
	make = data["make"]
	model = data["model"]
	year = data["year"]
	carDF = pd.read_csv("static/carData.csv")
	makeDF = carDF[carDF["make"] == make]
	modelDF = makeDF[makeDF["model"] == model]
	yearDF = modelDF[modelDF["year"] == int(year)]

	miles = np.array(yearDF["miles"].values)

	if len(miles)>0:
		nearestVal = find_nearest(miles, float(data["miles"]))
	
		ind = np.where(miles == nearestVal)
	
		bestPrice = yearDF["displayPrice"].values[ind[0][0]]
	else:
		bestPrice = random.randint(17000, 21000)
	return bestPrice
