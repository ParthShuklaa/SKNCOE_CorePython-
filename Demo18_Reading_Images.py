import numpy as np
import cv2

img = cv2.imread("Myimage.jpeg",1)

cv2.imshow("image",img)

k = cv2.waitKey(0) & 0xFF

# wait for ESC key to exit
if k == 27:
    cv2.destroyAllWindows()