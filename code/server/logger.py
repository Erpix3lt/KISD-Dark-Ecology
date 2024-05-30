import time
import tempfile
import webbrowser
from PIL import Image, ImageDraw

class Logger:
    def __init__(self):
      pass

    def log_analysed_image(self, image: Image.Image, add_timestamp = True):
      if add_timestamp:
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), timestamp, fill='white')

      with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
          image.save(temp_file, format='JPEG')
          temp_file_path = temp_file.name
          webbrowser.open('file://' + temp_file_path)