import anthropic
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()

# Create the client
client = anthropic.Anthropic()

# Make the API call
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "In one sentence, what is the most common technology problem facing UK construction SMEs?"
        }
    ]
)

# Print the response
print(message.content[0].text)