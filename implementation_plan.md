# AI-Generated vs Real Image Detection - Implementation Plan

## Goal Description
Build a machine learning pipeline to distinguish AI-generated images from real photographs.
The project will use Jupyter Notebooks for all stages: data preprocessing, model training, and evaluation.
We will use EfficientNet-B0 as the primary model and ResNet50 for comparison.

## User Review Required
> [!IMPORTANT]
> The dataset is expected to be in `Mtech_Project/dataset/train` and `Mtech_Project/dataset/test`.
> I will create the directories, but the user must populate them with images.

## Proposed Changes

### Project Structure
Create the following directory structure inside `Mtech_Project/`:
- `dataset/`
    - `train/`
    - `test/`
- `models/`
    - `efficientnet/`
    - `resnet/`

### Data Preprocessing
*merged into model notebooks*

### EfficientNet Model
#### [NEW] [models/efficientnet/EfficientNet.ipynb](file:///Users/kumarshubham/git/Mtech_Project/models/efficientnet/EfficientNet.ipynb)
- **Data Loading & Preprocessing**:
    - Use `tf.keras.utils.image_dataset_from_directory`
    - Standardization (Resize to 224x224, RGB)
    - Normalization (Rescaling 1./255)
    - Augmentation (`tf.keras.layers.RandomFlip`, `RandomRotation`)
- **Model**:
    - Load `tf.keras.applications.EfficientNetB0`
    - Modify final layer for binary classification
- **Training & Eval**:
    - Compile with `Adam` optimizer and `BinaryCrossentropy`
    - Training callbacks (ModelCheckpoint)
    - Evaluation metrics (Accuracy, Precision, Recall)

### ResNet Model (Comparison)
#### [NEW] [models/resnet/ResNet.ipynb](file:///Users/kumarshubham/git/Mtech_Project/models/resnet/ResNet.ipynb)
- **Data Loading & Preprocessing**: Same pipeline as EfficientNet
- **Model**: Load `tf.keras.applications.ResNet50`
- **Training & Eval**: Same training/eval setup

### GAN Discriminator Experiments
#### [NEW] [models/ganmodel/GAN_resnet.ipynb](file:///Users/kumarshubham/git/Mtech_Project/models/ganmodel/GAN_resnet.ipynb)
- **Concept**: Use ResNet50 as a strong GAN Discriminator baseline.
- **Architecture**: `tf.keras.applications.ResNet50` (frozen/unfrozen stages) + Classification Head.
- **Monitoring**: Psutil-based system monitoring.

#### [NEW] [models/ganmodel/GAN_xception.ipynb](file:///Users/kumarshubham/git/Mtech_Project/models/ganmodel/GAN_xception.ipynb)
- **Concept**: Use Xception, the industry standard for DeepFake/AI detection.
- **Architecture**: `tf.keras.applications.Xception` + Classification Head.
- **Monitoring**: Psutil-based system monitoring.

### Documentation
#### [NEW] [Copy Artifacts]
- Copy `task.md`, `stories.md`, `implementation_plan.md`, `walkthrough.md` to `Mtech_Project/`

## Verification Plan

### Automated Verification
- Run `models/efficientnet/EfficientNet.ipynb` to verify data loading, preprocessing, and training loop.
- Run `models/resnet/ResNet.ipynb` to verify the second model.

### Manual Verification
- Inspect the output logs in the notebooks.
- Check if model checkpoints are saved.
