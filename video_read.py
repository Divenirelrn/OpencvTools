import cv2


source = 0
cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     exit()

fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*"MJPG")

writer = cv2.VideoWriter("./video.avi", fourcc, fps, size)

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("frame", 640, 480)

while cap.isOpened():
    rval, frame = cap.read()
    if not rval:
        break

    cv2.imshow("frame", frame)
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()

