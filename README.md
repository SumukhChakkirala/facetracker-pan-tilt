Beans: A Face-Tracking Robot with a Human Touch

Beans is a face-tracking robot that uses a laptop's webcam to detect and track faces, moving its display to align with the face. It adds personality by displaying a smiley face, making the interaction feel more human-like.
Features

    Face tracking with a webcam.
    Servo motors to move the display and track the face.
    Friendly smiley face displayed on the screen.

Hardware Requirements

    Arduino board (e.g., Arduino Uno).
    2x Servo motors.
    LCD or LED Matrix display (optional, for displaying the smiley face).
    Laptop/PC with a webcam.

Software Requirements

    Python 3.x
    Libraries: opencv-python, cvzone, pyfirmata, numpy

Project Setup
Hardware Connections

    Connect the servo motors to pins 9 and 10 on the Arduino for X and Y axis control.
    Connect your display to the Arduino as per your setup (optional).
    Power the Arduino via USB or an external power source.

Software Setup

    Install Python Dependencies: pip install opencv-python pyfirmata cvzone numpy  

Upload the PyFirmata example found in the Arduino examples to the Arduino Uno:

    Open the Arduino IDE and go to File > Examples > PyFirmata.
    Select the example.
    Connect your Arduino Uno to your computer.
    Select the correct Board and Port from the Tools menu.
    Click the Upload button in the Arduino IDE to upload the example code to the Arduino Uno.
Run the Python Script:

    Make sure the Arduino is connected to the correct serial port (/dev/ttyUSB0 in linux or COM3 in windows).
    Run the Python face-tracking script

For the Display we could attact an LED Display to the pan-tilt servo mount 
