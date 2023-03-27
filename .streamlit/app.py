import streamlit as st
import openai
import os
import requests
from text_summarizer.functions import summarize

try:
  openai.api_type = "azure"
  openai.api_base = "https://chat-gpt-a1.openai.azure.com/"
  openai.api_version = "2022-12-01"
  openai.api_key = os.getenv("OPENAI_API_KEY")
  # openai.api_key = os.getenv('OPENAI_KEY')
  
  if "summary" not in st.session_state:
      st.session_state["summary"] = ""
  
  st.title("Text Summarizer")

  input_type = st.radio(
      "Select input type:",
      ("Document link", "Text")
  )

  if input_type == "Document link":
      document_url = st.text_input("Enter document link:")
      if document_url:
          response = requests.get(document_url)
          if response.status_code == 200:
              input_text = response.text
              st.write(f"Document summary for: {document_url}")
              st.write(f"{input_text[:100]}...")
          else:
              st.write("Error: Failed to retrieve document from URL.")
  else:
      input_text = st.text_area(label="Enter full text:", value="", height=250)

  if input_text:
    st.button(
      "Submit",
      on_click=summarize,
      kwargs={"prompt": input_text},
    )
    output_text = st.text_area(label="Summarized text:", value=st.session_state.get("summary", ""), height=250)
  else:
    st.write("Please input text or document link.")
  
except:
      st.write('There was an error =(')

