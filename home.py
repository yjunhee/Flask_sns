from flask import Blueprint, render_template

hm = Blueprint('home', __name__, url_prefix='/home')


@hm.route("/login")
def login():
    return render_template('login_page.html')


@hm.route("/pages")
def pages():
    return render_template('pages.html')


@hm.route("/result")
def result():
    return render_template('result.html')

@hm.route("/blockpage")
def blockpage():
    return render_template('blockpage.html')