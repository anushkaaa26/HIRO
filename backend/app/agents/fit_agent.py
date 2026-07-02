
import os
import json
from groq import Groq
from dotenv import load_dotenv
from app.agents.base_agent import BaseAgent

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class FitAgent(BaseAgent):
    name = "fit"

    def execute(self, context):
        jd = context.get("jd", {})
        profile = context.get("profile", {})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are HIRO's Fit Scorer. Score student-job matches. Always return valid JSON only, no explanation, no markdown."
                },
                {
                    "role": "user",
                    "content": f"""Score how well this student matches this job. Return ONLY this JSON:
{{
  "score": <number 0-100>,
  "matched_skills": ["skill1", "skill2"],
  "missing_skills": ["skill1", "skill2"],
  "experience_match": "good or partial or poor",
  "confidence_message": "one encouraging sentence for the student",
  "recommendation": "apply or consider or skip"
}}

Student Profile:
{json.dumps(profile, indent=2)}

Job Details:
{json.dumps(jd, indent=2)}"""
                }
            ],
            temperature=0.1,
            max_tokens=1024,
        )

        raw = response.choices[0].message.content.strip()
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        return json.loads(raw.strip())
