import cv2
import numpy as np


img_path = "./dog-cycle-car.png"

img = cv2.imread(img_path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = img[:,:,::-1].transpose((2,0,1)).copy()
# img = img[np.newaxis, :]
img = cv2.resize(img, (418, 418))

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", img)

if cv2.waitKey(0) and 0xFF == ord("q"):
    cv2.destroyAllWindows()

write = True
if write:
    cv2.imwrite("img.jpg", img)