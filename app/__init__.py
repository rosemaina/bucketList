"""This script Creates the application object"""
from flask import Flask

app = Flask(__name__)

from app import views