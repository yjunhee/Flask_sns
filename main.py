from flask import Flask, render_template
import blue, home, users

app = Flask(__name__)
app.register_blueprint(blue.bp)
app.register_blueprint(home.hm)
app.register_blueprint(users.user)


@app.route('/')
def home():
    return render_template('home.html')




if __name__ == '__main__':
    app.run(debug=True)
