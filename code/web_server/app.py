from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Assuming images are in the 'assets' folder
    image_folder = 'assets'
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]  # Adjust the file extension if needed
    image_paths = [os.path.join(image_folder, img) for img in images]
    return render_template('index.html', image_paths=image_paths)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
