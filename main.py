import json
import os

import requests

from sb_unfurl.scrapbox import ScrapboxPage


def main(event, context):
    if "body" in event.keys():
        body = json.loads(event["body"])
        if "challenge" in body.keys():
            return body["challenge"]
        else:
            unfurls = dict()

            for link in body["event"]["links"]:
                sp = ScrapboxPage.request(link["url"], os.environ["CONNECT_SID"])
                unfurls[sp.url] = sp.to_attachment()

            headers = {"Authorization": f"Bearer {os.environ['SLACK_TOKEN']}"}
            payload = {
                "token": os.environ["SLACK_TOKEN"],
                "channel": body["event"]["channel"],
                "ts": body["event"]["message_ts"],
                "unfurls": unfurls,
            }
            r = requests.post("https://slack.com/api/chat.unfurl", json=payload, headers=headers)
    return ""
