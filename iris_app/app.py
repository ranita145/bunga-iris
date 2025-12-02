import streamlit as st
import pandas as pd
import numpy as np
# Assuming 'predict' function is in a file named 'prediction.py'
from prediction import predict 

st.title('Classifying Iris Flowers')
st.markdown(
    'Toy model to play to classify iris flowers into \
    (setosa, versicolor, virginica) based on their sepal/petal \
    and length/width.'
)

st.header("Plant Features")
col1, col2 = st.columns(2)

with col1:
    st.text("Sepal characteristics")
    # Sepal length slider (Min: 1.0, Max: 8.0, Step: 0.5)
    sepal_l = st.slider('Sepal lenght (cm)', 1.0, 8.0, 0.5) 
    # Sepal width slider (Min: 2.0, Max: 4.4, Step: 0.5)
    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5) 

with col2:
    st.text("Petal characteristics")
    # Petal length slider (Min: 1.0, Max: 7.0, Step: 0.5)
    petal_l = st.slider('Petal lenght (cm)', 1.0, 7.0, 0.5)
    # Petal width slider (Min: 0.1, Max: 2.5, Step: 0.5)
    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)

st.text('') # Empty text for spacing

if st.button("Predict type of Iris"):
    # Create a NumPy array with the input features
    # Note: Ensure your 'predict' function accepts this format
    input_data = np.array([[sepal_l, sepal_w, petal_l, petal_w]])
    
    # Call the prediction function
    result = predict(input_data)
    
    # Display the prediction result
    st.text(result[0]) 

st.text('')
st.text('')
st.markdown('')