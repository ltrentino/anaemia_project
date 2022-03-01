from flask import Flask, render_template 
# import pandas as pd
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

# @app.route("/api.html")
# def api():
#     return render_template("api.html")




if __name__ == "__main__":
    app.run(debug=True)
