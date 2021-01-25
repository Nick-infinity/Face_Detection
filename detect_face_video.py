import cv2


# load haarcascade_frontalface_default
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# load webcam video
cap = cv2.VideoCapture(0);

# read frames from video
while True:
    _, img = cap.read()

#opencv only detecs gray scale images
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
    faces = face_cascade.detectMultiScale(gray,1.1,4)

# draw rectangle around image
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0),2)

# show image
    cv2.imshow('img',img)

# wait for Esc key press to stop the video loop
    k = cv2.waitKey(30) & 0xff
    if k ==27:
        break

cap.release()