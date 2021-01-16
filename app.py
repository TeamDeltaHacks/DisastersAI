from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from joblib import dump, load
import tensorflow as tf
import keras
from keras.models import load_model
import pandas as pd

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

tsunami_model = load('tsunami_model.joblib')
magnitude_model = load('magnitude_model.joblib')
putout_model = load('putout_model.joblib')
hurricane_nodel = load_model('hurricane-weights.h5')
wildfire_model = load_model('wildfire-weights.h5')


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/fires', methods=['GET', 'POST'])
def fires():
	if request.method == 'POST':
		if(request.form["type"] == "1"):
			if 'image' not in request.files:
				return render_template('fires.html', output="File not found! Please try re-uploading.")
			f = request.files["image"]
			if f.filename == '':
				return render_template('fires.html', output="File not found! Please try re-uploading.")
			if f and allowed_file(f.filename):
				filename = secure_filename(f.filename)
				f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				return render_template('fires.html', output="Output: 0")
			return render_template('fires.html', output="An unknown error occurred!")
		else:
			return render_template('fires.html', output="Coming soon!")
	else:
		return render_template('fires.html', output="")

@app.route('/hurricanes', methods=['GET', 'POST'])
def hurricanes():
	if request.method == 'POST':
		if(request.form["type"] == "0"):
			if 'image' not in request.files:
				return render_template('hurricanes.html', output="File not found! Please try re-uploading.")
			f = request.files["image"]
			if f.filename == '':
				return render_template('hurricanes.html', output="File not found! Please try re-uploading.")
			if f and allowed_file(f.filename):
				filename = secure_filename(f.filename)
				f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				return render_template('hurricanes.html', output="Output: 0")
			return render_template('hurricanes.html', output="An unknown error occurred!")
		else:
			return render_template('hurricanes.html', output="Coming soon!")
	else:
		return render_template('hurricanes.html', output="")

@app.route('/earthquakes', methods=['GET', 'POST'])
def earthquakes():
	if request.method == 'POST':
		print(request.form)
		if(request.form["type"] == "0"):
			output = ""
			try:
				longitude = float(request.form["longitude"])
				latitude = float(request.form["latitude"])
				
				assert (longitude >= -90)
				assert (longitude <= 90)
				assert (latitude >= -180)
				assert (latitude <= 180)
				
				mag_data = {'longitude': [longitude], 'latitude': [longitude]}
				mag_dataf = pd.DataFrame(data=mag_data)
				result = str(round(magnitude_model.predict(mag_dataf)[0], 2))
				output = "Output: " + result + " on the Richter scale"
				
			except Exception as e:
				print(e)
				output = "Invalid inputs!"
			return render_template('earthquakes.html', output=output)
		else:
			output = ""
			try:
				longitude = float(request.form["longitude"])
				latitude = float(request.form["latitude"])
				
				assert (longitude >= -90)
				assert (longitude <= 90)
				assert (latitude >= -180)
				assert (latitude <= 180)
				
				month = int(request.form["month"])
				day = int(request.form["day"])
				deaths = int(request.form["deaths"])
				
				tsunami_data = {'LONGITUDE': [longitude], 'LATITUDE': [longitude], 'MONTH': [month], 'DAY': [day], 'DEATHS': [deaths]}
				tsunami_dataf = pd.DataFrame(data=tsunami_data)
				result = str(tsunami_model.predict(tsunami_dataf)[0] * 100)
				output = "Output: " + result + "% chance of a tsunami"
			
			except Exception as e:
				print(e)
				output = "Invalid inputs!"
			return render_template('earthquakes.html', output=output)
	else:
		return render_template('earthquakes.html', output="")