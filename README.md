## Setup

### Install dependencies

```bash
pip install -r requirements.txt
```

### acquire environment variables

You need to set the following environment variables:

- `CONNECT_SID`: `connect.sid` cookie referenced when accessing the
  tohoku-nlp Scrapbox.
  See [ScrapboxのprivateプロジェクトのAPIを叩く](https://scrapbox.io/nishio/Scrapbox%E3%81%AEprivate%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AEAPI%E3%82%92%E5%8F%A9%E3%81%8F)
  for how to obtain the value. Note that abusing this value can retrieve your private
  Scrapbox contents.
- `SLACK_TOKEN`: User OAuth Token beginning with `xoxp-`. You can obtain
  it from the "OAuth & Permissions" section of the app's administration page.

Export these variables:

```bash
$ export CONNECT_SID=<sid>
$ export SLACK_TOKEN=<token>
```

### Setting of AWS

- Create a zip file for the python environment in AWS
```bash
pip install . -t layer/python
cd layer
zip -r mypackage.zip *
```
- Upload the zip file to create a layer of aws
- Activate the layer in the lambda function
- Set environment variables for lambda functions
