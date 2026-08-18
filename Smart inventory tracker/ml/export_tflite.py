# ml/export_tflite.py
from ultralytics import YOLO
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--weights', default='runs/detect/train/weights/best.pt')
parser.add_argument('--out', default='edge/models/model.tflite')
args = parser.parse_args()

os.makedirs(os.path.dirname(args.out), exist_ok=True)
model = YOLO(args.weights)
print("Exporting model to TFLite...")
model.export(format='tflite', imgsz=320)
# ultralytics export writes to runs/detect/predict or similar; move/rename as needed
print("Export complete. Move the exported file to:", args.out)
