from app.commands import handle_san_3p, handle_pick_team, handle_postman_setup

def register_event_handlers(slack_events_adapter, slack_web_client):
    @slack_events_adapter.on("message")
    def handle_message(payload):
        event = payload.get("event", {})
        text = event.get("text", "").lower()
        channel_id = event.get("channel")

        # Route to appropriate command handler
        if "san 3p" in text:
            handle_san_3p(slack_web_client, channel_id)
        elif "pick team" in text:
            handle_pick_team(slack_web_client, channel_id)
        elif "postman setup" in text:
            handle_postman_setup(slack_web_client, channel_id)
