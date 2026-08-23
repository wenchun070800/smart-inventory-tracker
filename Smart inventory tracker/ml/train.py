from ultralytics import YOLO
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--data', default='ml/yolo_config.yaml')
parser.add_argument('--epochs', type=int, default=100)
parser.add_argument('--imgsz', type=int, default=640)
parser.add_argument('--batch', type=int, default=16)
parser.add_argument('--weights', default='yolov8n.pt')
args = parser.parse_args()

os.makedirs('runs', exist_ok=True)
print(f"Starting training with data={args.data}, epochs={args.epochs}, imgsz={args.imgsz}")
model = YOLO(args.weights)
model.train(data=args.data, epochs=args.epochs, imgsz=args.imgsz, batch=args.batch, patience=10)
print("Training complete. Best weights in runs/detect/train/weights/best.pt")
