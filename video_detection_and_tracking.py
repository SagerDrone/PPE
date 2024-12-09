import cv2
import torch
from ultralytics import YOLO
import os

# Load the YOLOv8 model
model = YOLO("transfer_learning/runs/detect/train3/weights/best.pt")  # Replace with your model's path

# Input and output video paths
input_video_path = "/home/muna/Downloads/hardhat.mp4"  # Replace with your input video path
output_video_path = "/home/muna/Downloads/output_video.mp4"  # Replace with your output video path

# Create a VideoCapture object to read the video
cap = cv2.VideoCapture(input_video_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Step 1: Detect all objects in the frame
    results = model.predict(frame, save=False, conf=0.5)

    # Step 2: Filter detections to keep only "Person" class (class index: 5)
    persons = []
    for box in results[0].boxes:
        if box.cls == 5:  # Replace with the actual class index of "Person" in your model
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            persons.append((x1, y1, x2, y2))

    # Step 3: Process each detected person
    for (x1, y1, x2, y2) in persons:
        # Crop the person from the frame
        cropped_person = frame[y1:y2, x1:x2]

        # Step 4: Send the cropped person back to the model for prediction
        person_results = model.predict(cropped_person, save=False, conf=0.5)

        # Step 5: Draw the predictions for the cropped person on the original frame
        for box in person_results[0].boxes:
            cx1, cy1, cx2, cy2 = map(int, box.xyxy[0])
            class_id = int(box.cls)
            conf = box.conf[0]
            label = f"{model.names[class_id]} {conf:.2f}"

            # Calculate position relative to the original frame
            abs_x1 = x1 + cx1
            abs_y1 = y1 + cy1
            abs_x2 = x1 + cx2
            abs_y2 = y1 + cy2

            # Draw bounding box and label
            cv2.rectangle(frame, (abs_x1, abs_y1), (abs_x2, abs_y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (abs_x1, abs_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Write the frame to the output video
    out.write(frame)

    # Optionally display the frame in a window (press 'q' to quit)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
