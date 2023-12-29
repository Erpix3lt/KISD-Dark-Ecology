import unittest
import cv2
from brightness_analyser import BrightnessAnalyser

class TestBrightnessAnalyser(unittest.TestCase):

    def test_process_image(self):
        # Load the example image (adjust the file path accordingly)
        image = cv2.imread('assets/bright_spot_right.jpg')

        # Instantiate the BrightnessAnalyser
        analyser = BrightnessAnalyser()

        # Call the process_image method
        result = analyser.process_image(image)

        # The example image has its brightest spot on the right side,
        # so the result should be False
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
