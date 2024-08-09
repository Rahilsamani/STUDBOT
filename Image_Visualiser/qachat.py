import reportlab.pdfgen.canvas as canvas
from reportlab.lib.pagesizes import letter  # Adjust page size as needed
from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from googleapiclient.discovery import build  # For Google CSE API

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
def get_gemini_response(question):
  response=chat.send_message(question,stream=True)
  return response

## Google Custom Search Engine API (replace with your details)
YOUR_CSE_ID = "YOUR_CSE_ID"
YOUR_API_KEY = "YOUR_API_KEY"
def google_search(query):
  service = build("customsearch", "v1", developerKey=YOUR_API_KEY)
  res = service.cse().list(
      q=query, cx=YOUR_CSE_ID
  ).execute()
  if not 'items' in res:
    return []
  return [item['snippet'] for item in res['items']]

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

  # Sentiment analysis using TextBlob
  from textblob import TextBlob
  sentiment = TextBlob(input).sentiment.polarity

  # Perform web search based on query (if sentiment is neutral)
  if -0.1 < sentiment < 0.1:
    search_results = google_search(input)
    if search_results:
      st.write("Here are some additional resources from the web:")
      for result in search_results:
        st.write(f"- {result}")

  # Print chat history length for debugging
  print(f"Chat history length: {len(st.session_state['chat_history'])}")

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
