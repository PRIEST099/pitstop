from pitstop import app
from flask import render_template


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/test')
def test_code():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)