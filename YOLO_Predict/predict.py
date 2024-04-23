from ultralytics import YOLO

import cv2

# Load a pretrained YOLOv8n model
model = YOLO('../runs/detect/train2/weights/best.pt')

# Define path to the image file
source = '../images/WhatsApp Image.jpg'

# Run inference on the source
results = model(source , show=True)  # list of Results objects

cv2.waitKey(0)