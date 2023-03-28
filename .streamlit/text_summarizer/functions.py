import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            engine="Daniel",
            prompt=augmented_prompt,
            temperature=1,
            max_tokens=None,
            top_p=0.5,
            frequency_penalty=0,
            presence_penalty=0,
            best_of=1,
            stop=None
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')