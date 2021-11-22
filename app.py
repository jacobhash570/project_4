from flask import Flask, json, redirect, jsonify, render_template
import pandas as pd


#Initiate Flask app
app = Flask(__name__)


#Handle the default route and render the index.html
@app.route('/')
def home():
    return render_template('index.html')

    #Run the flask server in Production mode. 
#Tried running the server in debug mode and that never works
if __name__ == '__main__':
    app.run(debug=False)