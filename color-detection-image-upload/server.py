from flask import Flask, render_template, request, redirect, url_for, jsonify
from colordetection import color_function
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/Uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route to serve the HTML form
@app.route('/')
def index():
    return render_template('index.html',image_filename='img.png')

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file part'
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = 'img.png'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index', image_filename=filename))

# Route to handle image coordinate processing
@app.route('/process_coordinates', methods=['POST'])
def process_coordinates():
    data = request.json
    x = data.get('x')
    y = data.get('y')
    # Process the coordinates as needed
    result = color_function(x, y)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
