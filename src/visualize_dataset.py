
# Import required libraries
from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image

# Locate the project and dataset folders
project_folder = Path(__file__).resolve().parent.parent
dataset_path = project_folder / "data" / "raw" / "PlantVillage"

# Get all 15 disease category folders
class_folders = sorted([
    folder for folder in dataset_path.iterdir()
    if folder.is_dir()
])

# Create a figure with 3 rows and 5 columns
fig, axes = plt.subplots(3, 5, figsize=(16, 10))

# Display one sample image from each category
for ax, folder in zip(axes.flat, class_folders):

    # Get all image files from the category
    image_files = sorted([
        file for file in folder.iterdir()
        if file.suffix.lower() in [".jpg", ".jpeg", ".png"]
    ])

    # Skip folders that contain no images
    if not image_files:
        ax.axis("off")
        continue

    # Open the first image and convert it to RGB
    with Image.open(image_files[0]) as img:
        image = img.convert("RGB")

    # Display the leaf image
    ax.imshow(image)

    # Display the disease category as the title
    ax.set_title(folder.name.replace("_", " "), fontsize=8)

    # Hide x-axis and y-axis
    ax.axis("off")

# Adjust the spacing between images
plt.tight_layout()

# Save the visualization for our final report
results_path = project_folder / "results"
results_path.mkdir(exist_ok=True)

plt.savefig(results_path / "sample_images.png", dpi=300)

# Display the figure
plt.show()

print("Sample images visualization saved successfully!")
