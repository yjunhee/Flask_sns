from flask import Blueprint, request, render_template
user = Blueprint('users', __name__, url_prefix='/users')


username = 'Default'


@user.route('/update_username', methods=['POST'])
def update_username():
    global username
    username = request.form.get('text')
    return render_template('user_page.html', username= username)