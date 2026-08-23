import cv2
import time
import json
import requests
import argparse
import os
from smoothing import SlidingWindowSmoother, ExpSmoother

parser = argparse.ArgumentParser()
parser.add_argument('--backend', default='http://localhost:8000/api/detections')
parser.add_argument('--camera', type=int, default=0)
parser.add_argument('--interval', type=float, default=2.0)
parser.add_argument('--window', type=int, default=5)
parser.add_argument('--use_ultralytics', action='store_true', help='Use ultralytics YOLO directly (dev only)')
parser.add_argument('--model', default=None, help='Path to tflite model (optional)')
args = parser.parse_args()

smoother = SlidingWindowSmoother(window_size=args.window)
exp_smoother = ExpSmoother(alpha=0.6)

if args.use_ultralytics:
    from ultralytics import YOLO
    model = YOLO('yolov8n.pt')
    def detect_frame(frame):
        results = model(frame, imgsz=640)[0]
        counts = {}
        for box in results.boxes:
            cls = int(box.cls[0])
            name = model.names.get(cls, str(cls))
            counts[name] = counts.get(name, 0) + 1
        return counts
else:
    try:
        import tflite_runtime.interpreter as tflite
    except Exception:
        tflite = None

    if args.model and tflite:
        interpreter = tflite.Interpreter(model_path=args.model)
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
    else:
        interpreter = None

    def detect_frame(frame):
        if interpreter is None:
            return {}
        h, w = frame.shape[:2]
        in_h = input_details[0]['shape'][1]
        in_w = input_details[0]['shape'][2]
        img = cv2.resize(frame, (in_w, in_h))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.astype('float32') / 255.0
        img = img.reshape(input_details[0]['shape'])
        interpreter.set_tensor(input_details[0]['index'], img)
        interpreter.invoke()
        boxes = interpreter.get_tensor(output_details[0]['index'])
        scores = interpreter.get_tensor(output_details[1]['index'])
        classes = interpreter.get_tensor(output_details[2]['index'])
        counts = {}
        for i, s in enumerate(scores[0]):
            if s < 0.3:
                continue
            cls = int(classes[0][i])
            name = str(cls)
            counts[name] = counts.get(name, 0) + 1
        return counts

def main():
    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        print("Cannot open camera")
        return
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            counts = detect_frame(frame)
            smoother.add(counts)
            smoothed = smoother.smoothed()
            smoothed = exp_smoother.update(smoothed)
            payload = {'timestamp': time.time(), 'counts': smoothed, 'device_id': os.getenv('EDGE_DEVICE_ID', 'edge-01')}
            try:
                requests.post(args.backend, json=payload, timeout=2)
            except Exception as e:
                print("Failed to post to backend:", e)
            cv2.imshow("Edge - press q to quit", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(args.interval)
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()