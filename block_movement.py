import numpy as np
import cv2

window_height = 360
window_width = 600
left_up_x = 0
right_down_x = 80
side = right_down_x - left_up_x


R_direction = list(range(0, window_width-side+1))
L_direction = R_direction[:len(R_direction)-1]
L_direction = L_direction[::-1]
move_step = R_direction + L_direction


dic = {}
i = 0
for s in move_step:
    dic[str(i)] = s
    i += 1


index = 0
while True:
    if index != len(dic):
        img = np.full((window_height, window_width, 3), (255, 255, 255), np.uint8)
        sqr = cv2.rectangle(img, (dic[str(index)], 140), (dic[str(index)]+side, 220), (255, 0, 0), -1)
        cv2.imshow("img", img)
        index += 1

    elif index == len(dic):
        index == 0

    if cv2.waitKey(1) != -1:
        break
cv2.destroyAllWindows()