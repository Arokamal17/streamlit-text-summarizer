import streamlit as st
import openai
import os
from text_summarizer.functions import summarize

try:
  openai.api_key = "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"
  
  if "summary" not in st.session_state:
      st.session_state["summary"] = ""
  
  st.title("Text Summarizer")
  users_input_type = st.radio('Select input type', ('Text', 'URL'))
  if users_input_type == "Text":
      input_text = st.text_area(label="Enter full text:", value="", height=250)
      st.button(
            "Submit",
            on_click=summarize,
            kwargs={"prompt": input_text},
            )
      output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)
except:
  st.write('There was an error =(')

    # OPENAI_API_KEY = ''
    # with open('.\key.json', 'r') as file_to_read:
    #     json_data = json.load(file_to_read)
    #     OPENAI_API_KEY = json_data["OPENAI_API_KEY"]
    # openai.api_key = os.getenv('OPENAI_KEY')