from picamera import PiCamera
from time import sleep
from datetime import datetime
from sys import argv

camera = PiCamera()
camera.resolution=(2560, 1440)
timestamp = str(datetime.today().strftime('%Y-%m-%d-%H%M%S'))
filename = argv[1] + timestamp + str(".png")
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture(filename)
camera.stop_preview()
print("Image captured: %s \n" %filename)
camera.close()


# mkdir /hacks/pics
#
#  crontab -e
#  */5 * * * * /usr/bin/python /hacks/camera.py /hacks/pics >>/hacks/cron.log 2>&1
# crontab -l