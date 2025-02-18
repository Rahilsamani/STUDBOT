import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Verify if the API key is loaded correctly
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API key is not set in the environment variables.")
else:
    genai.configure(api_key=api_key)

# Function to load model and get response
def get_gemini_response(input, image):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')  # Update with an available model
        if input != "":
            response = model.generate_content([input, image])
        else:
            response = model.generate_content(image)
        return response.text
    except Exception as e:
        st.error(f"Error with Gemini API: {e}")
        return None

# Streamlit App Setup
st.set_page_config(page_title="Gemini Image Demo")
st.header("Pic Prompter")

# Input and image upload
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)  # Open image with PIL
        st.image(image, caption="Uploaded Image.", width=700)
    except Exception as e:
        st.error(f"Error loading image: {e}")

# Submit button to process the image
submit = st.button("Tell me about the image")

if submit:
    if image is not None:
        response = get_gemini_response(input, image)
        if response:
            st.subheader("The Response is")
            st.write(response)
    else:
        st.error("Please upload a valid image file.")
