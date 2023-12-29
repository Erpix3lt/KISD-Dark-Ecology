from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
image_folder = '_images'

@app.route('/')
def index():
    # Assuming images are in the 'cam_images' folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    image_paths = [os.path.join(image_folder, img) for img in images]
    return render_template('index.html', image_paths=image_paths)

@app.route('/_images/<path:filename>')
def get_image(filename):
    return send_from_directory(image_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
