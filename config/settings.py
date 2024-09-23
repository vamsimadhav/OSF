import os

class Config:
    SLACKBOT_TOKEN = os.environ.get('SLACKBOT_TOKEN')
    SLACK_EVENTS_TOKEN = os.environ.get('SLACK_EVENTS_TOKEN')

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevConfig,
    prod=ProdConfig
)
