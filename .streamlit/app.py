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
    
    input_text = st.text_area(label="Enter full text:", value="", height=250)
    st.button(
        "Submit",
        on_click=summarize,
        kwargs={"prompt": input_text},
    )
    output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)
except:
  st.write('There was an error =(')

