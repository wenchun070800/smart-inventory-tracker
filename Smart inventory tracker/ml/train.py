from ultralytics import YOLO
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--data', default='ml/yolo_config.yaml')
parser.add_argument('--epochs', type=int, default=100)
parser.add_argument('--imgsz', type=int, default=640)
parser.add_argument('--batch', type=int, default=16)
args = parser.parse_args()

model = YOLO('yolov8n.pt')  # start from small pretrained
model.train(data=args.data, epochs=args.epochs, imgsz=args.imgsz, batch=args.batch, patience=10)
print("Training complete. Best weights in runs/detect/train/weights/best.pt")
