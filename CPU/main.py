import cv2
cap = cv2.VideoCapture(0)
#Set khung ti le webcam
cap.set(3, 640)
cap.set(4, 480)
imgBackground  = cv2.imread('Resources/background.png')
folderModePath ='Resources/Modes'
while True:
    success, img = cap.read()
#Chen 2 lop layer lai voi nhau
    imgBackground[162:162+480, 55:55+640] = img
    # cv2.imshow("Displayface", img)
    cv2.imshow("Face Attendace", imgBackground)
    cv2.waitKey(1)


