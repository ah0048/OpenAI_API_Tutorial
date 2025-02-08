'''1. Sending a Request to the ChatGPT API and Printing the Response'''
from openai import OpenAI

# Instantiate a client with the openai API key
client = OpenAI(api_key="API_KEY")

# Create a chat completion request using the new interface
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful software developer."},
        {"role": "user", "content": "Explain recursion in detail with examples in python."}
    ]
)

# Print the assistant's reply using the updated attribute access
print(response.choices[0].message.content)
