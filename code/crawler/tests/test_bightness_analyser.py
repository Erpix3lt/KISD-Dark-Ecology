import unittest
import cv2
from brightness_analyser import BrightnessAnalyser

class TestBrightnessAnalyser(unittest.TestCase):

    def test_process_image_lower_left(self):
        image = cv2.imread('assets/bright_spot_lower_left.jpg')
        analyser = BrightnessAnalyser()
        result = analyser.process_image(image)
        self.assertTrue(result)

    def test_process_image_lower_right(self):
        image = cv2.imread('assets/bright_spot_lower_right.jpg')
        analyser = BrightnessAnalyser()
        result = analyser.process_image(image)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
