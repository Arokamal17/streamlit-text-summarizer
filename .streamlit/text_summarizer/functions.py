import openai
import streamlit as st

def summarize(text):
    # Split the input text into chunks of maximum length 8192
    chunks = [text[i:i+8192] for i in range(0, len(text), 8192)]
    
    # Initialize the output summary
    summary = ""
    
    # Summarize each chunk and append the result to the output summary
    for chunk in chunks:
        augmented_prompt = f"summarize this text: {chunk}"
        try:
            response = openai.Completion.create(
                engine="Daniel",
                prompt=augmented_prompt,
                temperature=0.3,
                max_tokens=250,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                best_of=1,
                stop=None
            )
            summary += response.choices[0].ext.strip()+" "
        except:
            st.write('There was an error =(')
    # Return the final summary
    return summary