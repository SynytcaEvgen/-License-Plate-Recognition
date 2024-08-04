from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Load a pretrained YOLOv8 model

model.train(
    data='dataset/data.yaml',
    epochs=25,
    imgsz=640,
    batch=4,  # Reduce batch size for CPU
    workers=2,  # Number of data loader workers (adjust based on your CPU)
    project='licens_plate',  # Project name for saving results
    exist_ok=True,  # Overwrite existing project
    device='cpu',  # Use CPU
    optimizer='AdamW',  # Use a more efficient optimizer
    lr0=0.01,  # Learning rate
    momentum=0.937,  # SGD momentum
    weight_decay=0.0005,  # Weight decay
    augment=True,  # Enable data augmentation
    multi_scale=True,  # Enable multi-scale training
    hsv_h=0.015,  # Hue augmentation
    hsv_s=0.7,  # Saturation augmentation
    hsv_v=0.4,  # Value augmentation
    translate=0.1,  # Translation augmentation
    scale=0.5,  # Scale augmentation
    shear=0.0,  # Shear augmentation
    perspective=0.0,  # Perspective augmentation
    flipud=0.0,  # Flip up-down augmentation
    fliplr=0.5,  # Flip left-right augmentation
    mosaic=True,  # Enable mosaic augmentation
    mixup=True,  # Enable mixup augmentation
    rect=False,  # Use rectangular training
    cache_images=False,  # Disable caching images for CPU
    sync_bn=False,  # Disable synchronized batch normalization
    workers=2,  # Number of data loader workers
    patience=10,  # Early stopping patience
    image_weights=True,  # Use weighted image selection for training
    cos_lr=True,  # Use cosine learning rate scheduling
    label_smoothing=0.1,  # Label smoothing factor
    seed=42,  # Random seed for reproducibility
    verbose=True  # Verbose output
)
