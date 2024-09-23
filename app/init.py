from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from config.settings import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    slack_web_client = WebClient(token=app.config['SLACKBOT_TOKEN'])
    slack_events_adapter = SlackEventAdapter(
        app.config['SLACK_EVENTS_TOKEN'], "/slack/events", app
    )

    return app, slack_web_client, slack_events_adapter
