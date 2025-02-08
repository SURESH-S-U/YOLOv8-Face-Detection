from fastapi import FastAPI
from fastapi.responses import JSONResponse
import cv2
import torch
from ultralytics import YOLO

app = FastAPI()

# Load YOLO model
model = YOLO("backend/model/yolov8n.pt")

@app.get("/")
def root():
    return {"message": "Backend is running!"}

@app.get("/detect")
def detect():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        return JSONResponse(content={"error": "Failed to capture frame"}, status_code=500)

    # Run YOLO detection
    results = model(frame)
    detections = []

    for result in results:
        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box[:4])
            detections.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

    cap.release()
    return {"detections": detections}
