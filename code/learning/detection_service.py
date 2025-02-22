from dataclasses import dataclass
import torch
import cv2
from PIL import Image
import numpy as np
import time
from typing import List

@dataclass
class Detection:
    label: str
    confidence: float
    bounding_box: tuple

class DetectionService:
    """
    A service for object detection using YOLOv5 model.

    Attributes:
    - model: YOLOv5 object detection model.
    """

    def __init__(self):
        """
        Initializes the Detection_Service object.

        This method loads the YOLOv5 model using torch.hub.load() from the ultralytics/yolov5 repository.
        """
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5n')
    
    def initialise_image(self, image: Image.Image)-> np.ndarray:
        """
        Intialising image, converting from pillow to np.
        """
        return np.array(image)
    
    def finalize_image(self, image: Image.Image, result, add_timestamp: bool = False) -> Image.Image:
        """
       Finalize the image. If true draw a timestamp. Draws boxes and percentage around objects found.

        Args:
        - image: Input image to be resized.
        - result: Result
        - add_timestamp: Check wether to draw timestamp

        Returns:
        Finalized Image
        """
        np_image = np.array(image)

        if add_timestamp:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(np_image, timestamp, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        detections = self.polish_result(result)

        for detection in detections:
            x1, y1, x2, y2 = detection.bounding_box
            if detection.label is not None and detection.label == 'person':
                detection.label = 'human component'
            text = detection.label + ' ' + str(detection.confidence)

            cv2.rectangle(np_image, (x1, y1), (x2, y2), (255, 255, 0), 2)
            cv2.putText(np_image, text, (x1 + 10, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

        return Image.fromarray(np_image)
    
    def polish_result(self, result) -> List[Detection]:
        """
        Helper class polishing the result. this will return an array of custom object for each detected object.
        The custom object consists of the label (object name, e.g car), its bounding boxes and the confidence score.
        """
        detections = []
        data_frame = result.pandas().xyxy[0]
        indexes = data_frame.index
        
        for index in indexes:
            x1 = int(data_frame['xmin'][index])
            y1 = int(data_frame['ymin'][index])
            x2 = int(data_frame['xmax'][index])
            y2 = int(data_frame['ymax'][index])
            
            detection = Detection(label=data_frame['name'][index], confidence=data_frame['confidence'][index].round(decimals=2), bounding_box=(x1, y1, x2, y2))
            detections.append(detection)
        
        return detections
        
    def analyse_image(self, image: Image.Image):
        """
        Performs object detection on the input image using the initialized YOLOv5 model.

        Args:
        - image: Input image for object detection.

        Returns:
        A tuple containing:
        - result: Detection result returned by the YOLOv5 model.
        - image: Input image with bounding boxes drawn around detected objects.
        """
        result = self.model(self.initialise_image(image))
        return result, self.finalize_image(image, result)
      
    