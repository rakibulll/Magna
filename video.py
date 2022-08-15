import cv2

cv2.namedWindow("output")
cap = cv2.VideoCapture(2)

if cap.isOpened():              # Getting the first frame
    ret, frame = cap.read()
else:
    ret = False

while ret:
    cv2.imshow("output", frame)
    ret, frame = cap.read()
    key = cv2.waitKey(20)
    if key == 27:                    # exit on Escape key
        break
cv2.destroyWindow("output")
