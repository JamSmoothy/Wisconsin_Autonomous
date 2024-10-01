import cv2
import numpy as np

img = cv2.imread('Coding_projects/red.png') #Gets image
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Switches it to HSV color space
#Defines red
lower_range = (0, 50, 175)
upper_range = (10, 255, 255)
mask = cv2.inRange(hsv_img, lower_range, upper_range) #Removes stuff not red
kernel = np.ones((3, 3), np.uint8)
#No idea how this works, but it removes random specks in the background
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.GaussianBlur(mask, (5, 5), 0)
color_img = cv2.bitwise_and(img, img, mask=mask)

#Gets the coordinates of cones
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    x, y, _, _ = cv2.boundingRect(contour)
    if x < (color_img.shape[1] / 2): #If it is part of the left set of cones
        left_coordinates.append((x, y))
    else: #If it is part of the right set of cones
        right_coordinates.append((x, y))
#Literally copied this off the internet
xl, yl = zip(*left_coordinates)
xr, yr = zip(*right_coordinates)

#Linear Regression
ml, bl = np.polyfit(xl, yl, 1)
mr, br = np.polyfit(xr, yr, 1)

#Draws line
x1 = 0
xf = int(color_img.shape[1])
yl1 = int(ml * x1 + bl)
ylf = int(ml * xf + bl)
yr1 = int(mr * x1 + br)
yrf = int(mr * xf + br)

cv2.line(img, (x1, yl1), (xf, ylf), (0, 0, 255), 2)
cv2.line(img, (x1, yr1), (xf, yrf), (0, 0, 255), 2)

#Creates the image
cv2.imwrite('Coding_projects/answer.png', img)
