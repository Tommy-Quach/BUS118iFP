from openai import OpenAI

client = OpenAI()


response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What's in this image?"},
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
