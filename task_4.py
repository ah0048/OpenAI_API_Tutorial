'''4. Creating an API Endpoint in Flask That Forwards a Request to OpenAI while handling errors and streaming response'''
from flask import Flask, request, Response, stream_with_context, jsonify
from openai import OpenAI, RateLimitError, APIConnectionError

# Instantiate the OpenAI client with openai API key.
client = OpenAI(api_key="API_KEY")

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("prompt")
    if not user_message:
        return jsonify({"error": "No prompt provided"}), 400

    # Define a generator that sends the request to OpenAI and yields each chunk.
    def generate():
        try:
            # Create a streaming chat completion request
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ],
                stream=True
            )
            # Yield each part of the streamed response as it arrives.
            for chunk in response:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    yield delta.content
        except RateLimitError:
            yield "Rate limit exceeded. Please wait and try again later."
        except APIConnectionError:
            yield "Network error: Unable to connect to the API. Check your connection."
        except Exception as e:
            yield f"An unexpected error occurred: {str(e)}"

    # Return a streaming response with MIME type text/plain.
    return Response(stream_with_context(generate()), mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
