from flask import Flask, render_template 
import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
import os 



# df = pd.read_csv("anaemia.csv")
# data = df.to_json(orient='records')

# create app 
app = Flask(__name__)



# page routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard.html")
def dashboard():
    return render_template("dashboard.html")

@app.route("/forecast.html")
def forecast():
    return render_template("forecast.html")


@app.route("/api/data")
def data():
    df = pd.read_csv("https://anaemia-app-bucket-01.s3.ap-southeast-2.amazonaws.com/anaemia.csv")
    data = df.to_dict(orient = 'records')
    return {'data':data}



@app.route("/api/predict")
def predict():
    df = pd.read_csv("https://anaemia-app-bucket-01.s3.ap-southeast-2.amazonaws.com/anaemia_forecast.csv")
    data = df.to_dict(orient = 'records')
    return {'data':data}





if __name__ == "__main__":
    app.run(debug=True)
