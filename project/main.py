
from agents.planner_agent import plan_agents
from core.agent_manager import run_agents

if __name__ == "__main__":
    user_goal = "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."
    agent_sequence = plan_agents(user_goal)
    final_result = run_agents(agent_sequence, user_goal)
    print("\n🚀 Final Result:")
    print(final_result)

    user_goal = "Show me the top 5 Hacker News headlines."
    agent_sequence = plan_agents(user_goal)
    final_result = run_agents(agent_sequence, user_goal)
    print("\n📰 News Headlines:")
    print(final_result)
