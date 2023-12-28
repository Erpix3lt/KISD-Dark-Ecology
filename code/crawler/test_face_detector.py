import unittest
import numpy
import cv2
import requests
from io import BytesIO
from face_detector import FaceDetector

class TestFaceDetector(unittest.TestCase):
    def test_face_detection(self):
        # Example image URL with a face
        image_url = "https://upload.wikimedia.org/wikipedia/commons/2/2a/Human_faces.jpg"
        
        # Fetch the image from the URL
        response = requests.get(image_url)
        self.assertEqual(response.status_code, 200, "Failed to fetch the image")

        # Convert the image data to a NumPy array
        image_data = BytesIO(response.content)
        image_array = cv2.imdecode(numpy.frombuffer(image_data.read(), numpy.uint8), -1)
        
        # Perform face detection
        face_detector = FaceDetector("/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")
        faces = face_detector.detect_faces(image_array)

        # Assert that at least one face is detected
        self.assertGreater(len(faces), 0, "No face detected in the image")

if __name__ == '__main__':
    unittest.main()
