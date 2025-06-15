# agents/planner_agent.py

def plan_agents(user_goal: str):
    """
    Determines which agents should handle the user goal.

    Args:
        user_goal (str): The goal given by the user.

    Returns:
        list[str]: Ordered list of agent names to be executed.
    """
    user_goal_lower = user_goal.lower()
    agent_sequence = []

    if "spacex" in user_goal_lower:
        agent_sequence.append("spacex_agent")

    if "weather" in user_goal_lower:
        agent_sequence.append("weather_agent")

    if "news" in user_goal_lower or "headlines" in user_goal_lower:
        agent_sequence.append("news_agent")

    if "spacex" in user_goal_lower or "weather" in user_goal_lower or "news" in user_goal_lower:
        agent_sequence.append("summary_agent")

    return agent_sequence
