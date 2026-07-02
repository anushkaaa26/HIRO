
import os
import json
from groq import Groq
from dotenv import load_dotenv
from app.schemas.jd_schema import JDParseResponse

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def parse_job_description(job_description: str) -> JDParseResponse:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are HIRO's JD Parser. Extract structured data from job descriptions. Always return valid JSON only, no explanation, no markdown."
            },
            {
                "role": "user",
                "content": f"""Extract structured data from this job description and return ONLY this JSON:
{{
  "company": "company name",
  "role": "job title",
  "skills": ["skill1", "skill2"],
  "experience": "experience required",
  "location": "location or Remote",
  "employment_type": "Full-time or Internship etc",
  "deadline": null
}}

Job Description:
{job_description}"""
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
    raw = raw.strip()
    data = json.loads(raw)
    return JDParseResponse(**data)
