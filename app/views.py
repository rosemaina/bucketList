"""This script Creates the application object"""
from flask import Flask, render_template, request, redirect, url_for, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__) 
app.config.from_object(__name__)

class ReusableForm(Form):
    username = TextField('username:',validators=[validators.required()])
    email = TextField('email:', validators=[validators.required(), validators.Length(min=6, max=16)])
    password = TextField('password:', validators=[validators.required(), validators.Length(min=4, max=16)])


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    """renders the homepage of the app"""
    #this will get you the variables when someone submits
    #the form since we have set our forms method to POST
    data = {'host_url': request.host_url}
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    return render_template('index')


@app.route('/registration')
def registration():
    """renders the registration page of the app"""

    form = ReusableForm(request.form)
    print (form.errors)
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print (username, " ", email, " ", password)

        if form.validate():
            flash('Thanks for registration' + username)
        else:
            flash('Error:Unaswered form field. ')
    return render_template('registration', form=form)


@app.route('/create_list')
def create_list():
    """Renders the create bucketlist of the app"""
    return render_template('create_list')
