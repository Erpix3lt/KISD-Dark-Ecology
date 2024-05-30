from vision_service import VisionService

visionService = VisionService()
visionService.start()
visionService.capture_array()
visionService.close()