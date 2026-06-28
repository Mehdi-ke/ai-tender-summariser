import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

tender_text = """
Project: Refurbishment of Riverside Community Centre, Bristol
Client: Bristol City Council
Contract Value: £850,000
Programme: 24 weeks
Scope: Strip out and full internal refurbishment including M&E replacement,
new ceilings, flooring, decoration, and external works. Works to be carried
out while the building remains partially occupied.
Submission deadline: 14 days from issue.
Insurance requirements: £5m public liability, £2m employers liability.
Liquidated damages: £1,500 per week.
"""

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