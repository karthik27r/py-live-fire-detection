import cv2
import numpy as np

def vidDetection(fname):
    video = cv2.VideoCapture("assets/functions/video1.mp4")

    while True:
        (grabbed, frame) = video.read()
    
        if not grabbed:
            break
        # frame = cv2.resize(frame, (960, 540))
        blur = cv2.GaussianBlur(frame, (15,15),0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    
        lower = [18,50,50]
        upper = [35,255,255]
        lower = np.array(lower,dtype='uint8')
        upper = np.array(upper,dtype='uint8')
    
        mask = cv2.inRange(hsv, lower, upper)
        output=cv2.bitwise_and(frame,hsv,mask=mask)
    
        fireProb = cv2.countNonZero(mask)
    
        cv2.imshow("output", blur) 

        if int(fireProb)>15000:
            print("Fire Detected")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    video.release()