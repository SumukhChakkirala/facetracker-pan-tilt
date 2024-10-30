import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import pyfirmata
import numpy as np
cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()


port = "/dev/ttyUSB0" #enter the name of your port
board = pyfirmata.Arduino(port)
servo_pinX = board.get_pin('d:9:s') #pin 9 Arduino
servo_pinY = board.get_pin('d:10:s') #pin 10 Arduino

detector = FaceDetector()
servoPos = [90, 100] # initial servo position

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img, draw=False)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    #bboxsflip = cv2.flip(bboxs,1)
    if bboxs:
        #get the coordinate
        fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
        #print("the vales of x,,y are",[fx,fy])

        pos = [fx, fy]

        # Draw rectangles around the detected faces and get their coordinates
        servoX = np.interp(fx, [0, ws], [0, 180])
        servoY = np.interp(fy, [0, hs], [0, 180])

        if servoX < 0:
            servoX = 0
            print("out of range")
        elif servoX > 180:
            servoX = 180
            print("out of range")
        if servoY < 0:
            servoY = 0
            print("out of range")
        elif servoY > 180:
            servoY = 180
            print("out of range")
        if servoX>140:
            servoX=140
        elif servoX<40:
            servoX=40
        print(servoPos[0])
        print(servoPos[1])
        servoPos[0] = 180-servoX
        servoPos[1] = servoY
        #if your want the box around your face to be seen uncomment the following lines
        #for (x, y, w, h) in faces:
            #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
            #cvzone.cornerRect(img, (x, y, w, h))

        #cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)
        #cv2.putText(img, str(pos), (fx+15, fy-15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2 )
        #cv2.line(img, (0, fy), (ws, fy), (0, 0, 0), 2)  # x line
        #cv2.line(img, (fx, hs), (fx, 0), (0, 0, 0), 2)  # y line
        #cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)
        #cv2.putText(img, "TARGET", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3 )



    else:
        cv2.putText(img, "NOTHING DETECTED", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)


    cv2.putText(img, f'Servo X: {int(servoPos[0])} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 1)
    cv2.putText(img, f'Servo Y: {int(servoPos[1])} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 1)

    servo_pinX.write(servoPos[0])
    try:
        servo_pinY.write(servoPos[1] - 45)
    except  ValueError :
        pass


    cv2.imshow("Image", img)
    cv2.waitKey(1)
