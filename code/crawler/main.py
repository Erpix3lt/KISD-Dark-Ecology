from vision_service import VisionService
from face_detector import FaceDetector
from file_service import FileService

if __name__ == "__main__":
    vs = VisionService()
    fd = FaceDetector("/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")

    vs.start()
    
    try:
        image = vs.capture_array()
        faces = fd.detect_faces(image)

        if len(faces) > 0:
            print("There is a face")
            fd.draw_faces(image, faces)
            FileService.save_image(image)
        else:
            print("No face detected")
    except KeyboardInterrupt:
        pass
    finally:
        vs.stop()
