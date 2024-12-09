import os
'''
# Folder containing YOLOv8 label files
label_folder = "our_data/Construction Site Safety.v30-raw-images_latestversion.yolov8/valid/labels"

# Iterate through all txt files in the folder
for filename in os.listdir(label_folder):
    if filename.endswith(".txt"):  # Process only txt files
        file_path = os.path.join(label_folder, filename)

        # Open the file and read lines
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Filter out lines with class index 1
        filtered_lines = [line for line in lines if not line.startswith("3 ")]

        # Overwrite the file with filtered lines
        with open(file_path, "w") as file:
            file.writelines(filtered_lines)

print("Bounding boxes with class index 1 have been removed.")
'''

import os

# Folder containing YOLOv8 label files
label_folder = "our_data/Construction Site Safety.v30-raw-images_latestversion.yolov8/train/labels"

# Iterate through all txt files in the folder
for filename in os.listdir(label_folder):
    if filename.endswith(".txt"):  # Process only txt files
        file_path = os.path.join(label_folder, filename)

        # Open the file and read lines
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Filter out lines with class index > 11
        filtered_lines = [
            line for line in lines if int(line.split()[0]) <= 11
        ]

        # Overwrite the file with filtered lines
        with open(file_path, "w") as file:
            file.writelines(filtered_lines)

print("Bounding boxes with class index > 11 have been removed.")
