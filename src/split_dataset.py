
# Import required libraries
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

# Locate the project and cleaned dataset
project_folder = Path(__file__).resolve().parent.parent
dataset_path = project_folder / "data" / "cleaned" / "PlantVillage"

# Store image paths and their corresponding class labels
image_data = []

# Read images from each disease category
for folder in sorted(dataset_path.iterdir()):

    if not folder.is_dir():
        continue

    for image_path in sorted(folder.iterdir()):

        if image_path.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            image_data.append({
                "image_path": str(image_path.relative_to(project_folder)),
                "label": folder.name
            })

# Convert image information into a DataFrame
df = pd.DataFrame(image_data)

# Split 70% for training and 30% temporarily
train_df, temp_df = train_test_split(
    df,
    test_size=0.30,
    stratify=df["label"],
    random_state=42
)

# Divide the remaining 30% equally:
# 15% validation and 15% testing
val_df, test_df = train_test_split(
    temp_df,
    test_size=0.50,
    stratify=temp_df["label"],
    random_state=42
)

# Label each dataset partition
train_df = train_df.copy()
val_df = val_df.copy()
test_df = test_df.copy()

train_df["split"] = "train"
val_df["split"] = "validation"
test_df["split"] = "test"

# Combine the splits into one table
split_df = pd.concat(
    [train_df, val_df, test_df],
    ignore_index=True
)

# Save the provisional split information
output_path = project_folder / "data" / "provisional_splits.csv"
split_df.to_csv(output_path, index=False)

# Display summary
print("\nProvisional Dataset Split Summary")
print("-" * 45)

print("Training images:", len(train_df))
print("Validation images:", len(val_df))
print("Testing images:", len(test_df))

print("\nTotal images:", len(split_df))

# Show class distribution across all three sets
print("\nClass distribution:")
print(pd.crosstab(split_df["label"], split_df["split"]))

print("\nProvisional split saved to:", output_path)
