import random
from app.blocks import messageBlock, codeBlock

def handle_pick_team(slack_web_client, channel_id):
    num = random.randint(0, 6)
    results = ["Vamsi Madhav H", 
               "Pawan Pal", 
               "Guruprasad J", 
               "Arsalan", 
               "Yashwanthi", 
               "Kritik Soni"
               ]
    val = messageBlock(f"You have been picked {results[num]}")

    slack_web_client.chat_postMessage(
        channel=channel_id,
        blocks=[val]
    )

def handle_san_3p(slack_web_client, channel_id):
    results = '''Facebook                  ⮕ fbmmp
Google                    ⮕ gaap
Google Marketing Platform ⮕ google_ddm
TikTok                    ⮕ TIKTOK
Snap                      ⮕ snapmmp
Twitter                   ⮕ TWITTER
Apple                     ⮕ apple_search_ad
Roku                      ⮕ roku
Persona                   ⮕ persona
'''
    val = codeBlock(results)

    slack_web_client.chat_postMessage(
        channel=channel_id,
        blocks=[val]
    )

def handle_postman_setup(slack_web_client, channel_id):
    json_file_path = '/Users/vamsi.madhavh/Desktop/OSF/data/Branch-APIs.postman_collection.json'

    slack_web_client.files_upload(
                channels=channel_id,
                file=json_file_path,
                title="Postman Setup File for Branch",
                filetype="json",
                initial_comment="Here is the Branch Postman setup file you requested!"
            )