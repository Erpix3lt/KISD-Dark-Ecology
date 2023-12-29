from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Assuming images are in the '_images' folder
    image_folder = '_images'
    images = [img for img in os.listdir(image_folder) if img.endswith((".jpg", ".png"))]
    image_paths = [img for img in images]
    return render_template('index.html', image_paths=image_paths)

@app.route('/_images/<filename>')
def get_image(filename):
    return send_from_directory('_images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
