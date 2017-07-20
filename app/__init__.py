"""This script Creates the application object"""
from app.models.user import User
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """renders the homepage of the app"""
    return render_template('index.html')

@app.route('/registration')
def registration():
    """renders the registration page of the app"""
    user = {
        "email": "jdoe@email",
        "password": "4444",
        "confirm_password": "4444"
        }

    return render_template('registration.html', user=user)


@app.route('/create_list')
def create_list():
    """Renders the create bucketlist of the app"""
    return render_template('create_list.html')
