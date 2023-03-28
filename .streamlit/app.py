import streamlit as st
import openai
import os
import requests
# from text_summarizer.functions import summarize

def summarize(prompt):
    chunk_size = 8000
    chunks = [prompt[i:i+chunk_size] for i in range(0, len(prompt), chunk_size)]
    summary = []
    for chunk in chunks:
        augmented_prompt = f"summarize this text: {chunk}"
    try:
        response = openai.Completion.create(
            engine="Daniel",
            prompt=augmented_prompt,
            temperature=1,
            max_tokens=100,
            top_p=0.5,
            frequency_penalty=0,
            presence_penalty=0,
            best_of=1,
            stop=None
        )
        summary.append(response.choices[0].text.strip())
    except Exception as e:
            st.write('Error:', e)
            return None
    return '\n'.join(summary)

try:
  openai.api_type = "azure"
  openai.api_base = "https://chat-gpt-a1.openai.azure.com/"
  openai.api_version = "2022-12-01"
  openai.api_key = os.getenv("OPENAI_API_KEY")
  
  


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
        try:
            # fetch the document text using requests.get() or any other method
            document_text = requests.get(input_url)
            summary =  summarize(document_text.text)
            if summary:
              st.session_state["summary"] = summary
              st.text_area(label="Summarized text:", value=summary, height=250)
        except:
              st.write("Invalid URL or unable to retrieve content.")

except:
    st.write('There was an error =(')

