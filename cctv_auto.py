import picamera
import time
import datetime
import subprocess

resolution_width = int(input("Set resolution width: "))
resolution_height = int(input("Set resolution height: "))
duration = int(input("Set total duration(sec): "))
interval = int(input("Set recording interval(sec): "))


def record():
    with picamera.PiCamera() as camera: 
        camera.resolution = (resolution_width, resolution_height) # set resolution
        now = datetime.datetime.now()  # get system time and restore
        filename = now.strftime('%Y-%m-%d_%H.%M.%S') # formatting time
        camera.start_recording(output = filename+".h264") # start
        camera.zoom = (0.0, 0.0, 1.0, 1.0) #zoom setting(default)
        camera.wait_recording(interval) # recoding time
        camera.stop_recording() # finish
        subprocess.call("MP4Box -add /home/pi/cctv/"+filename+".h264 /home/pi/cctv/mp4/"+filename+".mp4",shell=True)
        subprocess.call("rm {0}.h264".format(filename), shell=True)

# recording
for i in range(duration//interval):
    record()
