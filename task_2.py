'''2. Handling Errors (Rate Limit & Network Errors)'''
from openai import OpenAI
from openai import RateLimitError, APIConnectionError

# Instantiate the client with openai API key.
client = OpenAI(api_key="API_KEY")

def get_chat_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful software developer."},
                {"role": "user", "content": prompt}
            ]
        )
        # Use attribute access on the Pydantic model returned
        return response.choices[0].message.content
    except RateLimitError:
        print("Rate limit exceeded. Please wait and try again later.")
    except APIConnectionError:
        print("Network error: Unable to connect to the API. Check your connection.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    return ""

if __name__ == "__main__":
    prompt = "Explain recursion in detail with examples in python."
    result = get_chat_response(prompt)
    if result:
        print(result)
