# app/streamlit_app.py
"""
Maize Disease Detection - Streamlit Interface

A simple web application for farmers to upload leaf images
and receive disease predictions.
"""
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from pathlib import Path
from typing import Tuple, Dict
import plotly.express as px

@st.cache_resource
def load_model(model_path: str = "models/maize_disease_model.h5"):
    """Load the trained model (cached across sessions)."""
    return tf.keras.models.load_model(model_path)

def preprocess_image(image: Image.Image, target_size: Tuple = (224, 224)):
    """Resize and normalize an uploaded image for prediction."""
    img = image.resize(target_size)
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

def main():
    st.title("Maize Disease Detective")
    st.write("Upload a photo of a maize leaf for disease diagnosis.")

    model = load_model()
    class_names = ["Healthy", "Leaf Blight", "Common Rust", "Gray Leaf Spot"]

    uploaded_file = st.file_uploader("Choose a leaf image", type=["jpg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded leaf image", use_column_width=True)

        processed = preprocess_image(image)
        predictions = model.predict(processed)[0]
        predicted_class = class_names[np.argmax(predictions)]
        confidence = float(np.max(predictions))

        st.subheader(f"Diagnosis: {predicted_class}")
        st.metric("Confidence", f"{confidence:.1%}")

        fig = px.bar(x=class_names, y=predictions, labels={"x": "Class", "y": "Probability"})
        st.plotly_chart(fig)

        if predicted_class != "Healthy":
            st.warning(f"""
                **Recommended actions for {predicted_class}:**
                - Document the affected area
                - Isolate affected plants if possible
                - Contact your local agricultural extension office
                - Consider appropriate treatment options
                """)
    else:
        st.info("Upload an image to see predictions")

if __name__ == "__main__":
    main()