from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fires')
def features():
    return render_template('fires.html')

@app.route('/floods')
def pricing():
    return render_template('floods.html')

@app.route('/earthquakes')
def blog():
    return render_template('earthquakes.html')
