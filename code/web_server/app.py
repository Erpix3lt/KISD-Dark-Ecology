from flask import Flask, render_template, send_from_directory, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_images')
def get_images():
    folder_path = request.args.get('folder', default='', type=str)
    image_folder = os.path.join(os.getcwd(), folder_path)
    images = [img for img in os.listdir(image_folder) if img.endswith((".jpg", ".png"))]
    image_paths = [img for img in images]
    return jsonify({'imagePaths': image_paths})

@app.route('/<folder>/<filename>')
def get_image(folder, filename):
    return send_from_directory(folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
