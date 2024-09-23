# Section Message Block (Reusable)
def messageBlock(text):
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": text
        }
    }

# Preformatted Code Block (Reusable)
def codeBlock(preformatted_text):
    return {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_preformatted",
                "elements": [{"type": "text", "text": preformatted_text}]
            }
        ]
    }

# Divider Block (Reusable)
def dividerBlock():
    return {"type": "divider"}

# Image Block (Reusable)
def imageBlock(image_url, alt_text, title=""):
    return {
        "type": "image",
        "image_url": image_url,
        "alt_text": alt_text,
        "title": {
            "type": "plain_text",
            "text": title
        }
    }

# Context Block (Small Inline Text or Images)
def contextBlock(elements):
    # 'elements' is a list of dictionaries representing text/images
    return {
        "type": "context",
        "elements": elements
    }

# Button Block
def buttonBlock(text, action_id, value):
    return {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": text
                },
                "action_id": action_id,
                "value": value
            }
        ]
    }
