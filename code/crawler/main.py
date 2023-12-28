from vision_service import VisionService
from face_detector import FaceDetector
import time

if __name__ == "__main__":
    vision_service = VisionService()
    face_detector = FaceDetector("/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")

    vision_service.start()
    
    try:
        while True:
            image = vision_service.capture_array()
            faces = face_detector.detect_faces(image)
            if len(faces) > 0:
                print("There is a face")
                face_detector.draw_faces(image, faces)
            else:
                print("There is no face")
            time.sleep(5)  # Adjust the delay as needed
    except KeyboardInterrupt:
        pass
    finally:
        vision_service.stop()
