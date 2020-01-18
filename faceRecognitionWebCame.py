import face_recognition
import cv2
import numpy as np

videoCapture = cv2.VideoCapture(0)

known_face_encodings = []
#change color of frame here _____ You can choose your own favourite color
R = 0
G = 255
B = 0
face_locations = []
face_encodings = []
faceNames = []
processThisFrame = True
# Turn on this function to use
"""def pFunction():
    print("Human face detected")"""


while True:
    ret, frame = videoCapture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]


    if processThisFrame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        for face_encoding in face_encodings:
            name = "Human" #change tag Here
            faceNames = []
            faceNames.append(name)     
    processThisFrame = not processThisFrame


    for (top, right, bottom, left), name in zip(face_locations, faceNames):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        #cv2.putText(frame,"Face Recognition",(left, top), font, 1.0, (R, G, B),1)
        cv2.rectangle(frame, (left, top), (right, bottom), (B, G, R), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (B, G, R), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX #chage font to your own
        cv2.putText(frame, name, (left + 9, bottom - 6), font, 1.0, (255, 255, 255), 1)
        #pFunction()
    cv2.imshow('Face Recognition System by Rudra Shah', frame)

    #press letter 'e' to stop the running session
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

videoCapture.release()
cv2.destroyAllWindows()