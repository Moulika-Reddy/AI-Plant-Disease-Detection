
# Import required libraries
from pathlib import Path
from PIL import Image
import pandas as pd
import imagehash

# Locate the project folder
project_folder = Path(__file__).resolve().parent.parent

# Read the provisional dataset split
csv_path = project_folder / "data" / "provisional_splits.csv"
df = pd.read_csv(csv_path)

# Store the perceptual hash for each image
hashes = []

# Calculate a perceptual hash for every image
for image_path in df["image_path"]:

    full_path = project_folder / image_path

    with Image.open(full_path) as img:
        image_hash = imagehash.phash(img.convert("RGB"))

    hashes.append(str(image_hash))

# Add hashes to our dataset table
df["phash"] = hashes

# Find images with identical perceptual hashes
# These are candidates for visual similarity
similar_groups = df.groupby("phash")

cross_split_groups = 0
candidate_images = 0

for phash_value, group in similar_groups:

    # Check whether matching hashes occur in different splits
    if len(group) > 1 and group["split"].nunique() > 1:
        cross_split_groups += 1
        candidate_images += len(group)

        # Show the first few matching groups
        if cross_split_groups <= 5:
            print("\nMatching perceptual hash:", phash_value)
            print(group[["image_path", "label", "split"]].to_string(index=False))

print("\nNear-Duplicate Screening Summary")
print("-" * 45)
print("Cross-split matching-hash groups:", cross_split_groups)
print("Images in those groups:", candidate_images)

# Save the hash information for later analysis
output_path = project_folder / "data" / "image_hashes.csv"
df.to_csv(output_path, index=False)

print("\nHash information saved to:", output_path)
