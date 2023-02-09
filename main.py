import cv2
import numpy as np


img = cv2.imread("1.jpg")
img_copy = cv2.imread("1.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
max_distance = 100

lower_green = np.array([45, 100, 50])
upper_green = np.array([75, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
bold_points = []
for cnt in contours:
    if cv2.contourArea(cnt) > 100 and cv2.contourArea(cnt) < 1000:
        bold_points.append(cv2.minEnclosingCircle(cnt))


for i in range(len(bold_points) - 2):
    point1 = (int(bold_points[i][0][0]), int(bold_points[i][0][1]))
    point2 = (int(bold_points[i+1][0][0]), int(bold_points[i+1][0][1]))
    point3 = (int(bold_points[i+2][0][0]), int(bold_points[i+2][0][1]))
    distance1 = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    distance2 = np.sqrt((point3[0] - point2[0])**2 + (point3[1] - point2[1])**2)
    if distance1 < max_distance and distance2 < max_distance:
        angle = np.arctan2(point2[1] - point1[1], point2[0] - point1[0]) * 180 / np.pi
        cv2.line(img, point1, point3, (0, 255, 0), 5)
        cv2.line(img, point2, point3, (0, 255, 0), 5)
        cv2.putText(img, str(int(angle)), (point2[0], point2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

cv2.imshow("Image before", img_copy)
cv2.waitKey(0)
cv2.imshow("Image with lines", img)
cv2.waitKey(0)
cv2.imshow("Image in HSV", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()