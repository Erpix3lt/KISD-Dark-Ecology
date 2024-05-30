import torch
import cv2
from PIL import Image
import numpy as np
import time

class Detection_Service:
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
        
        data_frame = result.pandas().xyxy[0]
        indexes = data_frame.index
        for index in indexes:
            # Find the coordinate of top left corner of bounding box
            x1 = int(data_frame['xmin'][index])
            y1 = int(data_frame['ymin'][index])
            # Find the coordinate of right bottom corner of bounding box
            x2 = int(data_frame['xmax'][index])
            y2 = int(data_frame['ymax'][index])

            # Find label name
            label = data_frame['name'][index]
            
            # Find confidence score of the model
            conf = data_frame['confidence'][index]
            text = label + ' ' + str(conf.round(decimals=2))

            cv2.rectangle(np_image, (x1,y1), (x2,y2), (255,255,0), 2)
            cv2.putText(np_image, text, (x1,y1-5), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0), 2)
        return Image.fromarray(np_image)
        
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
      
    def navigate(self, result, where_to: str) -> str:
        """
        Determines the direction to reach the first detected instance of the desired object within the image.

        Args:
        - result: Result of the object detection.
        - where_to: The desired direction relative to the desired object.

        Returns:
        A string indicating the direction to reach the desired object: 'left', 'right', or 'unknown'.
        """
        data_frame = result.pandas().xyxy[0]

        # Filter detection results for the desired object type
        desired_objects = data_frame[data_frame['name'] == where_to]

        if len(desired_objects) == 0:
            return 'unknown'  # Desired object not found

        image_width = result.imgs[0].shape[1]  # Width of the image
        object_x_center = (desired_objects['xmin'] + desired_objects['xmax']) / 2  # X center of the object

        # Get the x coordinate of the first detected instance of the desired object
        first_object_x = object_x_center.iloc[0]

        # Determine if the first detected instance is on the left or right half of the image
        if first_object_x < image_width / 2:
            return 'left'
        else:
            return 'right'
