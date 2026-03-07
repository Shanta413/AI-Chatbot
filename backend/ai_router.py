import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MENTORBRIDGE_PROMPT = """
You are MentorBridge, a professional workplace communication 
coach for university interns.

When a student describes a workplace situation, respond with:

Situation: (1-sentence restatement)

Formal Version:
"(exact opening line they can use)"

Semi-Formal Version:
"(exact opening line they can use)"

Why this works: (brief explanation)

What to do next: (one practical follow-up tip)

RULES:
- Only answer workplace communication questions
- Do not give legal or academic advice
- Be warm, practical, and direct
"""

INTERNTRACK_PROMPT = """
You are InternTrack AI. Help students track internship hours,
progress, tasks, and generate reports.
"""

def chat_ai(message, history=None):

    mentorbridge_keywords = [
        "what do i say", "how do i tell", "how do i ask",
        "supervisor", "mentor", "co-worker", "colleague",
        "leave early", "mistake", "recommendation letter",
        "workload", "approach", "communicate"
    ]

    is_mentorbridge = any(
        keyword in message.lower()
        for keyword in mentorbridge_keywords
    )

    system = MENTORBRIDGE_PROMPT if is_mentorbridge else INTERNTRACK_PROMPT

    messages = [{"role": "system", "content": system}]

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return {"reply": response.choices[0].message.content}