import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Ustawienie rozmiarów wyświetlanych obrazów
# plt.rcParams["figure.figsize"] = (18,10)

image = cv.imread("images/example.jpg")
# plt.show(cv.cvtColor(image, cv.COLOR_BGR2RGB))


flag = np.empty((99, 200, 3), dtype=float)
for x in range(99):
    for y in range(200):
        if x < 33:
            flag[x, y, :] = [0, 1, 0]
        elif x < 66:
            flag[x, y, :] = [1, 1, 0]
        else:
            flag[x, y, :] = [1, 0, 0]
            
flag = cv.cvtColor(flag, cv.COLOR_BGR2RGB)
cv.imshow("Jaki ladny obrazek!", flag)
cv.waitKey(0)
cv.destroyAllWindows()
