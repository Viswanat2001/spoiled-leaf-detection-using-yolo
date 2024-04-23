from ultralytics import YOLO
import cv2

model=YOLO('../YOLO-Weights/yolov8n.pt')
results=model.train(data="data.yaml", show=True , epochs=500 , imgsz=640)

cv2.waitKey(0)