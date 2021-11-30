from flask import Flask, json, redirect, jsonify, render_template, request
import pandas as pd
import joblib
from sqlalchemy import create_engine

data_for_website = {}
# link to your database
engine = create_engine("postgresql://eyjulbqjgoyzac:7dd513f6edde71ea3a743c2483b5ae84a90dccc9b306e098d8c425513a698bba@ec2-52-73-29-239.compute-1.amazonaws.com:5432/d5taik2sir38ga", echo = False)
#engine = create_engine("postgres://localhost:5432/d9vp4cuu7ce85k", echo = False)


#Initiate Flask app
app = Flask(__name__)


@app.route('/predictPrice', methods=['POST'])
def predictPrice():
	model= joblib.load('finalModel_Hina.joblib')
    
	columns = ['enginelocation', 'carwidth', 'carheight', 'curbweight', 'enginesize', 'car_company']
	carwidth=request.json.get("carWidth")
	curbweight=request.json.get("carWeight")
	enginesize=request.json.get("engineSize")
	enginelocation=engineLocEnumerated(request.json.get("engineLocation"))
	carheight=request.json.get("carHeight")
	carCompany = carNameEnumerated(request.json.get("carCompany"))
	test_data = pd.DataFrame([[enginelocation, carwidth, carheight, curbweight, enginesize, carCompany]], columns=columns)
	pred = model.predict(test_data)
	return {"Prediction": round(pred[0],2)}
#Handle the default route and render the index.html
@app.route('/')
def home():
	
    return render_template('index.html', data= getLookupValues())

    #Run the flask server in Production mode. 
#Tried running the server in debug mode and that never works
def loadCleanedCSVToPostgreSQL():
	cars = pd.read_csv('Resources/cars_cleaned.csv')
	cars.to_sql('cars', engine, if_exists='replace', index = False)
	#return true

def getLookupValues():
	cars = pd.read_csv('Resources/cars_cleaned.csv')
	cars.to_sql('cars', engine, if_exists='replace', index = False)
	carwidthArray= []
	carwidths = engine.execute('select distinct carwidth from cars order by carwidth desc').fetchall()
	carwidths=[i[0] for i in carwidths]
	for carwidth in carwidths:
		carwidthArray.append(carwidth)
	data_for_website['car_widths'] = carwidthArray

	carWeightsArray = []
	carWeights = engine.execute('select distinct curbweight from cars order by curbweight desc').fetchall()
	carWeights=[i[0] for i in carWeights]
	for carWeight in carWeights:
		carWeightsArray.append(carWeight)
	data_for_website['car_weights'] = carWeightsArray

	engineSizeArray = []
	engineSizes = engine.execute('select distinct enginesize from cars order by enginesize desc').fetchall()
	engineSizes=[i[0] for i in engineSizes]
	for engineSize in engineSizes:
		engineSizeArray.append(engineSize)
	data_for_website['engine_sizes'] = engineSizeArray

	engineLocationArray = []
	engineLocations = engine.execute('select distinct enginelocation from cars order by enginelocation desc').fetchall()
	engineLocations=[i[0] for i in engineLocations]
	for engineLocation in engineLocations:
		engineLocationArray.append(engineLocation)
	data_for_website['engine_locations'] = engineLocationArray

	carHeightArray = []
	carHeights = engine.execute('select distinct carheight from cars order by carheight desc').fetchall()
	carHeights=[i[0] for i in carHeights]
	for carHeight in carHeights:
		carHeightArray.append(carHeight)
	data_for_website['car_heights'] = carHeightArray

	carCompanyArray = []
	carCompanys = engine.execute('select distinct car_company from cars order by car_company desc').fetchall()
	carCompanys=[i[0] for i in carCompanys]
	for carCompany in carCompanys:
		carCompanyArray.append(carCompany)
	data_for_website['car_companys'] = carCompanyArray

	return data_for_website



def checkIfLookupDataisLoaded():
	return true

def engineLocEnumerated(engineLoc):
	if engineLoc == "front":
		return 1
	else:
		return 2

def carNameEnumerated(carName):
	if carName == 'toyota':
		return 1
	elif carName == 'nissan':
		return 2
	elif carName == 'mazda':
		return 3
	elif carName == 'mitsubishi':
		return 4
	elif carName == 'honda':
		return 5
	elif carName == 'volkswagen':
		return 6
	elif carName == 'subaru':
		return 7
	elif carName == 'peugeot':
		return 8
	elif carName == 'volvo':
		return 9
	elif carName == 'dodge':
		return 10
	elif carName == 'buick':
		return 11
	elif carName == 'bmw':
		return 12
	elif carName == 'audi':
		return 13
	elif carName == 'plymouth':
		return 14
	elif carName == 'saab':
		return 15
	elif carName == 'porsche':
		return 16
	elif carName == 'isuzu':
		return 17
	elif carName == 'jaguar':
		return 18
	elif carName == 'chevrolet':
		return 19
	elif carName == 'alfa-romero':
		return 20
	elif carName == 'renault':
		return 21
	elif carName == 'mercury':
		return 22
	else:
		return 1





if __name__ == '__main__':
    app.run(debug=False)