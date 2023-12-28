import unittest
import cv2
from ..face_detector import FaceDetector

class TestFaceDetector(unittest.TestCase):
    def test_face_detection(self):
        # Path to the downloaded image
        image_path = "assets/face_image.jpg"
        
        # Read the image from the local file
        image_array = cv2.imread(image_path)

        # Perform face detection
        face_detector = FaceDetector("/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")
        faces = face_detector.detect_faces(image_array)

        # Assert that at least one face is detected
        self.assertGreater(len(faces), 0, "No face detected in the image")

if __name__ == '__main__':
    unittest.main()
