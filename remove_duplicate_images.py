import os
import hashlib
from PIL import Image

def hash_image(image_path):
    """Generate a hash for the image using its pixel data."""
    with Image.open(image_path) as img:
        # Convert the image to a consistent format
        img = img.convert("RGB")
        # Resize to standard dimensions for consistent hashing (optional)
        img = img.resize((256, 256))
        # Generate a hash using the pixel data
        return hashlib.md5(img.tobytes()).hexdigest()

def remove_duplicates(folder_path):
    """Find and remove duplicate images based on pixel data."""
    image_hashes = {}
    removed_files = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                image_hash = hash_image(file_path)
                if image_hash in image_hashes:
                    # Duplicate found; remove the file
                    os.remove(file_path)
                    removed_files.append(file_path)
                else:
                    image_hashes[image_hash] = file_path
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

    return removed_files

# Replace with your folder path
folder_path = "final_data/valid/images"

removed_files = remove_duplicates(folder_path)

if removed_files:
    print("Duplicate images removed:")
    for file_path in removed_files:
        print(f"Removed: {file_path}")
else:
    print("No duplicates found.")
