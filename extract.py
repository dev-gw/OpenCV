# extract images from mp4

import cv2

vidcap = cv2.VideoCapture('C:/cv_source/GBC_ball.mp4')

count = 0

while(vidcap.isOpened()):
	ret, image = vidcap.read()
	 
	image = cv2.resize(image, (416, 416)) #이미지 사이즈

	
	if(int(vidcap.get(1)) % 30 == 0): # 30frame 마다 추출
		print('Saved frame number : ' + str(int(vidcap.get(1))))
		cv2.imwrite("C:/GBC/frame%d.png" % count, image) # 저장경로 

		count += 1

vidcap.release()