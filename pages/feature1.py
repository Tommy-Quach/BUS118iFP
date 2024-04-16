from openai import OpenAI
import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Focus on the damaged roads and potholes of the image. Assess the severity of damage include size and depth."},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://media.istockphoto.com/id/174662203/photo/pot-hole.jpg?s=612x612&w=0&k=20&c=HhFYQD5qAJItGzYWJJQ72nxBR8iidL7Np2g82dfvnoM=",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])