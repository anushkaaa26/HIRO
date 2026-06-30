from app.agents.base_agent import BaseAgent


class FitAgent(BaseAgent):
    name = "fit"

    def execute(self, context):
        return {
            "score": 74,
            "matched_skills": ["Python", "FastAPI"],
            "missing_skills": ["AWS", "Docker"],
            "confidence": "You're stronger than you think."
        }