import tensorflow as tf
import cv2

video_feed = cv2.VideoCapture(0)

while True:
    ret, theImage = cap.read()
    