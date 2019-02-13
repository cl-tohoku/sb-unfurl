from dataclasses import dataclass
from itertools import dropwhile
from typing import Tuple, Optional, Iterable
from urllib.parse import urlparse

import requests


def parse_url(url: str) -> Tuple[str, str, str]:
    o = urlparse(url)
    paths = o.path.split("/")
    return paths[1], paths[2], o.fragment


def truncate_lines(lines: Iterable[str]) -> str:
    n_chars = 0
    truncated_lines = []
    for line in lines:
        if n_chars > 400:
            break
        n_chars += len(line)
        truncated_lines.append(line)
    return "\n".join(truncated_lines)


def truncate_text(text: str) -> str:
    # the first line is a title
    return truncate_lines(text.splitlines()[1:])


@dataclass
class ScrapboxPage:
    title: str
    url: str
    image_url: Optional[str]
    text: str

    @classmethod
    def request(cls, url: str, team: str, connect_sid: str) -> "ScrapboxPage":
        parsed_team, title, line_id = parse_url(url)
        if parsed_team != team:
            raise ValueError

        api_url = f"https://scrapbox.io/api/pages/{team}/{title}"
        cookies = {"connect.sid": connect_sid}

        r = requests.get(api_url, cookies=cookies)
        data = r.json()
        title = data["title"]
        image_url = data["image"]

        r = requests.get(f"{api_url}/text", cookies=cookies)

        if line_id:
            text = truncate_lines(
                line["text"]
                for line in dropwhile(lambda line: line["id"] != line_id, data["lines"])
            )
        else:
            text = truncate_text(r.content.decode("utf-8"))

        return cls(title, url, image_url, text)

    def to_attachment(self):
        return {
            "title": self.title,
            "title_link": self.url,
            "image_url": self.image_url,
            "color": "#39ac86",
            "text": truncate_text(self.text),
        }
