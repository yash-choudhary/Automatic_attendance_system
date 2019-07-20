#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math
import cv2
import time
from sklearn import neighbors
import numpy as np
import pandas as pd
import os
import os.path
import pickle
from PIL import Image, ImageDraw
import face_recognition
import requests
from face_recognition.face_recognition_cli import image_files_in_folder
curd = os.getcwd()

try:  
    os.mkdir("{}/models".format(curd))
except:
    pass
names=[]
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# In[8]:

import shutil
folder='{}/assets/test/'.format(curd)
dest='{}/assets/History/'.format(curd)
for i in os.listdir(folder):
    shutil.move(folder+i,dest)
    # file_path=os.path.join(folder,i)
    # if os.path.isfile(file_path):
    #     os.remove(file_path)
# In[9]:



cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 100)
rat, frame = cap.read()
count=0
while count<10:
    curtime = time.strftime("%Y_%m_%d-%H_%M_%S")
    rat, frame = cap.read()
    cv2.imwrite("{}/assets/test/{}.jpg".format(curd,curtime), frame)
    count+=1
    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(5)    


cap.release()    
cv2.destroyAllWindows()


# In[10]:


def predict(frame, knn_clf=None, model_path=None, distance_threshold=0.6):
    

    if knn_clf is None and model_path is None:
        raise Exception("Must supply knn classifier either thourgh knn_clf or model_path")

    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)

    
   # X_img = face_recognition.load_image_file(X_img_path)
    X_img = frame
    X_face_locations = face_recognition.face_locations(X_img)

    if len(X_face_locations) == 0:
        return []

    faces_encodings = face_recognition.face_encodings(X_img, known_face_locations=X_face_locations)

    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_face_locations))]

    return [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches)]


# In[11]:


def show_prediction_labels_on_image(frame, predictions):
    
    #pil_image = Image.open(img_path).convert("RGB")
    pil_image = Image.fromarray(frame).convert("RGB")
    draw = ImageDraw.Draw(pil_image)

    for name, (top, right, bottom, left) in predictions:
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        
        name = name.encode("UTF-8")

        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    del draw

    #pil_image.show()
    #cv2.imshow("frame",pil_image)
    return np.asarray(pil_image)


# In[15]:


for image_file in os.listdir(r"{}\assets\test".format(curd)):   
    full_file_path = os.path.join(r"{}\assets\test".format(curd), image_file)

    print("Looking for faces in {}".format(image_file))
    frame = cv2.imread(full_file_path,-1)

    predictions = predict(frame, model_path=r"{}\assets\models\trained_knn_model.clf".format(curd))

    for name, (top, right, bottom, left) in predictions:
        print("- Found {} at ({}, {})".format(name, left, top))
        names.append(name)
    # Display results overlaid on an image
    #show_prediction_labels_on_image(frame, predictions)
    final_img = show_prediction_labels_on_image(frame, predictions)
    cv2.imshow("X",final_img)
    cv2.waitKey(1)
cv2.destroyAllWindows()


# In[16]:


namesD=pd.DataFrame(names, columns=["Names"])
namesD= namesD[namesD.Names!="unknown"]

attendance= pd.DataFrame(namesD.iloc[:,0].value_counts())
attendance.rename(index=str,columns={'Names': 'Count'},inplace=True)
attendance["Present"] =0

attendance["Count"][0] > 5
for i in range(attendance.shape[0]):
    if(attendance["Count"][i] > 5):
        attendance["Present"][i] =1


attendance_final=attendance.drop(['Count'],axis=1)
attendance_final
attendance_final.to_csv('Attendance.csv')


# In[ ]:




