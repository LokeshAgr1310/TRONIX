import cv2 as cv
from deepface import DeepFace as df

capture = cv.VideoCapture(0)

while True:
    _,frame = capture.read()
   
    if _:
        emotion = df.analyze(frame,["emotion"],enforce_detection=False)
        print(print(emotion["dominant_emotion"]))

    if (cv.waitKey(1) & 0xFF) == ord('q'):
        break

    cv.imshow("frame",frame)

capture.release()#releases the capture pointer and frees the memory
cv.destroyAllWindows()#closes all the