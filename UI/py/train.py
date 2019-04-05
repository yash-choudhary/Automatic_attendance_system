#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import cv2
from sklearn import neighbors
import numpy as np
import pandas as pd
import os
import os.path
import pickle
from PIL import Image, ImageDraw
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
print("in train")
curd = os.getcwd()
try:  
    os.mkdir("{}/assets/models".format(curd))
except:
    pass
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# In[ ]:


def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=False):
   
    X = []
    y = []

    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            image = face_recognition.load_image_file(img_path)
            face_bounding_boxes = face_recognition.face_locations(image)

            if len(face_bounding_boxes) != 1:
                if verbose:
                    print("Image {} not suitable for training: {}".format(img_path, "Didn't find a face" if len(face_bounding_boxes) < 1 else "Found more than one face"))
            else:
                X.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                y.append(class_dir)

    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(X))))
        if verbose:
            print("Chose n_neighbors automatically:", n_neighbors)

    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)

    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)

    return knn_clf


# In[ ]:


#Trainer
if __name__ == "__main__":
    # STEP 1: Train the KNN classifier and save it to disk
    print("Training KNN classifier...")
    classifier = train("assets/data",
                       model_save_path="{}/assets/models/trained_knn_model.clf".format(curd),
                       n_neighbors=2)
    print("Training complete!")

