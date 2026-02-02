# Project Stories & Backlog

## Backlog

### Story 1: Project Setup & Environment
**As a** Developer
**I want to** initialize the `Mtech_Project` repository with the required directory structure
**So that** I have a clean workspace for datasets and models.
- [x] Create `dataset/train` and `dataset/test` folders
- [x] Create `models/efficientnet` and `models/resnet` folders

### Story 2: Data Pipeline & EfficientNet Baseline
**As a** Researcher
**I want to** load, resize (224x224), and normalize images in a Jupyter Notebook and train an EfficientNet-B0 model
**So that** I can establish a baseline for detecting AI-generated images.
- [x] Create `models/efficientnet/EfficientNet.ipynb`
- [x] Implement image cleaning (remove corrupted)
- [x] Implement transformations (Resize, Norm, Augmentation)
- [x] Load EfficientNet-B0 (pretrained) and modify head
- [x] Implement training loop and save best model
- [x] Evaluate Accuracy, Precision, Recall, F1

### Story 3: Compare with ResNet50
**As a** Researcher
**I want to** train a ResNet50 model using the same preprocessing steps
**So that** I can compare its performance against Real vs AI detection.
- [x] Create `models/resnet/ResNet.ipynb`
- [x] Reuse/Re-implement data pipeline
- [x] Train ResNet50
- [x] Compare metrics with EfficientNet

### Story 4: Documentation & Walkthrough
**As a** Stakeholder
**I want to** see a walkthrough of the results and code
**So that** I can verify the reproducibility and performance.
- [x] Create `walkthrough.md` with results summary

### Story 5: GAN Classifier & Performance Metrics
**As a** Researcher
**I want to** train a GAN-based Discriminator and measure system resource usage (CPU/RAM/Disk)
**So that** I can assess if a custom architecture is more efficient or accurate than pretrained models.
- [x] Create `models/ganmodel/`
- [x] Implement DCGAN Discriminator as Binary Classifier
- [x] Implement `psutil` logging for performance metrics
- [x] Train and Compare

## In Progress
*(None)*

## Done
### Story 1: Project Setup & Environment
- [x] Create `dataset/train` and `dataset/test` folders
- [x] Create `models/efficientnet` and `models/resnet` folders

### Story 2: Data Pipeline & EfficientNet Baseline
- [x] Create `models/efficientnet/EfficientNet.ipynb`
- [x] Implement image cleaning (remove corrupted)
- [x] Implement transformations (Resize, Norm, Augmentation)
- [x] Load EfficientNet-B0 (pretrained) and modify head
- [x] Implement training loop and save best model
- [x] Evaluate Accuracy, Precision, Recall, F1

### Story 3: Compare with ResNet50
- [x] Create `models/resnet/ResNet.ipynb`
- [x] Reuse/Re-implement data pipeline
- [x] Train ResNet50
- [x] Compare metrics with EfficientNet

### Story 4: Documentation & Walkthrough
- [x] Create `walkthrough.md` with results summary
