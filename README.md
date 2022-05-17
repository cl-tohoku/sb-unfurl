## Setup

### Install dependencies

```bash
pip install -r requirements.txt
```

### Export environment variables

You need to set the following environment variables:

- `SANIC_CONNECT_SID`: `connect.sid` cookie referenced when accessing the
  tohoku-nlp Scrapbox.
  See [ScrapboxのprivateプロジェクトのAPIを叩く](https://scrapbox.io/nishio/Scrapbox%E3%81%AEprivate%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AEAPI%E3%82%92%E5%8F%A9%E3%81%8F)
  for how to obtain the value. Note that abusing this value can retrieve your private
  Scrapbox contents.
- `SANIC_SLACK_TOKEN`: User OAuth Token beginning with `xoxp-`. You can obtain
  it from the "OAuth & Permissions" section of the app's administration page.

Export these variables:

```bash
$ export SANIC_CONNECT_SID=<sid>
$ export SANIC_SLACK_TOKEN=<token>
```

## Start the server

```bash
$ sanic main.app
```
