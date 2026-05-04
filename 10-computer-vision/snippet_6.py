def residual_block(x: tf.Tensor,
                   filters: int,
                   kernel_size: int = 3) -> tf.Tensor:
    """
    Create a residual block with skip connection.

    Args:
        x: Input tensor
        filters: Number of filters in conv layers
        kernel_size: Size of convolution kernel

    Returns:
        Output tensor with residual connection
    """
    # Save the input for the skip connection
    shortcut = x

    # Main path
    x = layers.Conv2D(filters, kernel_size, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)

    x = layers.Conv2D(filters, kernel_size, padding='same')(x)
    x = layers.BatchNormalization()(x)

    # If dimensions don't match, project shortcut
    if shortcut.shape[-1] != filters:
        shortcut = layers.Conv2D(filters, (1, 1), padding='same')(shortcut)
        shortcut = layers.BatchNormalization()(shortcut)

    # Add skip connection
    x = layers.Add()([x, shortcut])
    x = layers.Activation('relu')(x)

    return x