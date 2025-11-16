import numpy as np
import cv2 as cv

cv.namedWindow("Controls")

cv.createTrackbar("SigmaColor", "Controls", 150, 500, lambda x: None)
cv.createTrackbar("SigmaSpace", "Controls", 150, 500, lambda x: None)
cv.createTrackbar("BlockSize", "Controls", 9, 15, lambda x: None)
cv.createTrackbar("C", "Controls", 3, 10, lambda x: None)

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    sigmaColor = cv.getTrackbarPos("SigmaColor", "Controls")
    sigmaSpace = cv.getTrackbarPos("SigmaSpace", "Controls")
    blockSize   = cv.getTrackbarPos("BlockSize", "Controls")
    C           = cv.getTrackbarPos("C", "Controls")

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
    color = cv.bilateralFilter(frame, d=9, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)

    if blockSize % 2 == 0: blockSize += 1

    if blockSize < 3: blockSize = 3

    edges = cv.adaptiveThreshold(
        gray_blur, 255,
        cv.ADAPTIVE_THRESH_MEAN_C,
        cv.THRESH_BINARY,
        blockSize,
        C
    )
    
    edges_bgr = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)

    cartoon = cv.bitwise_and(color, edges_bgr)
    combined = np.hstack((frame, cartoon))
    combined_2 = np.hstack((frame, edges_bgr))
    combined_3 = np.vstack((combined, combined_2))

    # Display the resulting frame
    cv.imshow('frame', combined_3)

    # Exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if cv.getWindowProperty('frame', cv.WND_PROP_VISIBLE) < 1:
        break
    # Save
    if cv.waitKey(1) & 0xFF == ord('s'):
        cv.imwrite("result2.png", combined_3)
        print("Image saved as saved_output.png")
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()