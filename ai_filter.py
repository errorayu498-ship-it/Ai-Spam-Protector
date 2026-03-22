import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def check_message(content):

    prompt = f"""
    Detect if this message contains:
    - spam
    - scam links
    - discord server ads
    - nude sites
    - grabber links
    - nuke tools
    - malicious links

    Message: {content}

    Answer only SAFE or BLOCK
    """

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
