"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask
from Cerberus import app
from Cerberus import Garage



@app.route('/status')
def status():
    garageObj = Garage.Garage
    return garageObj.checkStatus()


@app.route('/activate')
def activate():
    garageObj = Garage.Garage
    return garageObj.activateGarage()
