from flask import Flask, render_template, send_from_directory, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_images')
def get_images():
    try:
        folder_path = request.args.get('folder', default='', type=str)
        folder_path = os.path.normpath(folder_path)  # Normalize the path
        image_folder = os.path.join(os.getcwd(), folder_path)

        # Check if the folder exists
        if not os.path.exists(image_folder) or not os.path.isdir(image_folder):
            return jsonify({'error': 'Invalid folder path'})

        images = [img for img in os.listdir(image_folder) if img.endswith((".jpg", ".png"))]
        image_paths = [os.path.join(folder_path, img) for img in images]

        return jsonify({'imagePaths': image_paths})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/<folder>/<filename>')
def get_image(folder, filename):
    try:
        folder_path = os.path.join(os.getcwd(), folder)
        return send_from_directory(folder_path, filename)
    except Exception as e:
        return str(e), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
