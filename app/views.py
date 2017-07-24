"""This script Creates the application object"""
from flask import Flask, render_template, request, redirect, url_for, session
from app.models.user import User

app = Flask(__name__)
app.config.from_object(__name__)
# used to create a cryptographic token that is used to validate a form
app.secret_key = 'muthundo'

app.users = {}
app.bucketlists = {}
app.items = {}


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    """renders the homepage of the app"""
    # you can enter the email,password
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email in app.users:
            if password == app.users[email].password:
                # marks user as logged-in
                session['logged_in'] = True

                #redirects one to the create list page
                return redirect(url_for('create_list'))
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    """renders the registration page of the app"""
    # you can enter the email,password
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
        if password == password2:
            # created a new user
            new_user = User(username, email, password)

            # saves the new user object to app.user
            app.users[email] = new_user
            session['logged_in'] = True
            return redirect(url_for('create_list'))
    return render_template('registration.html')


@app.route('/create_list', methods=['GET', 'POST'])
def create_list():
    """Renders the create bucketlist of the app"""
    return render_template('create_list.html')
