import cv2


# load haarcascade_frontalface_default
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# load test image
img = cv2.imread('test.jpg')

#opencv only detecs gray scale images
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
faces = face_cascade.detectMultiScale(gray,1.8,2)

# draw rectangle around image
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h),(255,0,0),2)

# show image
cv2.imshow('img',img)

# wait for key press tp close the image window
cv2.waitKey()