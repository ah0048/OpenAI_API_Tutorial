'''3. Displaying Streaming Responses Interactively'''
from openai import OpenAI

# Instantiate the client.
client = OpenAI(api_key="API_KEY")

# Create a streaming chat completion request.
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful software developer."},
        {"role": "user", "content": "Explain recursion in detail with examples in python."}
    ],
    stream=True  # Enable streaming responses.
)

# Process and print each chunk as it arrives.
for chunk in response:
    # Each chunk has a 'delta' attribute that may include new content.
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
