import openai
import os
import streamlit as st


def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            engine="text-davinci-003",
            prompt=augmented_prompt,
            temperature=0.3,
            max_tokens=250,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            best_of=1,
            stop=None
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')