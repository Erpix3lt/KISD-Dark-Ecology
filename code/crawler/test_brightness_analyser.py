import unittest
import cv2
from brightness_analyser import BrightnessAnalyser
from logger import Logger

class TestBrightnessAnalyser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = Logger()
        cls.analysed_images = []
        cls.initial_image = cv2.imread('assets/bright_spot_lower_left.jpg')
        cls.brightness_analyser = BrightnessAnalyser(cls.initial_image)

    @classmethod
    def tearDownClass(cls):
        for analysed_image in cls.analysed_images:
            cls.logger.save_analysed_images_to_web_server(analysed_image)

    def test_process_image_left(self):
        image = cv2.imread('assets/bright_spot_lower_left.jpg')
        result, analysed_image = self.brightness_analyser.process_image(image)
        self.analysed_images.append(analysed_image)
        self.assertTrue(result)

    def test_process_image_lower_left(self):
        image = cv2.imread('assets/bright_spot_lower_left.jpg')
        result, analysed_image = self.brightness_analyser.process_image(image, analyse_lower_half=True)
        self.analysed_images.append(analysed_image)
        self.assertTrue(result)

    def test_process_image_right(self):
        image = cv2.imread('assets/bright_spot_lower_right.jpg')
        result, analysed_image = self.brightness_analyser.process_image(image)
        self.analysed_images.append(analysed_image)
        self.assertFalse(result)

    def test_process_image_lower_right_gaussian_blur(self):
        image = cv2.imread('assets/bright_spot_lower_right.jpg')
        result, analysed_image = self.brightness_analyser.process_image(image, blur_kernel_size=(11, 11), blur_sigma=0)
        self.analysed_images.append(analysed_image)
        self.assertTrue(result)

    def test_process_image_lower_right(self):
        image = cv2.imread('assets/bright_spot_lower_right.jpg')
        result, analysed_image = self.brightness_analyser.process_image(image, analyse_lower_half=True)
        self.analysed_images.append(analysed_image)
        self.assertFalse(result)

    def test_unprepared_image(self):
        image = cv2.imread('assets/no_bright_spot.jpg')
        result, analysed_images = self.brightness_analyser.process_image(image)
        self.analysed_images.append(analysed_images)
        self.assertIsNotNone(result)

    def test_check_if_above_threshhold(self):
        image = cv2.imread('assets/white.jpg')
        result = self.brightness_analyser.check_if_above_threshhold(image)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
