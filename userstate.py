from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User():
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

print(User)
print(1)