# Adding Batch Normalization to a convolutional block
layers.Conv2D(64, (3, 3), padding='same'),
layers.BatchNormalization(),
layers.Activation('relu'),