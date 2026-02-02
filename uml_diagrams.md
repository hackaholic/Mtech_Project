# Project UML Diagrams

These diagrams represent the end-to-end workflow implemented in the Jupyter Notebooks for `EfficientNet` and `ResNet` models.

## 1. EfficientNet Workflow

```mermaid
sequenceDiagram
    participant NB as Jupyter Notebook
    participant HF as HF Datasets (Parquet)
    participant Pipe as Data Pipeline (TF)
    participant Model as EfficientNetB0 (Keras)
    participant Train as Training Loop (Model.fit)

    Note over NB: 1. Load Modules & Config
    NB->>NB: Import tensorflow, datasets, sklearn

    Note over NB: 2. Load Dataset
    NB->>HF: load_dataset("parquet", files=...)
    HF-->>NB: Returns DatasetDict (Train/Val/Test)

    Note over NB: 3. Preprocessing
    NB->>Pipe: create_tf_dataset()
    loop For each image
        Pipe->>Pipe: process_example()
        Pipe->>Pipe: Decode Image (PIL/Bytes)
        Pipe->>Pipe: Resize (224, 224)
        Pipe->>Pipe: Convert to RGB
    end
    Pipe-->>NB: Returns tf.data.Dataset

    Note over NB: 4. Load & Build Model
    NB->>Model: build_model()
    Model->>Model: Load Pretrained Weights (ImageNet)
    Model->>Model: Freeze Base Layers
    Model->>Model: Add Augmentation (Flip, Rot, Zoom)
    Model->>Model: Add Top Layers (Pooling, Dropout, Dense)
    Model-->>NB: Returns Compiled Model

    Note over NB: 5. Training
    NB->>Train: model.fit(train_ds, val_ds)
    loop Each Epoch
        Train->>Pipe: Request Batch
        Pipe-->>Train: Image Batch + Labels
        Train->>Train: Forward Pass
        Train->>Train: Backprop & Update Weights
        Train->>Train: Checkpoint & Early Stopping
    end
    Train-->>NB: Returns History

    Note over NB: 6. Evaluation
    NB->>Train: model.evaluate(test_ds)
    Train-->>NB: Accuracy, Precision, Recall
```

## 2. ResNet-50 Workflow

```mermaid
sequenceDiagram
    participant NB as Jupyter Notebook
    participant HF as HF Datasets (Parquet)
    participant Pipe as Data Pipeline (TF)
    participant Model as ResNet50 (Keras)
    participant Train as Training Loop (Model.fit)

    Note over NB: 1. Load Modules & Config
    NB->>NB: Import tensorflow, datasets, sklearn

    Note over NB: 2. Load Dataset
    NB->>HF: load_dataset("parquet", files=...)
    HF-->>NB: Returns DatasetDict (Train/Val/Test)

    Note over NB: 3. Preprocessing
    NB->>Pipe: create_tf_dataset()
    loop For each image
        Pipe->>Pipe: process_example()
        Pipe->>Pipe: Decode Image (PIL/Bytes)
        Pipe->>Pipe: Resize (224, 224)
        Pipe->>Pipe: Convert to RGB
    end
    Pipe-->>NB: Returns tf.data.Dataset

    Note over NB: 4. Load & Build Model
    NB->>Model: build_model()
    Model->>Model: Load Pretrained Weights (ImageNet)
    Model->>Model: Freeze Base Layers
    Model->>Model: Add Augmentation (Flip, Rot, Zoom)
    Model->>Model: Add Specific ResNet Preprocessing
    Model->>Model: Add Top Layers (Pooling, Dropout, Dense)
    Model-->>NB: Returns Compiled Model

    Note over NB: 5. Training
    NB->>Train: model.fit(train_ds, val_ds)
    loop Each Epoch
        Train->>Pipe: Request Batch
        Pipe-->>Train: Image Batch + Labels
        Train->>Train: Forward Pass
        Train->>Train: Backprop & Update Weights
        Train->>Train: Checkpoint & Early Stopping
    end
    Train-->>NB: Returns History

    Note over NB: 6. Evaluation
    NB->>Train: model.evaluate(test_ds)
    Train-->>NB: Accuracy, Precision, Recall
```
