from app.agents.registry import AGENTS


class Planner:

    def run_agent(self, agent_name, context):

        agent = AGENTS.get(agent_name)

        if not agent:
            raise ValueError(f"Unknown agent: {agent_name}")

        return agent.execute(context)


planner = Planner()