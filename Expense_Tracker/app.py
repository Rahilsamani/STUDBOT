import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini 1.5 model (or another available model)
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get Gemini response
def get_gemini_response(prompt, image, user_input):
    response = model.generate_content([prompt, image[0], user_input])
    return response.text

# Function to process uploaded image
def input_image_details(uploaded_file):
    if uploaded_file:
        return [{
            "mime_type": uploaded_file.type,
            "data": uploaded_file.getvalue()
        }]
    st.error("Please upload an image file.")
    return None

# Streamlit App Configuration
st.set_page_config(page_title="MultiLanguage Student Expense Extractor")
st.header("MultiLanguage Student Expense Extractor")

input_prompt = "You are an expert in understanding student expense invoices. Use the uploaded invoice image to answer questions."
user_input = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an invoice image (jpg, jpeg, png):", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(Image.open(uploaded_file), caption="Uploaded Image", use_container_width=True)

if st.button("Analyze Invoice"):
    image_data = input_image_details(uploaded_file)
    if image_data:
        with st.spinner("Analyzing invoice..."):
            response = get_gemini_response(input_prompt, image_data, user_input)
            st.subheader("Invoice Analysis Result:")
            st.write(response)
