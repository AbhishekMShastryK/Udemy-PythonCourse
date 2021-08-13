import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg") #Default as color image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,
minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),4)

print(type(faces))
print(faces)

resized_img = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Gray",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()