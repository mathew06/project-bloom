from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from werkzeug.utils import secure_filename
from flask_session import Session
import uuid
import time
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import os
from clrdtctn import color_function
from imageResize import resize_image

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './flask_session/'
app.config['SESSION_PERMANENT'] = False

Session(app)

# Configure upload folder
UPLOAD_FOLDER = './static/Uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route to serve the HTML form
@app.route('/')
def index():
    return render_template('front.html')

@app.route('/one',methods=['GET','POST'])
def one():
    return render_template('1.html')

@app.route('/test1',methods=['GET','POST'])
def test1():
    return render_template('test1.html')

@app.route('/test2',methods=['GET','POST'])
def test2():
    return render_template('test2.html')

@app.route('/test3',methods=['GET','POST'])
def test3():
    return render_template('test3.html')

@app.route('/test4',methods=['GET','POST'])
def test4():
    return render_template('test4.html')

@app.route('/test5',methods=['GET','POST'])
def test5():
    return render_template('test5.html')

@app.route('/test6',methods=['GET','POST'])
def test6():
    return render_template('test6.html')

@app.route('/test7',methods=['GET','POST'])
def test7():
    return render_template('test7.html')

@app.route('/deotaranopia',methods=['GET','POST'])
def deotaranopia():
    return render_template('deotaranopia.html')

@app.route('/monocromatic',methods=['GET','POST'])
def monocromatic():
    return render_template('monocromatic.html')

@app.route('/oops',methods=['GET','POST'])
def oops():
    return render_template('oops.html')

@app.route('/protonopia',methods=['GET','POST'])
def protonopia():
    return render_template('protonopia.html')

@app.route('/tritanopia',methods=['GET','POST'])
def tritanopia():
    return render_template('tritanopia.html')

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/imageupload')
def imageupload():
    # Fetch the image path from the session
    image = session.get('image')
    return render_template('imageUpload.html', image_name=image)

@app.route('/camera')
def camera():
    return render_template('opencamera.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    # Get the image data from the request
    image_data = request.files['image']
    # Define the path where the image will be saved
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'frame.jpg')
    # Save the image to the server
    image_data.save(image_path)
    session['image'] = image_path
    img_path = session.get('image')
    result = color_function(img_path,500, 375)
    return jsonify({'result': result})

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file part'
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Ensure unique filename
        unique_id = str(uuid.uuid4())
        filename = secure_filename(f"{unique_id}_{file.filename}")
        # Resize the image
        file = resize_image(file)
        loc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(loc)
        # Store file paths in session
        session['image'] = loc
        return jsonify({'image_filename': filename})

# Route to handle image coordinate processing
@app.route('/process_coordinates', methods=['POST'])
def process_coordinates():
    data = request.json
    x = data.get('x')
    y = data.get('y')
    image_path = session.get('image')
    # Process the coordinates as needed
    result = color_function(image_path,x, y)
    return jsonify({'result': result})

# Clean up function to remove all files older than 5 minutes
def cleanup_upload_folder():
    folder = app.config['UPLOAD_FOLDER']
    now = time.time()
    cutoff = now - 5 * 60 # 5 minutes ago

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            if os.stat(filepath).st_mtime < cutoff:
                os.remove(filepath)
                print(f"Deleted {filepath}")

# Setup a scheduler to run the cleanup function periodically
scheduler = BackgroundScheduler()
scheduler.add_job(func=cleanup_upload_folder, trigger="interval", minutes=1)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(debug=True)