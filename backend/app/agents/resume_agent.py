
import os
import json
from groq import Groq
from dotenv import load_dotenv
from app.agents.base_agent import BaseAgent

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ResumeAgent(BaseAgent):
    name = "resume"

    def execute(self, context):
        jd = context.get("jd", {})
        resume_text = context.get("resume_text", "")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are HIRO's Resume Tailor. Rewrite resumes to match job descriptions. Never fabricate experience. Always return valid JSON only, no markdown."
                },
                {
                    "role": "user",
                    "content": f"""Tailor this resume for the job. Return ONLY this JSON:
{{
  "tailored_resume": "full rewritten resume text",
  "ats_score": <number 0-100>,
  "keywords_added": ["kw1", "kw2"],
  "changes_summary": "brief description of changes made"
}}

Job:
{json.dumps(jd, indent=2)}

Current Resume:
{resume_text}"""
                }
            ],
            temperature=0.1,
            max_tokens=2048,
        )

        raw = response.choices[0].message.content.strip()
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        return json.loads(raw.strip())
