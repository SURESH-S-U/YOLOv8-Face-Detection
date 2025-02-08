import cv2
import torch
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from ultralytics import YOLO

app = FastAPI()

# Load YOLOv8 model
model = YOLO("backend/model/yolov8n.pt")  # Ensure this is the correct face-detection model

# Open webcam
cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break

        # Perform face detection
        results = model(frame)

        # Draw bounding boxes
        for result in results:
            for box in result.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box[:4])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Encode the frame
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.get("/")
def home():
    return {"message": "YOLOv8 Face Detection API is running"}

@app.get("/video_feed")
def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")
