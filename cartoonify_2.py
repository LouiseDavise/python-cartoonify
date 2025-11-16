import numpy as np
import cv2 as cv
 
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv.flip(frame, 1) # Flipping
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_blur = cv.medianBlur(gray, 7)
    color = cv.bilateralFilter(frame, d=9, sigmaColor=200, sigmaSpace=10)
    edges = cv.adaptiveThreshold(
        gray_blur, 255,
        cv.ADAPTIVE_THRESH_MEAN_C,
        cv.THRESH_BINARY,
        blockSize=9,
        C=3
    )
    edges_bgr = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    cartoon = cv.bitwise_and(color, edges_bgr)

    # Display the resulting frame
    cv.imshow('frame', cartoon)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    if cv.getWindowProperty('frame', cv.WND_PROP_VISIBLE) < 1:
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()