from dataclasses import dataclass
from typing import Tuple, Optional
from urllib.parse import urlparse

import requests


def parse_url(url: str) -> Tuple[str, str]:
    o = urlparse(url)
    paths = o.path.split("/")
    return paths[1], paths[2]


def truncate_text(text: str) -> str:
    lines = text.split("\n")
    n_chars = 0
    truncated_lines = []
    for line in lines[1:]:  # the first line is a title
        if n_chars > 400:
            break
        n_chars += len(line)
        truncated_lines.append(line)
    return "\n".join(truncated_lines)


@dataclass
class ScrapboxPage:
    title: str
    url: str
    image_url: Optional[str]
    text: str

    @classmethod
    def request(cls, url: str, team: str, connect_sid: str) -> "ScrapboxPage":
        parsed_team, title = parse_url(url)
        if parsed_team != team:
            raise ValueError

        api_url = f"https://scrapbox.io/api/pages/{team}/{title}"
        cookies = {"connect.sid": connect_sid}

        r = requests.get(api_url, cookies=cookies)
        data = r.json()
        title = data["title"]
        image_url = data["image"]

        r = requests.get(f"{api_url}/text", cookies=cookies)
        text = r.content.decode("utf-8")

        return cls(title, url, image_url, text)

    def to_attachment(self):
        return {
            "title": self.title,
            "title_link": self.url,
            "image_url": self.image_url,
            "color": "#39ac86",
            "text": truncate_text(self.text),
        }
