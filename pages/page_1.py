from openai import OpenAI
import streamlit as st
import base64
import requests

client = OpenAI()

st.markdown("# Page 1 Road Status Detection")
st.sidebar.markdown("# Page 1 Road Status Detection")

response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Are there potholes?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
