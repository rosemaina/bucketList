"""This script Creates the application object"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from app.models.user import User

app = Flask(__name__)
app.config.from_object(__name__)
# used to create a cryptographic token that is used to validate a form
app.secret_key = 'muthundo'

all_users = {}

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    """renders the homepage of the app"""
    # you can enter the email,password
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        try:
            if all_users[email] and all_users[email] == password:
                session['logged_in'] = True
                flash(email, ' you are logged in')
                return redirect(url_for('create_list'))
            else:
                error = 'Wrong password!'
                return render_template('index.html', error=error)

        except KeyError:
            error = 'User does not exist'
            return render_template('index.html', error=error)
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    """renders the registration page of the app"""
    # you can enter the email,password
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # password2 = request.form['password2']
        # if password == password2:
            # created a new user
        all_users[email] = password
            # saves the new user object to app.user
        session['logged_in'] = True
        return redirect(url_for('index'))
    return render_template('registration.html')


@app.route('/create_list', methods=['GET', 'POST'])
def create_list():
    """Renders the create bucketlist of the app"""

    return render_template('create_list.html')


@app.route("/logout")
def logout():
    "Logs out a user"
    session['logged_in'] = False
    return redirect(url_for('index'))

