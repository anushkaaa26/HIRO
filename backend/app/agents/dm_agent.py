
import os
import json
from groq import Groq
from dotenv import load_dotenv
from app.agents.base_agent import BaseAgent

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class DMAgent(BaseAgent):
    name = "dm"

    def execute(self, context):
        profile = context.get("profile", {})
        jd = context.get("jd", {})
        contact = context.get("contact", {})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are HIRO's DM Writer. Write personalized recruiter outreach messages. Sound human, never generic. Always return valid JSON only, no markdown."
                },
                {
                    "role": "user",
                    "content": f"""Write a recruiter outreach message under 150 words. Return ONLY this JSON:
{{
  "subject": "email subject line",
  "body": "full message body",
  "tone": "professional or warm"
}}

Student: {json.dumps(profile, indent=2)}
Job: {json.dumps(jd, indent=2)}
Recruiter: {json.dumps(contact, indent=2)}"""
                }
            ],
            temperature=0.3,
            max_tokens=1024,
        )

        raw = response.choices[0].message.content.strip()
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        return json.loads(raw.strip())
