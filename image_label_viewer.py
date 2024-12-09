import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to the folders containing images and labels
images_folder = "muna/IS gloves.v1i.yolov8/test/images"
labels_folder = "muna/IS gloves.v1i.yolov8/test/labels"

# Define colors for the classes
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Load image and label file names
image_files = sorted([f for f in os.listdir(images_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])
label_files = sorted([f for f in os.listdir(labels_folder) if f.endswith('.txt')])

# Ensure equal number of images and labels
assert len(image_files) == len(label_files), "Mismatch between images and labels."

# Initialize index
index = 0

def load_labels(file_path):
    """
    Load bounding box labels from a YOLO format text file.
    Returns a list of tuples: (class_id, x_center, y_center, width, height).
    """
    with open(file_path, "r") as f:
        lines = f.readlines()
    labels = [list(map(float, line.strip().split())) for line in lines]
    return labels

def draw_bounding_boxes(image, labels, colors):
    """
    Draw bounding boxes on the image based on labels.
    Each class is assigned a specific color.
    """
    h, w, _ = image.shape
    for label in labels:
        class_id, x_center, y_center, box_width, box_height = label
        class_id = int(class_id)
        color = colors[class_id % len(colors)]
        
        # Convert YOLO format to pixel coordinates
        x1 = int((x_center - box_width / 2) * w)
        y1 = int((y_center - box_height / 2) * h)
        x2 = int((x_center + box_width / 2) * w)
        y2 = int((y_center + box_height / 2) * h)
        
        # Draw rectangle and label
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        cv2.putText(image, f"Class {class_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return image

while True:
    # Load the current image and labels
    image_path = os.path.join(images_folder, image_files[index])
    label_path = os.path.join(labels_folder, label_files[index])
    
    image = cv2.imread(image_path)
    labels = load_labels(label_path)
    
    # Draw bounding boxes
    image_with_boxes = draw_bounding_boxes(image, labels, colors)
    
    # Display the image
    cv2.imshow("Image Viewer", image_with_boxes)
    
    # Wait for user input
    key = cv2.waitKey(0) & 0xFF
    
    if key == ord('d'):  # Next image
        index = (index + 1) % len(image_files)
    elif key == ord('a'):  # Previous image
        index = (index - 1) % len(image_files)
    elif key == ord('t'):  # Delete current image and label
        print(f"Deleting {image_path} and {label_path}")
        os.remove(image_path)
        os.remove(label_path)
        image_files.pop(index)
        label_files.pop(index)
        if index >= len(image_files):
            index = 0  # Reset index if it exceeds the list length
    elif key == 27:  # ESC key to exit
        break

# Close all windows
cv2.destroyAllWindows()


'''
# Path to the folders containing images and labels
images_folder = "our_data/gloves.v2i.yolov8/train/images"
labels_folder = "our_data/gloves.v2i.yolov8/train/labels"

# Define classes and their corresponding colors
classes = ["Hardhat", "No-Hardhat", "NO-Saftey Vest", "Person", "Safety Vest"]
colors = [
    (255, 0, 0),    # Blue for Hardhat
    (0, 255, 0),    # Green for No-Hardhat
    (0, 0, 255),    # Red for NO-Safety Vest
    (255, 255, 0),  # Cyan for Person
    (255, 0, 255)   # Magenta for Safety Vest
]

# Load image and label file names
image_files = sorted([f for f in os.listdir(images_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])
label_files = sorted([f for f in os.listdir(labels_folder) if f.endswith('.txt')])

# Ensure equal number of images and labels
assert len(image_files) == len(label_files), "Mismatch between images and labels."

# Initialize index
index = 0

def load_labels(file_path):
    """
    Load bounding box labels from a YOLO format text file.
    Returns a list of tuples: (class_id, x_center, y_center, width, height).
    """
    with open(file_path, "r") as f:
        lines = f.readlines()
    labels = [list(map(float, line.strip().split())) for line in lines]
    return labels

def draw_bounding_boxes(image, labels, colors, classes):
    """
    Draw bounding boxes on the image based on labels.
    Each class is assigned a specific color.
    """
    h, w, _ = image.shape
    for label in labels:
        class_id, x_center, y_center, box_width, box_height = label
        class_id = int(class_id)
        color = colors[class_id % len(colors)]
        class_name = classes[class_id]
        
        # Convert YOLO format to pixel coordinates
        x1 = int((x_center - box_width / 2) * w)
        y1 = int((y_center - box_height / 2) * h)
        x2 = int((x_center + box_width / 2) * w)
        y2 = int((y_center + box_height / 2) * h)
        
        # Draw rectangle and label
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        cv2.putText(image, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return image

while image_files and label_files:
    # Load the current image and labels
    image_path = os.path.join(images_folder, image_files[index])
    label_path = os.path.join(labels_folder, label_files[index])
    
    image = cv2.imread(image_path)
    labels = load_labels(label_path)
    
    # Draw bounding boxes
    image_with_boxes = draw_bounding_boxes(image, labels, colors, classes)
    
    # Display the image
    cv2.imshow("Image Viewer", image_with_boxes)
    
    # Wait for user input
    key = cv2.waitKey(0) & 0xFF
    
    if key == ord('d'):  # Next image
        index = (index + 1) % len(image_files)
    elif key == ord('a'):  # Previous image
        index = (index - 1) % len(image_files)
    elif key == ord('t'):  # Delete current image and label
        print(f"Deleting {image_path} and {label_path}")
        os.remove(image_path)
        os.remove(label_path)
        image_files.pop(index)
        label_files.pop(index)
        if index >= len(image_files):
            index = 0  # Reset index if it exceeds the list length
    elif key == 27:  # ESC key to exit
        break

    # Check if there are no files left
    if not image_files or not label_files:
        print("No more images or labels to display.")
        break

# Close all windows
cv2.destroyAllWindows()

'''