def summarize(launch_data, weather_data, news_data=None):
    summary = "\n🧠 Summary Report:\n"

    # Launch info
    mission = launch_data.get("name", "Unknown Mission")
    date = launch_data.get("date_utc", "Unknown Date")
    summary += f"\n🚀 Launch Info:\n- Mission: {mission}\n- Date (UTC): {date}\n"

    # Weather info
    summary += f"\n🌤️ Weather at Launch Site:\n- {weather_data}\n"

    # News info
    summary += f"\n📰 News Info: "
    if news_data:
        summary += "\nNews Headlines:\n" + "\n".join(f"- {h}" for h in news_data)
    else:
        summary += "Not available\nNews Headlines: No result."

    return summary
