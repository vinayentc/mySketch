# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:42:04 2017

@author: vinay
"""


import cv2


def sketch(image):
    #cv2.imshow('image',image)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_blur=cv2.GaussianBlur(img_gray,(5,5),0)
    canny_edges=cv2.Canny(img_gray_blur,10,70)
    ret, mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow('mySketch || Hit q To Exit',sketch(frame))
    if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          cap.release()
          break

    

    