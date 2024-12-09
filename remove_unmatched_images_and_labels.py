import os

# Define folder paths
images_folder = "tariq hatouq validated/tariq hatouq/gloves.v2i Final Annotations 1/images"
labels_folder = "tariq hatouq validated/tariq hatouq/gloves.v2i Final Annotations 1/labels"

# Get lists of files in each folder
image_files = {os.path.splitext(f)[0] for f in os.listdir(images_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))}
label_files = {os.path.splitext(f)[0] for f in os.listdir(labels_folder) if f.endswith('.txt')}

# Identify unmatched files
unmatched_images = image_files - label_files
unmatched_labels = label_files - image_files

# Remove unmatched image files
for image in unmatched_images:
    image_path = os.path.join(images_folder, image + '.jpg')  # Change extension if needed
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Removed unmatched image: {image_path}")

# Remove unmatched label files
for label in unmatched_labels:
    label_path = os.path.join(labels_folder, label + '.txt')
    if os.path.exists(label_path):
        os.remove(label_path)
        print(f"Removed unmatched label: {label_path}")

print("Cleanup completed.")
