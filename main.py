from flask import Flask, render_template
import home, users

app = Flask(__name__)

app.register_blueprint(home.hm, url_prefix='/home')
app.register_blueprint(users.user, url_prefix='/users')


@app.route('/')
def main():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=5500)