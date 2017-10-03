import cv2

dark=0
white=0

print("Minimum pixel set = 10")
img=cv2.imread("temp1.jpg",0)
#print(img)
print(len(img),len(img[0]))

r=int(len(img)/2)
c=int(len(img[0])/2)

r1=r-5
r2=r+5

c1=c-5
c2=c+5

#print(img[r1:r2,c1:c2])
print(img)

for i in img:
    for j in i:
        if j<125:
            dark+=1
        elif j>125:
            white+=1

print(dark,white)

if dark>white:
    print("Less Intensity")
else:
    print("High Intensity")
