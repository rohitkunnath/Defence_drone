from ultralytics import YOLO

# Load your model
model = YOLO('majy8final.pt')

# Run detection on the live feed from ESP32-CAM
results = model(source='http://192.168.252.252:81/stream', show=True, conf=0.5, save=True)

# Visualize the detections (uncomment if you want to show)
# results.show()
