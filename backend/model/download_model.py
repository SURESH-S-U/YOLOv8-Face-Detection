from ultralytics import YOLO

# Download the YOLOv8 model
model = YOLO("yolov8n.pt")
model.export(format="onnx")  # Optional: Convert to ONNX format
