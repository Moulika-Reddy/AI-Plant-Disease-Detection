
# Import required libraries
from pathlib import Path
from PIL import Image
from collections import Counter
import hashlib

# Locate our dataset folder
project_folder = Path(__file__).resolve().parent.parent
dataset_path = project_folder / "data" / "raw" / "PlantVillage"

# Store dataset information
image_sizes = Counter()
image_formats = Counter()
image_hashes = {}
corrupted_images = []
duplicates = []

# Go through all 15 class folders
for folder in sorted(dataset_path.iterdir()):

    if not folder.is_dir():
        continue

    # Go through images in each folder
    for image_path in folder.iterdir():

        if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue

        try:
            # Verify that the image file is readable
            with Image.open(image_path) as img:
                img.verify()

            # Reopen to get dimensions and format
            with Image.open(image_path) as img:
                image_sizes[img.size] += 1
                image_formats[img.format] += 1

            # Generate a hash to detect identical files
            with open(image_path, "rb") as file:
                image_hash = hashlib.sha256(file.read()).hexdigest()

            # Check whether the same image was seen before
            if image_hash in image_hashes:
                duplicates.append(
                    (str(image_path), image_hashes[image_hash])
                )
            else:
                image_hashes[image_hash] = str(image_path)

        except Exception as error:
            corrupted_images.append((str(image_path), str(error)))

# Display results
print("\nImage Dimensions:")
for size, count in image_sizes.items():
    print(size, ":", count)

print("\nImage Formats:")
for fmt, count in image_formats.items():
    print(fmt, ":", count)

print("\nCorrupted Images:", len(corrupted_images))
print("Exact Duplicate Images:", len(duplicates))

# Show examples if duplicates are found
for duplicate in duplicates[:10]:
    print("Duplicate:", duplicate)
