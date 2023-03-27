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
      input_type = st.radio('Select input type', ('Text', 'URL'))
      if input_type == 'Text':
          input_text = st.text_area(label="Enter full text:", value="", height=250)
          if st.button("Submit"):
              summary = summarize(input_text)
              if summary:
                  st.session_state["summary"] = summary
                  st.text_area(label="Summarized text:", value=summary, height=250)
      else:
          input_url = st.text_input(label="Enter document URL:", value="")
          if st.button("Submit"):
              # fetch the document text using requests.get() or any other method
              document_text = ""
              summary = summarize(document_text)
              if summary:
                  st.session_state["summary"] = summary
                  st.text_area(label="Summarized text:", value=summary, height=250)

except:
    st.write('There was an error =(')

