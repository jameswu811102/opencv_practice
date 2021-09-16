import cv2
import numpy as np

v1 = cv2.VideoCapture("hw3.mp4")

while v1.isOpened():
	ret, img1 = v1.read()
	if ret == True:
		img2 = cv2.subtract(img1, (255, 0, 0, 0))
		img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
		img2 = cv2.bitwise_not(img2)
		img2 = cv2.dilate(img2, np.ones((11, 91)))
		img2 = cv2.subtract(img2, 205)
		img2 = cv2.multiply(img2, 100)
		img2 = cv2.inRange(img2, 240, 255)

		contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		for i in range(len(contours)):
			x, y, width, height = cv2.boundingRect(contours[i])
			if width > height * 4:
				cv2.rectangle(img1, (x, y), (x + width, y + height), (0, 0, 255), 2)
				cv2.imshow("m1", img1)

		cv2.imshow("m1", img1)

	if cv2.waitKey(33) != -1:
		break

cv2.destroyAllWindows()