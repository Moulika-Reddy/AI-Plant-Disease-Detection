# AI-Based Plant Disease Detection Using Deep Learning

## Project Overview

This project aims to detect and classify plant leaf diseases using deep learning techniques. We are developing and comparing a custom Convolutional Neural Network (CNN) and a transfer-learning model based on MobileNetV2.

## Dataset

**Source:** [PlantVillage Dataset on Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)

The project focuses on three crops:

- Tomato — 10 classes
- Potato — 3 classes
- Bell Pepper — 2 classes

**Dataset summary:**

- Original images: 20,638
- Exact duplicate images removed: 14
- Cleaned images: 20,624
- Image dimensions: 256 × 256 pixels
- Corrupted images detected: 0

## Technologies

- Python 3.12
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Pillow
- ImageHash

## Completed Work

1. Dataset download and exploration
2. Class distribution analysis
3. Visualization of sample images
4. Image quality verification
5. Exact duplicate removal
6. Provisional stratified training, validation, and testing split
7. Initial perceptual-hash screening

## Dataset Splitting

| Dataset | Images | Percentage |
|---|---:|---:|
| Training | 14,436 | 70% |
| Validation | 3,094 | 15% |
| Testing | 3,094 | 15% |

These splits are provisional until additional near-duplicate checks are completed.

## How to Run

Download the PlantVillage dataset from Kaggle and extract it into:

`data/raw/PlantVillage/`

Install the required Python libraries and run the scripts in this order:

```bash
python src/explore_dataset.py
python src/visualize_dataset.py
python src/check_dataset.py
python src/clean_dataset.py
python src/split_dataset.py
python src/check_near_duplicates.py
```

## Upcoming Work

- Near-duplicate image investigation
- Final training, validation, and testing splits
- Image preprocessing and augmentation
- Custom CNN model development
- MobileNetV2 transfer learning
- Model evaluation using accuracy, precision, recall, and F1-score
- Testing model performance on unfamiliar images
