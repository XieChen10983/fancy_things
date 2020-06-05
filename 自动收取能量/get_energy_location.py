# coding=gbk
import cv2
import numpy as np

catch_template = cv2.imread("D:/catch_template.png")

screen_shot = cv2.imread("D:/1.png")
roi = screen_shot[:, 1011:, :]

location = cv2.matchTemplate(roi, catch_template, cv2.TM_CCOEFF_NORMED)
max_location = np.where(location > 0.95)

print(max_location[0][0])
# cv2.rectangle(screen_shot, (max_location[0][0], 1010), (max_location[0][0] + 35, 1079), (0, 255, 255), 2)
# cv2.imshow("dlkfj", screen_shot)
# cv2.waitKey()
# cv2.destroyAllWindows()
