# Fig. 7b - A variation of adaptive backgrounding in Python
import cv2
threshold = 10
camera = cv2.VideoCapture(0)
_, backgroundFrame = camera.read()
backgroundFrame = cv2.cvtColor(backgroundFrame, cv2.COLOR_BGR2GRAY)
i = 1
while 1:
	_, currentFrame = camera.read()
	currentFrame = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
	foreground = cv2.absdiff(backgroundFrame, currentFrame)
	foreground = cv2.threshold(foreground, threshold, 255, cv2.THRESH_BINARY)[1]
	cv2.imshow("foreground", foreground)
	alpha = (1.0/i)
	backgroundFrame = cv2.addWeighted(currentFrame, alpha, backgroundFrame, 1.0-alpha, 0)
	cv2.imshow("backgroundFrame", backgroundFrame)
	i += 1