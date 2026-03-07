import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are InternTrack AI.

You have TWO MODES:

1) InternTrack
Help students track internship hours, progress, tasks, and reports.

2) MentorBridge
Help students communicate professionally with supervisors.

Detect the user intent automatically.

If internship related → InternTrack
If workplace communication → MentorBridge
"""

def chat_ai(message):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":message}
        ]
    )

    return {"reply": response.choices[0].message.content}