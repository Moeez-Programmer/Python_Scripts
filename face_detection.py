import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg",1)
gray = cv2.cvtColor(img,(cv2.COLOR_BGR2GRAY))
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("njd",img)
cv2.waitKey(2000)
cv2.destroyAllWindows()