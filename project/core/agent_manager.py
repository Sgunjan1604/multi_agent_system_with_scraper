# core/agent_manager.py

from agents.spacex_agent import get_next_launch
from agents.weather_agent import get_weather
from agents.summary_agent import summarize
# If the function is named get_news
from agents.news_agent import run as run_news_agent



def run_agents(sequence, user_goal):
    context = {}

    for agent in sequence:
        if agent == "spacex_agent":
            context['launch'] = get_next_launch()

        elif agent == "weather_agent":
            context['weather'] = get_weather(context['launch'])

        elif agent == "news_agent":
            context['news'] = run_news_agent(context, user_goal)
            

        elif agent == "summary_agent":
            context['summary'] = summarize(
                context.get('launch'),
                context.get('weather'),
                context.get('news')
            )

    return context.get('summary', 'No result.')
