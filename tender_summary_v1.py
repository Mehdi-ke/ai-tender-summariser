import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

filename = input("Enter tender file name (e.g. tender.txt): ")
with open(filename, "r") as f:
    tender_text = f.read()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"""You are a construction estimating assistant. 
Analyse the following tender summary and extract:
1. Scope of works (bullet points)
2. Key risks
3. Commercial watch points
4. Questions to raise with client

Tender text:
{tender_text}"""
        }
    ]
)

print(message.content[0].text)