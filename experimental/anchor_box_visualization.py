import cv2
import json
import numpy as np
import argparse


config_file = open("config.json", "r")
configs = json.load(config_file)
anchors = configs['model']['anchors']

w, h = (configs['model']['input_size_w'], configs['model']['input_size_h'])

blank_image = np.zeros((h, w, 3), np.uint8)

new_anchors = [(0, 0, anchors[2 * i], anchors[2 * i + 1]) for i in range(int(len(anchors) // 2))]

colors = [(255, 0, 0),
          (255, 255, 0),
          (0, 255, 0),
          (0, 0, 255),
          (0, 255, 255),
          (55, 0, 0),
          (255, 55, 0),
          (0, 55, 0),
          (0, 0, 25),
          (0, 255, 55)]

cv2.namedWindow('Image')
cv2.moveWindow('Image', w, h)

offset_x = int(w / max(anchors))
offset_y = int(h / max(anchors))

for i, a in enumerate(new_anchors):
    xmin = a[0]
    ymin = a[1]
    xmax = int(a[2] * offset_x)
    ymax = int(a[3] * offset_y)

    cv2.rectangle(blank_image, (xmin, ymin), (xmax, ymax), colors[i])

cv2.imshow('Image', blank_image)
cv2.waitKey(1)
