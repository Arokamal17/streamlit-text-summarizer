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

  if input_type == "Text":
    input_text = st.text_area(label="Enter full text:", value="", height=250)
    if st.button("Submit"):
        st.session_state["summary"] = summarize(input_text)

  elif input_type == "Document link":
      url = st.text_input("Enter the URL of the webpage:", "")
      if st.button("Submit"):
          try:
              response = requests.get(url)
              st.session_state["summary"] = summarize(response.text)
          except:
              st.write("Invalid URL or unable to retrieve content.")
              
  output_text = st.text_area(label="Summarized text:", value=st.session_state.get("summary", ""), height=250)
except:
      st.write("Please input text or document link.")

