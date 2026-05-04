def build_transfer_learning_model(
    num_classes: int,
    input_shape: Tuple[int, int, int] = (224, 224, 3),
    base_model_name: str = 'ResNet50',
    freeze_base: bool = True
) -> keras.Model:
    """
    Build a transfer learning model using a pre-trained base.

    Args:
        num_classes: Number of output classes
        input_shape: Input image dimensions (ResNet expects 224x224)
        base_model_name: Name of pre-trained model to use
        freeze_base: Whether to freeze base model weights
    """
    # Load base model
    if base_model_name == 'MobileNetV2':
        base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    else:
        base_model = ResNet50V2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        
    if freeze_base:
        base_model.trainable = False
        
    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dropout(0.5),
        Dense(128, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    
    return model

cassava_model = build_transfer_learning_model(num_classes=5)

cassava_model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print(f"Total parameters: {cassava_model.count_params():,}")
print(f"Trainable parameters: {sum(np.prod(v.shape) for v in cassava_model.trainable_weights):,}")