
# Import required libraries
from pathlib import Path
import hashlib
import shutil

# Locate the project folder
project_folder = Path(__file__).resolve().parent.parent

# Original dataset location
raw_path = project_folder / "data" / "raw" / "PlantVillage"

# Cleaned dataset location
clean_path = project_folder / "data" / "cleaned" / "PlantVillage"

# Create the cleaned dataset directory
clean_path.mkdir(parents=True, exist_ok=True)

# Store hashes of images already copied
seen_hashes = set()

# Track the number of copied and duplicate images
copied_count = 0
duplicate_count = 0

# Go through each disease category
for folder in sorted(raw_path.iterdir()):

    if not folder.is_dir():
        continue

    # Create the same category folder in cleaned data
    destination_folder = clean_path / folder.name
    destination_folder.mkdir(exist_ok=True)

    # Go through images in the category
    for image_path in sorted(folder.iterdir()):

        if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue

        # Generate a unique fingerprint for the image
        with open(image_path, "rb") as file:
            image_hash = hashlib.sha256(file.read()).hexdigest()

        # Skip images already encountered
        if image_hash in seen_hashes:
            duplicate_count += 1
            continue

        # Remember the image hash
        seen_hashes.add(image_hash)

        # Copy the unique image to the cleaned dataset
        shutil.copy2(
            image_path,
            destination_folder / image_path.name
        )

        copied_count += 1

# Display the cleaning summary
print("\nDataset Cleaning Summary")
print("-" * 40)
print("Original images:", copied_count + duplicate_count)
print("Duplicate images skipped:", duplicate_count)
print("Unique images copied:", copied_count)

print("\nCleaned dataset saved to:")
print(clean_path)
