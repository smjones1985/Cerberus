"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask
from Cerberus import app

@app.route('/')
def default():
    return 'hello world'

