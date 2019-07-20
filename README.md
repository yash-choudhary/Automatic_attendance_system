# Multi-Face Recognition and Attendance System
A wide angle CCTV placed above the blackboard of the class detects the faces of all the children, recognizes them and marks their attendance. Result is the Attendance on spreadsheet. Libraries used on python:
* [face_recognition](https://github.com/ageitgey/face_recognition)
* [dlib](https://pypi.org/project/dlib/)
* [OpenCV](https://opencv.org/)

In addition their is also a script for real time face_recognition using web cam and phone camera(using 'IP webcam' on PlayStore). First we run the training script, the program asks for name where we provide the name or a unique identifier which can be used as a primary key(e.g. roll no.). The webCam takes 10 images and stores it int the known_people folder in a folder(with name given initially).We can also use 2 or 3 High-res images insted of 10 webcam images. This is the training data. The end of the cell that is executed finds the encoding of all the faces and trains the K nearest classifier to find the K nearest neighbors to these encodings. This model is stored as 'trained_knn_model.clf' in models folder. This clf file is used directly in training.

To generate test data we can use web cam, phone or could directly paste 10 images of whole class. Note: here 10 images of good quality(for prediction accuracy) is necessary.

Then we run the PredictAttendance script. -> We can predict on the 10 images in test data and attendance is given on the basis if a person is present in more than 5. -> We can also use WebCam of real-time face recognition althogh this feature is just to show surveilance capability and does not give attendance. -> We can also use Phone Camera intgrated with IP webcam application. -> In this the user is expected to run IP webcam on his/her phone and create a server(connection) -> For this, the computer(server) and the phone must be connected on same Wifi(net enabled).

Instructions for installation:
  * Install and unpack electron inside the /main
  * Open Terminal and run electron using: 
    > npm start
  * Default logins credentials are:
    > staff@mozohack.com | mozostaff
    > admin@mozohack.com | mozoadmin
    
All codes are equipped with appropriate logs for debug.

Note:- The model is pretrained on Jason Mamoa, Elon Musk and Leonardo DiCap. So you can directly run the PredictAttendance(Face_recog 10 stills) to see the output.
<p align="center">
  <img src="UPDATED/Screenshot 2019-03-31 at 1.35.54 AM.png" width="350" title="Demo">
</p>
