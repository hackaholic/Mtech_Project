# AI vs Real Image Detection - Walkthrough

## Project Overview
This project distinguishes AI-generated images from real photographs using Deep Learning (CNNs).
We have implemented two models for comparison:
1. **EfficientNet-B0**: A lightweight, efficient baseline.
2. **ResNet-50**: A standard, deeper architecture for comparison.

All code is implemented using **TensorFlow/Keras** and contained in self-sufficient Jupyter Notebooks.

## 1. Directory Structure
The project is organized as follows:
```
Mtech_Project/
├── dataset/             # (Not used with Parquet loading)
├── models/
│   ├── efficientnet/
│   │   └── EfficientNet.ipynb  # Main notebook for EfficientNet
│   └── resnet/
│       └── ResNet.ipynb        # Main notebook for ResNet comparison
```

## 2. Setup & Dataset
The project is configured to load data directly from Parquet files located at:
- `/storage/AIGeneratedImages_Midjourney/data/train-*.parquet`
- `/storage/AIGeneratedImages_Midjourney/data/validation-*.parquet`
- `/storage/AIGeneratedImages_Midjourney/data/test-*.parquet`

**No manual dataset copying is required** if these paths are accessible.

## 3. Running the Experiments

### Experiment 1: EfficientNet Baseline
1. Open terminal and run `jupyter notebook`.
2. Navigate to `Mtech_Project/models/efficientnet/EfficientNet.ipynb`.
3. fast-forward through the "Imports" and "Configuration" cells.
4. **Data Cleaning**: The notebook includes a cell to remove corrupted images. Uncomment and run it if unsure about data quality.
5. **Training**: Run the training loop. Validations metrics (Accuracy, F1) are printed every epoch.
6. **Evaluation**: The final cell evaluates the model on the `test` set.

### Experiment 2: ResNet Comparison
1. Open `Mtech_Project/models/resnet/ResNet.ipynb`.
2. Run the cells similar to Experiment 1.
3. Compare the "Best Validation Accuracy" and "Test Set Metrics" with EfficientNet.

## 4. Verification
To verify the setup without training for long:
- Set `NUM_EPOCHS = 1` in the "Configuration" section of the notebooks.
- Run all cells.
- Ensure `efficientnet_b0_best.keras` and `resnet50_best.keras` are created.
