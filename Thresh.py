import cv2
import numpy as np
import matplotlib.pyplot as plt

dark=0
white=0

org = cv2.imread('s1.jpg')
img = cv2.imread('s1.jpg',0)
threshold = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

for i in threshold:
    for j in i:
        if j==0:
            dark+=1
        elif j==255:
            white+=1

print(dark,white)

if dark>white:
    print("Less Intensity")
else:
    print("High Intensity")


labels = 'Black', 'White'
sizes = [dark,white]
explode = (0, 0.1)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()


cv2.imshow('GreyScale',img)
cv2.imshow('threshold',threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
