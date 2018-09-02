from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def runit():
    return render_template('index.html')

@app.route('/signup.html')
def signup():
    return render_template('signup')

if __name__ == '__main__':
    app.run()