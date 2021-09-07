from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
camera.resolution=(2560, 1440)
timestamp = str(datetime.today().strftime('%Y-%m-%d-%H%M%S'))
filename = str("/pics/") + timestamp + str(".png")
camera.start_preview()
sleep(5)
camera.capture(filename)
camera.stop_preview()
print("Image captured: %s \n" %filename)
camera.close()


# mkdir /hacks/pics
#
#  crontab -e
#  */5 * * * * /usr/bin/python /hacks/camera.py >>/hacks/cron.log 2>&1
# crontab -l