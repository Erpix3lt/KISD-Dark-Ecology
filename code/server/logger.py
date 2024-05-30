import time
import tempfile
import webbrowser
import os
from PIL import Image, ImageDraw

class Logger:
    def __init__(self):
        self.previous_temp_file_path = None

    def log_analysed_image(self, image: Image.Image, add_timestamp=True):
        if add_timestamp:
            timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
            draw = ImageDraw.Draw(image)
            draw.text((10, 10), timestamp, fill='white')

        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
            image.save(temp_file, format='JPEG')
            temp_file_path = temp_file.name

        if self.previous_temp_file_path:
            self.close_preview(self.previous_temp_file_path)
        
        webbrowser.open('file://' + temp_file_path)
        self.previous_temp_file_path = temp_file_path

    def close_preview(self, file_path):
        """
        As temp file are opened on mac with the preview window, we do not want to spam the window.
        This script might close the previous preview window.
        """
        try:
            close_script = f'''
            tell application "Preview"
                set theDocs to every document
                repeat with aDoc in theDocs
                    if (name of aDoc) is equal to "{os.path.basename(file_path)}" then
                        close aDoc
                    end if
                end repeat
            end tell
            '''
            os.system(f"osascript -e '{close_script}'")
        except Exception as e:
            print("Error during close preview window. This might be cause by you either not running this on mac or having not allowed apple script access.", str(e))
