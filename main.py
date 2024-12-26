from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/main')
def main():
    return render_template("main.html")


@app.route('/login')
def login():
    return render_template("login_page.html")


@app.route('/pages')
def pages():
    return render_template("pages.html")


if __name__ == '__main__':
    app.run(debug=True)
