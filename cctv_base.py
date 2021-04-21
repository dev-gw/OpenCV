import picamera
import time
import datetime

def record():
 with picamera.PiCamera() as camera:
 	camera.resolution = (640, 480)  #해상도 설정
 	now = datetime.datetime.now()   # 현재 시스템 시간 저장
 	filename = now.strftime('%Y-%m-%d %H:%M:%S')  # 시간을 원하는 형식으로 포맷팅
 	camera.start_recording(output = filename + '.h264') # 라즈베리 파이 카메라 모듈은 .h264로 저장됌
 	camera.wait_recording(10)
 	camera.stop_recording()

 while True:
 	record()