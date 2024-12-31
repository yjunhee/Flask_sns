from flask import Blueprint, request, render_template
login = Blueprint('login', __name__, url_prefix='/login')


username = 'Default'
users = {
    "123" : "123"
}

@login.route('/check', methods=['POST'])
def login():
    Id = request.form.get('id')
    Password = request.form.get('password')
    return render_template('user_page.html', username= username)