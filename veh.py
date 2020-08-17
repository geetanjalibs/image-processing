import numpy as np
import cv2
p1 = cv2.imread('/home/geetanajali/internship/t2.jpeg')
p2 = cv2.imread('/home/geetanajali/internship/t3.jpeg')
p3 = cv2.imread('/home/geetanajali/internship/t4.jpeg')
p4 = cv2.imread('/home/geetanajali/internship/t11.jpeg')
car_cascade = cv2.CascadeClassifier('/home/geetanajali/internship/cars.xml')
i1=0
i2=0
i3=0
i4=0
gr1 = cv2.cvtColor(p1, cv2.COLOR_BGR2GRAY)
gr2 = cv2.cvtColor(p2, cv2.COLOR_BGR2GRAY)
gr3 = cv2.cvtColor(p3, cv2.COLOR_BGR2GRAY)
gr4 = cv2.cvtColor(p4, cv2.COLOR_BGR2GRAY)
ca1 = car_cascade.detectMultiScale(gr1,1.1,1)
ca2 = car_cascade.detectMultiScale(gr2,1.1,1)
ca3 = car_cascade.detectMultiScale(gr3,1.1,1)
ca4 = car_cascade.detectMultiScale(gr4,1.1,1)
for (x,y,w,h) in ca1:
    i1=i1+1
for (x,y,w,h) in ca2:
    i2=i2+1
for (x,y,w,h) in ca3:
    i3=i3+1
for (x,y,w,h) in ca4:
    i4=i4+1
print('no of vehicles in p1=',i1)
print('no of vehicles in p2=',i2)
print('no of vehicles in p3=',i3)
print('no of vehicles in p4=',i4)
