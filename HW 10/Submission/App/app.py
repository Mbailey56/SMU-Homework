import datetime as dt
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper()

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"""Welcome to the Best Hawaii Weather API!<br>
        <a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a>
        <a href='/api/v1.0/tobs'>/api/v1.0/tobs</a>
        <a href='/api/v1.0/stations'>/api/v1.0/stations</a>
        <a href='/api/v1.0/start'>/api/v1.0/<start</a>
        <a href='/api/v1.0/<start>/<end>'>/api/v1.0/<start>/<end></a>
        """
    )

@app.route("/api/v1.0/precipitation")
def get_precipitation():
    df = sqlHelper.getPrecipitation()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/tobs")
def getTempDataSinceDate():
    df = sqlHelper.getTempDataSinceDate()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def get_stations():
    df = sqlHelper.getStations()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>")
def get_temp_data_since_date(start):
    df = sqlHelper.getTempDataSinceDate(start)
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>/<end>")
def get_temp_data_for_date_range(start, end):
    df = sqlHelper.getTempDataForDateRange(start, end)
    data = df.to_dict(orient="records")
    return(jsonify(data))

if __name__ == "__main__":
    app.run(debug=True)
