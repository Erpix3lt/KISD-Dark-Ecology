import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vision_service import VisionService

visionService = VisionService()
visionService.start()
visionService.capture_array()
visionService.close()