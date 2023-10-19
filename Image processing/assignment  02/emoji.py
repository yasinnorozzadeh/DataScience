import cv2
import cvzone

f_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

f_emoj = cv2.imread("emoji.png", cv2.IMREAD_UNCHANGED)

cap = cv2.VideoCapture(0)
current_state = 0
while True:    
    ret, frame = cap.read()

    FACES = f_detector.detectMultiScale(frame, 1.29 , 4)
    for (x, y, w, h) in FACES:
        finalEmojy = cv2.resize(f_emoj, (w, h))
        frame = cvzone.overlayPNG(frame, finalEmojy, [x, y])
        
    cv2.imshow('video', frame)

    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()