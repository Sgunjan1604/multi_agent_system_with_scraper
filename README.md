# Multi-Agent AI System using Google ADK

## 📌 Description
A multi-agent system that handles a user goal by chaining agents to plan, enrich, and iterate with public APIs.

## 🧠 Agents
- `planner_agent`: Plans the agent sequence.
- `spacex_agent`: Fetches next SpaceX launch.
- `weather_agent`: Gets weather for the launch site.
- `summary_agent`: Summarizes likelihood of delay.

## ⚙️ Setup
1. Clone or unzip the repo.
2. Copy `.env.example` to `.env` and insert your API keys.
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the app:
```bash
python main.py
```

## ✅ Evaluation
- Tests two example goals with agent routing and iterative output.
