import cv2 #to access the live feed using camera 
import numpy as np #using numpy for normal numeric opreations 
from keras.models import model_from_json


emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# load json and create model
json_file = open('C:\\Users\\km030\\OneDrive\\Desktop\\projects\\Emotion_detection\\model\\emotion_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)# to convert json into model 

# load weights into new model
emotion_model.load_weights("C:\\Users\\km030\\OneDrive\\Desktop\\projects\\Emotion_detection\\model\\emotion_model.h5")
print("Loaded model from disk")

# start the webcam feed
#cap = cv2.VideoCapture(0)

# pass here your video path
cap = cv2.VideoCapture("C:\\Users\\km030\\OneDrive\\Desktop\\projects\\Emotion_detection\\clips\\video1.mp4")

while True:
    # Find haar cascade to draw bounding box around face
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    if not ret:
        break
    face_detector = cv2.CascadeClassifier('C:\\Users\\km030\\OneDrive\\Desktop\\projects\\Emotion_detection\\haarcascades\\haarcascade_frontalface_default.xml')#first of all we have to detected the face for the video or from camera 
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# convert all image into grayscale 

    # detect faces available on camera
    num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # take each face available on the camera and Preprocess it
    for (x, y, w, h) in num_faces:# here i am trying to make the reactangle x,y is the starting corner and w and h is wridth and hight
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
        roi_gray_frame = gray_frame[y:y + h, x:x + w]#croping the each face image 
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)#resize the image  48 by 48 

        # predict the emotions
        emotion_prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(emotion_prediction))#we will check max detection modal of image
        cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

