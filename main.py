import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img= cv.imread("cat/cat.png")
#cv.imshow("cat",img)
def rescale(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dims=(width,height)
    return cv.resize(frame, dims, interpolation=cv.INTER_AREA)
resize_image=rescale(img)
surf = cv.xfeatures2d.SURF_create(800)
cv.imshow('Image',resize_image)

cv.waitKey(0)
