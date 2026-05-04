def build_sentiment_model(vocab_size: int,
                          embedding_dim: int,
                          max_length: int,
                          lstm_units: int = 32,
                          bidirectional: bool = True,
                          dropout_rate: float = 0.3) -> keras.Model:
    """
    Build an LSTM model for binary sentiment classification.

    Args:
        vocab_size: Size of the vocabulary
        embedding_dim: Dimension of word embeddings
        max_length: Maximum sequence length
        lstm_units: Number of LSTM units
        bidirectional: Whether to use bidirectional LSTM
    """
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_dim, input_length=max_length))
    
    if bidirectional:
        model.add(Bidirectional(LSTM(lstm_units)))
    else:
        model.add(LSTM(lstm_units))
        
    model.add(Dense(24, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

vocab_size = 1000
embedding_dim = 32
model = build_sentiment_model(
    vocab_size=vocab_size,
    embedding_dim=embedding_dim,
    max_length=max_length,
    lstm_units=32,
    bidirectional=True
)

model.summary()