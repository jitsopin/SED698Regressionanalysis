import streamlit as st
import joblib
import pandas as pd
#Load the trained model
model =joblib.load('model-reg-67130701719.pkl')
# Streamlit App
st.title("Sales Prediction System")
#Input from the user
st.sidebar.header("Input Features")
youtube =st.sidebar.number_input("Youtube", min_value=0, max_value=100, value=50)
tiktok =st.sidebar.number_input("TikTok Ads Spend ($)", min_value=0.0, max_value=500.0, value=50.0)
instagram = st.sidebar.number_input("Instagram Ads Spend ($)", min_value=0.0, max_value=500.0, value=50.0)
# Prediction logic
if st.button("Predict Sales"):
    try:
        # Create a new DataFrame with user inputs
        new_data = pd.DataFrame({'youtube': [youtube], 'tiktok': [tiktok], 'instagram': [instagram]})
        
        # Make predictions
        predicted_sales = model.predict(new_data)
        
        # Display the prediction result
        st.subheader("Predicted Sales:")
        st.write(f"Estimated Sales: ${predicted_sales[0]:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
