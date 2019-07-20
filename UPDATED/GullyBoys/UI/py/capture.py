#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import time
import os
curd = os.getcwd()
print("in Python file now")

f = open("py/helper.txt", "r") 
name = f.read()
print(name)
f.close()

print("FILE READ COMPLETE")
path = r"{}\assets\data\{}".format(curd,name)
try:  
    os.mkdir(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 100)
rat, frame = cap.read()

count=0
while count<10:
    
    rat, frame = cap.read()
    cv2.imwrite(r"{}\{}{}.jpg".format(path,name,count), frame)
    count+=1
    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(1)    


cap.release()    
cv2.destroyAllWindows()

