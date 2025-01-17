from flask import Blueprint, request, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from usersql import User

DATABASE_URL = "sqlite:///user_state.db"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

user = Blueprint('users', __name__, url_prefix='/users')

@user.route('/userpage', methods=['Get','POST'])
def update_username():
    global username
    username = str(request.form.get('Id', 'guest'))
    password = request.form.get('userPassword', 'None')
    new_user = User(password = password, username = username)
    session.add(new_user)
    session.commit()
    if username == "admin":
        return render_template('admin.html')
    else:
        return render_template('user_page.html', username=username, password=password)