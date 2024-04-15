import os
import openai
import streamlit as st
from openai import OpenAI


st.markdown("# Page 1: Text Generation And Analysis")
st.divider()
st.sidebar.markdown("# Page 1: Text Generation")

openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "Your job is to analyze text based on user input and educate users on potholes."},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content


with st.form(key = "chat"):
    prompt = st.text_input("What would you like to know about potholes or do you have any potholes you'd like to add to the map?: ") 
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(get_completion(prompt))