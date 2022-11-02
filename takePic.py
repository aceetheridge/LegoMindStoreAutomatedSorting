import picamera

with picamera.PiCamera() as camera:
    camera.resolution= (1920,1080)
    camera.capture()