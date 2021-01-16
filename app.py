from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/fires', methods=['GET', 'POST'])
def fires():
	if request.method == 'POST':
		print(request.form)
		if(request.form["type"] == "1"):
			if 'image' not in request.files:
				return render_template('fires.html')
			f = request.files["image"]
			if f.filename == '':
				return render_template('fires.html')
			if f and allowed_file(f.filename):
				filename = secure_filename(f.filename)
				f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return render_template('fires.html')
	else:
		return render_template('fires.html')

@app.route('/hurricanes', methods=['GET', 'POST'])
def hurricanes():
	if request.method == 'POST':
		print(request.form)
		print(request.form["type"] == "0")
		if(request.form["type"] == "0"):
			if 'image' not in request.files:
				return render_template('hurricanes.html')
			f = request.files["image"]
			if f.filename == '':
				return render_template('hurricanes.html')
			if f and allowed_file(f.filename):
				filename = secure_filename(f.filename)
				f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
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