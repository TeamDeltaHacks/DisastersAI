from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/fires', methods=['GET', 'POST'])
def fires():
	if request.method == 'POST':
		print(request.form)
		return render_template('fires.html')
	else:
		return render_template('fires.html')

@app.route('/hurricanes', methods=['GET', 'POST'])
def hurricanes():
	if request.method == 'POST':
		print(request.form)
		return render_template('hurricanes.html')
	else:
		return render_template('hurricanes.html')

@app.route('/earthquakes', methods=['GET', 'POST'])
def earthquakes():
	if request.method == 'POST':
		print(request.form)
		return render_template('earthquakes.html')
	else:
		return render_template('earthquakes.html')