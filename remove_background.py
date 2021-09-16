import cv2

# 原始
img1 = cv2.imread("hw2.png", 1)

# 去藍 → 轉變色彩型態觀察
img2 = cv2.subtract(img1, (255, 0, 0, 255))
img3 = cv2.cvtColor(img2, cv2.COLOR_HSV2BGR)

# 背景反黑並剩字 → 凸顯字體顏色
img4 = cv2.subtract(img3, (254, 255, 255, 255))
img5 = cv2.multiply(img4, (255, 0, 0, 255))

# 轉變色彩型態至灰階 → 凸顯字體顏色  (黑底白字)
img6 = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
img7 = cv2.multiply(img6, 255)

# 取反 (白底黑字)
img8 = cv2.bitwise_not(img7)

cv2.imshow("img", img8)
cv2.waitKey(0)
cv2.destroyAllWindows()