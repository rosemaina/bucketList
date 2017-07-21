"""This script Creates the application object"""
from flask import Flask, render_template, request, redirect, url_for
from app.models.user import User

app = Flask(__name__)
app.config.from_object(__name__)

app.users = {}
app.bucketlists = {}
app.items = {}


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    """renders the homepage of the app"""
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    """renders the registration page of the app"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        new_user = User(username, email, password)
        # saves the new user object to app.user
        app.users[username] = new_user

        return redirect(url_for('/registration'))

    return render_template('registration.html')


@app.route('/create_list')
def create_list():
    """Renders the create bucketlist of the app"""
    return render_template('create_list.html')
