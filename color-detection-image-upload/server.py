from flask import Flask, render_template, request, redirect, url_for, jsonify
from clrdtctn import color_function
from clrdtctn import set_imgLocation
from imageResize import resize_image
import os

app = Flask(__name__)

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
    return render_template('image_upload.html', image_filename='img.png')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    # Get the image data from the request
    image_data = request.files['image']
    # Define the path where the image will be saved
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'frame.jpg')
    # Save the image to the server
    image_data.save(image_path)
    set_imgLocation(image_path)
    result = color_function(500, 375)
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
        filename = 'img.png'
        # Resize the image
        file = resize_image(file)
        loc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(loc)
        set_imgLocation(loc)
        return redirect(url_for('imageupload', image_filename=filename))

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