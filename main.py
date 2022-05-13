import requests
from sanic import Sanic
from sanic import response
from sanic.log import logger
from sanic.request import Request

from sb_unfurl.scrapbox import ScrapboxPage

app = Sanic("sb-unfurl")


@app.post("/")
async def root(request: Request):
    j = request.json
    logger.debug(j)

    if j["type"] == "url_verification":
        return response.text(j["challenge"])

    else:
        unfurls = dict()
        for link in j["event"]["links"]:
            sp = ScrapboxPage.request(link["url"], app.config.CONNECT_SID)
            unfurls[sp.url] = sp.to_attachment()

        headers = {"Authorization": f"Bearer {app.config.SLACK_TOKEN}"}
        payload = {
            "token": app.config.SLACK_TOKEN,
            "channel": j["event"]["channel"],
            "ts": j["event"]["message_ts"],
            "unfurls": unfurls,
        }
        logger.debug(payload)
        r = requests.post(
            "https://slack.com/api/chat.unfurl", json=payload, headers=headers
        )
        logger.debug(r.json())

    return response.text("")


@app.get("/")
async def test(request):
    return response.json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
