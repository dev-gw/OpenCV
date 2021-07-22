import cv2
import numpy as np

#cap = cv2.VideoCapture(1)
# Load image, convert to grayscale, Otsu's threshold for binary image
#while(True):
    #ret, image = cap.read()

image = cv2.imread('bluepen.jpg') #사진사용
image = cv2.resize(image,(0,0),fx=0.2,fy=0.2) # 사이즈 조절
print(image.shape)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 이미지를 흑백으로 변환
imgBlur = cv2.GaussianBlur(gray,(5,5),1) # 이미지를 부드럽게 처리
imgCanny = cv2.Canny(imgBlur,100,100) # 이미지의 가장자리 검출
kernel = np.ones((5,5))
imgDial = cv2.dilate(imgCanny, kernel, iterations=3) # 객체를 팽창시켜 빈곳을 채움
thresh = cv2.erode(imgDial, kernel, iterations=2) # 객체 외곽을 검은색으로 변경
    #thresh = cv2.threshold(thresh, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find contours, find rotated rectangle, obtain four verticies, and draw
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
rect = cv2.minAreaRect(cnts[0]) # 최소의 사각형 그리기
print(rect)
box = np.int0(cv2.boxPoints(rect))
#print(box) 네 모서리 좌표
cv2.drawContours(image, [box], 0, (36,255,12), 3) # OR
#cv2.polylines(image, [box], True, (36,255,12), 3)


cv2.imshow('image', image)
cv2.waitKey(0)