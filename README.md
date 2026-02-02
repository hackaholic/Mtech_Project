# AI-Generated vs Real Image Detection (MTech Project)

## Project Overview
This project aims to develop and compare deep learning models for distinguishing between **AI-generated images** (e.g., Midjourney) and **Real photographs**.
The study evaluates the effectiveness of standard CNN architectures versus Generative Adversarial Network (GAN) discriminators in detecting synthetic media.

## Models Implemented
The project includes three primary approaches:

1.  **EfficientNet-B0**: A lightweight, efficient baseline classifier.
2.  **ResNet-50**: A standard, deep residual network for comparison.
3.  **GAN Discriminators**: Custom discriminators trained to classify Real vs Fake.
    *   **ResNet-Backbone Discriminator**
    *   **Xception-Backbone Discriminator** (Industry standard for DeepFake detection)

## Features
*   **Parquet Data Loading**: Efficient data streaming from Hugging Face / Parquet files.
*   **System Monitoring**: Real-time tracking of **CPU, RAM, Disk I/O, and GPU** usage during training.
*   **Comparison Metrics**: Accuracy, Precision, Recall, and F1-Score evaluation.

## Repository Structure
```
Mtech_Project/
├── models/
│   ├── efficientnet/
│   │   └── EfficientNet.ipynb   # EfficientNet-B0 Implementation
│   ├── resnet/
│   │   └── ResNet.ipynb         # ResNet-50 Comparison
│   └── ganmodel/
│       ├── GAN_Classifier.ipynb # Basic DCGAN Discriminator
│       ├── GAN_resnet.ipynb     # GAN Discriminator (ResNet50)
│       └── GAN_xception.ipynb   # GAN Discriminator (Xception)
├── implementation_plan.md       # Technical Development Plan
├── walkthrough.md               # Step-by-step Usage Guide
└── requirements.txt             # (Dependencies listed in notebooks)
```

## Setup & Requirements
The project is designed to run in **Jupyter Notebooks** (Linux/Mac).

### Prerequisites
*   Python 3.8+
*   TensorFlow
*   Hugging Face `datasets`
*   `psutil` (for CPU/RAM monitoring)
*   `nvidia-smi` (for GPU monitoring on Linux)

### Dataset
This project uses the **AIGeneratedImages_Midjourney** dataset.
*   **Source**: [ideepankarsharma2003/AIGeneratedImages_Midjourney](https://huggingface.co/datasets/ideepankarsharma2003/AIGeneratedImages_Midjourney)
*   **Description**: A collection of AI-generated images from Midjourney, useful for training DeepFake detection models.

### Installation
Install the required libraries:
```bash
pip install tensorflow datasets pandas pyarrow psutil matplotlib scikit-learn
```

## Usage
1.  **Configure Data Paths**:
    Open any notebook and verify the `DATA_FILES` dictionary matches your Parquet file locations:
    ```python
    DATA_FILES = {
        "train": "/path/to/train-*.parquet",
        ...
    }
    ```

2.  **Run Experiments**:
    *   **Baseline**: Run `models/efficientnet/EfficientNet.ipynb`.
    *   **Comparison**: Run `models/resnet/ResNet.ipynb`.
    *   **GAN Experiment**: Run `models/ganmodel/GAN_xception.ipynb`.

3.  **View Performance**:
    After training, each notebook displays comphrehensive plots for Model Accuracy and System Resource Usage.

## License
MTech Project - All Rights Reserved.
