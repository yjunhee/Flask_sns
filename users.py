from flask import Blueprint, request, render_template
from flask_sqlalchemy import SQLAlchemy 

user = Blueprint('users', __name__, url_prefix='/users')

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200))


@user.route('/userpage', methods=['Get','POST'])
def update_username():
    global username
    username = str(request.form.get('Id', 'guest'))
    password = request.form.get('userPassword', 'None')

    if username == "admin":
        return render_template('admin.html')
    else:
        return render_template('user_page.html', username=username, password=password)