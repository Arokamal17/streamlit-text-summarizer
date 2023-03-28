import openai
import streamlit as st

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