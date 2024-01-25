from flask import Flask, render_template, send_from_directory
import os
import re

app = Flask(__name__)

@app.route('/')
def index():
    # Assuming images are in the '_images' folder
    image_folder = '_images'
    images = [img for img in os.listdir(image_folder) if img.endswith((".jpg", ".png"))]
    
    # Group images by tags
    grouped_images = {}
    for img in images:
        match = re.match(r'(\w+)_(\d{14})_\d+\.jpg', img)
        if match:
            tag, timestamp = match.group(1), match.group(2)
            if tag not in grouped_images:
                grouped_images[tag] = []
            grouped_images[tag].append({'filename': img, 'timestamp': timestamp})

    # Sort images by timestamp within each group
    for tag in grouped_images:
        grouped_images[tag] = sorted(grouped_images[tag], key=lambda x: x['timestamp'], reverse=True)

    return render_template('index.html', grouped_images=grouped_images)

@app.route('/_images/<filename>')
def get_image(filename):
    return send_from_directory('_images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
