import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Extract text from PDF
def get_pdf_text(pdf_docs):
    return "".join(page.extract_text() for pdf in pdf_docs for page in PdfReader(pdf).pages)

# Split text into chunks
def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return splitter.split_text(text)

# Generate vector store
def get_vector_store(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    store = FAISS.from_texts(chunks, embedding=embeddings)
    store.save_local("faiss_index")

# Create LangChain conversational chain
def get_conversational_chain():
    prompt = PromptTemplate(template="""
    Answer the question based only on the provided context. If unknown, state "answer is not available in the context."
    Context: {context}
    Question: {question}
    Answer:
    """, input_variables=["context", "question"])
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)

# Handle user queries
def handle_user_query(question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = store.similarity_search(question)
    response = get_conversational_chain()({"input_documents": docs, "question": question}, return_only_outputs=True)
    st.write("Reply:", response["output_text"])

# Main Streamlit app
def main():
    st.set_page_config(page_title="Chat with PDF")
    st.header("Chat with PDF 💬")

    question = st.text_input("Ask a question from the uploaded PDFs")
    if question:
        handle_user_query(question)

    with st.sidebar:
        st.title("Menu")
        pdf_files = st.file_uploader("Upload PDF Files", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_files)
                get_vector_store(get_text_chunks(raw_text))
                st.success("Processing completed")

if __name__ == "__main__":
    main()
