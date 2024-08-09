import reportlab.pdfgen.canvas as canvas
from reportlab.lib.pagesizes import letter  # Adjust page size as needed
from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
def get_gemini_response(question):
  response=chat.send_message(question,stream=True)
  return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
  st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
  response=get_gemini_response(input)
  # Add user query and response to session state chat history
  st.session_state['chat_history'].append(("You", input))
  st.subheader("The Response is")
  for chunk in response:
    st.write(chunk.text)
    st.session_state['chat_history'].append(("Bot", chunk.text))

  # Add button for PDF download
  if st.button("Download PDF"):
    # Generate PDF content
    pdf_text = "\n".join([f"{role}: {text}" for role, text in st.session_state['chat_history']])

    # Create a new PDF document
    pdf = canvas.Canvas("chat_history.pdf", pagesize=letter)

    # Add title and set font
    pdf.setFont("Helvetica", 16)
    pdf.drawString(100, 700, "Chat History")

    # Add chat history content with proper line spacing
    y_pos = 650
    line_height = 15
    for text in pdf_text.splitlines():
      pdf.drawString(50, y_pos, text)
      y_pos -= line_height

    # Save the PDF document
    pdf.save()

    st.success("Chat history downloaded as chat_history.pdf")

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
  st.write(f"{role}: {text}")
