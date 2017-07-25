"""This script Creates the application object"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from app.models.bucketlist import Bucketlist
from app.models.item import Item

app = Flask(__name__)
app.config.from_object(__name__)
# used to create a cryptographic token that is used to validate a form
app.secret_key = b'\xe1\x1d\x01<\x08\xca\xeb\xf0\x17\xe6\xe8\xa5s&o\xd8\x14\x03\xce\x06\xbck\x9c\xd1'

app.all_users = {}
app.all_bucketlists = {}
app.all_items = {}


@app.route('/')


@app.route('/index', methods=['POST', 'GET'])
def index():
    """renders the homepage of the app"""
    # you can enter the email,password
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if app.all_users[email] and app.all_users[email] == password:
                session['logged_in'] = True
                flash(email, ' you are logged in')
                print(app.all_users)
                return redirect(url_for('create_bucketlist'))
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
        # if email in all_users:
        #     return 'User is registered'
        # else:
        #     if password == password2:
        #         pass
        app.all_users[email] = password
        # saves the new user object to app.user
        session['logged_in'] = True
        return redirect(url_for('index'))
    return render_template('registration.html')

# CRUD for bucketlist
@app.route('/create_list', methods=['GET', 'POST'])
def create_bucketlist():
    """Renders the create bucketlist of the app"""
    if 'logged_in' in session:
        if request.method == 'POST':
            # gets the title and intro
            title = request.form['title']
            intro = request.form['intro']
            # creating an instance of bucket
            new_bucketlist = Bucketlist(title, intro)
            # saving into a dict using _id as key
            app.all_bucketlists[new_bucketlist._id] = new_bucketlist
    else:
        return redirect(url_for('index'))

    return render_template('create_list.html', bucketlist=app.all_bucketlists)


@app.route('/delete_bucket/<_id>')
def delete_bucket(_id):
    """Route deletes a bucketlist """
    # deletes bucketlist using key[_id]
    del app.all_bucketlists[_id]
    return redirect(url_for('create_bucketlist'))


@app.route('/edit_bucket/<_id>', methods=['GET', 'POST'])
def edit_bucket(_id):
    """Route deletes a bucketlist """
    if request.method == 'POST':
        # gets the title and intro
        title = request.form['title']
        intro = request.form['intro']
        
        bucketlist = app.all_bucketlists[_id]
        bucketlist.title = title
        bucketlist.intro = intro
        app.all_bucketlists[_id] = bucketlist
        return redirect(url_for('create_bucketlist'))
    return render_template('edit_bucket.html', bucketlist=app.all_bucketlists[_id])



# CRUD for bucketlist items
@app.route('/create_list', methods=['GET', 'POST'])
def create_item():
    """Renders the create bucketlist of the app"""
    if 'logged_in' in session:
        if request.method == 'POST':
            # gets the item_name and description
            item_name = request.form['item_name']
            description = request.form['description']
            # creating an instance of bucket item
            new_item = Item(item_name, description)
            # saving into a dict using _id as key
            app.all_bucketlists[new_item.bucketlist_id] = new_item
    else:
        return redirect(url_for('index'))

    return render_template('create_list.html', bucketlist=app.all_bucketlists)


# @app.route('/delete_item/<bucketlist_id>')
# def delete_item(bucketlist_id):
#     """Route deletes a bucketlist """
#     # deletes bucketlist using key[_id]
#     del app.all_items[bucketlist_id]
#     return redirect(url_for('create_bucketlist'))


# @app.route('/edit_bucket/<bucketlist_id>', methods=['GET', 'POST'])
# def edit_item(bucketlist_id):
#     """Route deletes a bucketlist """
#     if request.method == 'POST':
#         # gets the title and intro
#         title = request.form['title']
#         intro = request.form['intro']

#         item = app.all_items[bucketlist_id]
#         title = title
#         intro = intro
#         app.all_items[bucketlist_id] = item
#         return redirect(url_for('create_bucketlist'))
#     return render_template('edit_bucket.html', item=app.all_items[bucketlist_id])


@app.route("/logout")
def logout():
    "Logs out a user"
    session['logged_in'] = False
    return redirect(url_for('index'))
