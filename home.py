from flask import Blueprint, render_template

hm = Blueprint('home', __name__, url_prefix='/home')


def render_page(template_name):
    return render_template(template_name)

@hm.route("/login")
def login():
    return render_page('login_page.html')


@hm.route("/pages")
def pages():
    return render_page('pages.html')


@hm.route("/result")
def result():
    return render_page('result.html')

@hm.route("/blockpage")
def blockpage():
    return render_page('blockpage.html')