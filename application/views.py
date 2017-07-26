"""This script Creates the application object"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from application.models.bucketlist import Bucketlist
from application.models.item import Item

app = Flask(__name__)
app.config.from_object(__name__)
# used to create a cryptographic token that is used to validate a form
app.secret_key = b'nGzc\xd6\x19\x03\x19\x8c\xa4\xed\xe6'

all_users = {}
all_bucketlists = {}
all_items = {}


@app.route('/')


@app.route('/index', methods=['POST', 'GET'])
def login(self):
    """renders the homepage of the app"""
    # you can enter the email,password
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if all_users[email] and all_users[email] == password:
                session['logged_in'] = True
                flash(email, ' you are logged in')
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
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            error = 'Passwords do not match!'
            return render_template('registration.html', error=error)
        all_users[email] = password
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
            # saving into a dict using bucket_id as key
            all_bucketlists[new_bucketlist.bucket_id] = new_bucketlist
    else:
        return redirect(url_for('index'))

    return render_template('create_list.html', bucketlist=all_bucketlists)


@app.route('/delete_bucket/<bucket_id>')
def delete_bucket(bucket_id):
    """Route deletes a bucketlist """
    # deletes bucketlist using key[id]
    del all_bucketlists[bucket_id]
    return redirect(url_for('create_bucketlist'))


@app.route('/edit_bucket/<bucket_id>', methods=['GET', 'POST'])
def edit_bucket(bucket_id):
    """Route deletes a bucketlist """
    if request.method == 'POST':
        # gets the title and intro
        title = request.form['title']
        intro = request.form['intro']
        bucketlist = all_bucketlists[bucket_id]
        bucketlist.title = title
        bucketlist.intro = intro
        all_bucketlists[bucket_id] = bucketlist
        return redirect(url_for('create_bucketlist'))
    return render_template('edit_bucket.html', bucketlist=all_bucketlists[bucket_id])



# CRUD for bucketlist items
@app.route('/create_item/<bucket_id>', methods=['GET', 'POST'])
def create_item(bucket_id):
    """Renders the create bucketlist of the app"""
    if 'logged_in' in session:
        if request.method == 'POST':
            # gets the item_name and description
            item_name = request.form['item_name']
            description = request.form['description']
            # creating an instance of bucket item
            new_item = Item(item_name, description, bucket_id)
            # saving into a dict using id as key
            all_items[new_item.item_id] = new_item
    return render_template('create_item.html', item=all_items, bucket_id=bucket_id)


@app.route('/delete_item/<bucket_id>/<item_id>')
def delete_item(item_id, bucket_id):
    """Route deletes a bucketlist """
    # deletes bucketlist item using key id
    del all_items[item_id]
    # returns create_item with the bucket_id
    return redirect('/create_item/{}'.format(bucket_id))


@app.route('/edit_item/<bucket_id>/<item_id>', methods=['GET', 'POST'])
def edit_item(item_id, bucket_id):
    """Route edits a bucketlist item """
    if request.method == 'POST':
        # gets the title and intro
        item_name = request.form['item_name']
        description = request.form['description']

        item = all_bucketlists[bucket_id]
        item.item_name = item_name
        item.description = description
        all_items[item_id] = item
        return redirect('/create_list')
    return render_template('create_item.html', item=all_items[item_id])


@app.route("/logout")
def logout():
    "Logs out a user"
    session['logged_in'] = False
    return redirect(url_for('index'))
