import streamlit as st
import os
import google.generativeai as genai
from googleapiclient.discovery import build
from textblob import TextBlob
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from dotenv import load_dotenv
from io import BytesIO

# Set page config as the first command
st.set_page_config(page_title="Q&A with Gemini")

# Load environment variables
load_dotenv()

# Configure Gemini Pro model (ensure API key is correctly set)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get Gemini response
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return [chunk.text for chunk in response]

# Google Search API (without CSE ID)
def google_search(query):
    service = build("customsearch", "v1", developerKey=os.getenv("GOOGLE_API_KEY"))
    # We don't pass CSE ID and instead query Google's general search
    res = service.cse().list(q=query).execute()
    return [item['snippet'] for item in res.get('items', [])]

# Generate PDF of chat history
def generate_pdf(chat_history):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 14)
    pdf.drawString(100, 750, "Chat History")
    pdf.setFont("Helvetica", 10)
    y_pos = 730
    line_height = 14
    for role, text in chat_history:
        if y_pos < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y_pos = 750
        pdf.drawString(50, y_pos, f"{role}: {text}")
        y_pos -= line_height
    pdf.save()
    buffer.seek(0)
    return buffer

# Streamlit app setup
st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_query = st.text_input("Ask a question:")
if st.button("Submit") and input_query:
    gemini_response = get_gemini_response(input_query)
    st.session_state['chat_history'].append(("You", input_query))
    st.subheader("Gemini Response")
    for chunk in gemini_response:
        st.write(chunk)
        st.session_state['chat_history'].append(("Bot", chunk))

    sentiment = TextBlob(input_query).sentiment.polarity
    if -0.1 < sentiment < 0.1:
        search_results = google_search(input_query)
        if search_results:
            st.write("Additional Resources from Web:")
            for result in search_results:
                st.write(f"- {result}")

    if st.button("Download Chat as PDF"):
        pdf_buffer = generate_pdf(st.session_state['chat_history'])
        st.download_button(label="Download PDF", data=pdf_buffer, file_name="chat_history.pdf", mime="application/pdf")
