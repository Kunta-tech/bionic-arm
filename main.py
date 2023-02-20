import cv2
import controller as cn
import mediapipe
import serial

from cvzone.HandTrackingModule import HandDetector
from cvzone import SerialModule as sm
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=1)
myserial= sm.SerialObject('COM6',9600,1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        fingers1 = detector.fingersUp(hands[0])
        print(fingers1[2])
        myserial.sendData(fingers1)
        cn.led(fingers1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
