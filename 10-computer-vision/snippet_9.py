def create_cassava_data_pipeline(
    data_dir: str,
    batch_size: int = 32,
    img_size: Tuple[int, int] = (224, 224),
    validation_split: float = 0.2
) -> Tuple[tf.data.Dataset, tf.data.Dataset, list]:
    """
    Create training and validation datasets for cassava disease classification.

    Expects directory structure:
    data_dir/
        CMD/
        CBSD/
        CGM/
        CBB/
    """
    train_ds = image_dataset_from_directory(
        directory,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=image_size,
        batch_size=batch_size
    )
    
    val_ds = image_dataset_from_directory(
        directory,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=image_size,
        batch_size=batch_size
    )

    # Performance optimization
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    return train_ds, val_ds, class_names

# Example usage (assuming data is available)
# train_ds, val_ds, class_names = create_cassava_data_pipeline('cassava_images/')
# history = cassava_model.fit(train_ds, validation_data=val_ds, epochs=20)