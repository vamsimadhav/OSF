# run.py
from app.init import create_app
from app.slack_events import register_event_handlers

app, slack_web_client, slack_events_adapter = create_app("dev")

register_event_handlers(slack_events_adapter, slack_web_client)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
