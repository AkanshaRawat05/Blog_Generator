import streamlit as st
import cohere

# Initialize Cohere client
co = cohere.Client('EIeOEUCzDNoMzhjTGMW1VDX6nS7x1RQs0BXfCYAW')

# Streamlit app
st.title("Blog Generator")
user_prompt = st.text_input("Enter a prompt to generate text:")

if st.button("Generate Blog"):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=user_prompt,
        max_tokens=700,
        temperature=1,
    )
    st.text_area("Generated Blog:", value=response.generations[0].text, height=300)
