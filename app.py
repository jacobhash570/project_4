from flask import Flask, json, redirect, jsonify, render_template
import pandas as pd
from sqlalchemy import create_engine

data_for_website = {}
# link to your database
engine = create_engine("postgresql://xsuqpfznpphjhp:cb6bee46fb171cabc3c2611382c2589f5be919bdac4a9ed68a8b1c78ebfb2645@ec2-3-231-112-124.compute-1.amazonaws.com:5432/d9vp4cuu7ce85k", echo = False)


#Initiate Flask app
app = Flask(__name__)



#Handle the default route and render the index.html
@app.route('/')
def home():
	
    return render_template('index.html', data= getLookupValues())

    #Run the flask server in Production mode. 
#Tried running the server in debug mode and that never works
def loadCleanedCSVToPostgreSQL():
	cars = pd.read_csv('Resources/cars_cleaned.csv')
	cars.to_sql('cars', engine, if_exists='replace', index = False)
	return true

def getLookupValues():
	loadCleanedCSVToPostgreSQL
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

	carCompanyArray = []
	carCompanys = engine.execute('select distinct car_company from cars order by car_company desc').fetchall()
	carCompanys=[i[0] for i in carCompanys]
	for carCompany in carCompanys:
		carCompanyArray.append(carCompany)
	data_for_website['car_companys'] = carCompanyArray

	return data_for_website



def checkIfLookupDataisLoaded():
	return true

	
if __name__ == '__main__':
    app.run(debug=False)