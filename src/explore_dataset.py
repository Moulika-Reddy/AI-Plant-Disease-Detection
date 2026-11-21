
# Import the required libraries
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Locate the PlantVillage dataset
# __file__ refers to the current Python script
project_folder = Path(__file__).resolve().parent.parent
dataset_path = project_folder / "data" / "raw" / "PlantVillage"

# Check that the dataset folder exists
if not dataset_path.exists():
    print("Dataset folder not found!")
    print("Expected location:", dataset_path)
    raise SystemExit(1)

# Store the image count for each disease category
class_counts = {}

# Go through each category folder
for folder in sorted(dataset_path.iterdir()):

    # Skip files that are not folders
    if not folder.is_dir():
        continue

    # Count image files in the folder
    images = [
        file for file in folder.iterdir()
        if file.suffix.lower() in [".jpg", ".jpeg", ".png"]
    ]

    # Save the folder name and image count
    class_counts[folder.name] = len(images)

# Convert results into a Pandas DataFrame
df = pd.DataFrame(
    list(class_counts.items()),
    columns=["Disease Category", "Image Count"]
)

# Print dataset information
print("\nPlantVillage Dataset Summary")
print("-" * 50)
print(df.to_string(index=False))

print("\nTotal classes:", len(df))
print("Total images:", df["Image Count"].sum())

# Create a bar chart showing images per category
plt.figure(figsize=(12, 7))
plt.barh(df["Disease Category"], df["Image Count"])
plt.xlabel("Number of Images")
plt.ylabel("Disease Category")
plt.title("PlantVillage Dataset - Class Distribution")
plt.tight_layout()

# Save the graph in the results folder
results_path = project_folder / "results"
results_path.mkdir(exist_ok=True)

plt.savefig(results_path / "class_distribution.png", dpi=300)
plt.show()

print("\nClass distribution graph saved successfully!")
