from sb_unfurl.scrapbox import parse_url


def test_parse_url():
    url = "https://scrapbox.io/tohoku-nlp/2019-01-31_Minutes_of_Research_Seminar_%23324"
    team, title = parse_url(url)
    assert team == "tohoku-nlp"
    assert title == "2019-01-31_Minutes_of_Research_Seminar_%23324"

    url = "https://scrapbox.io/tohoku-nlp/2019-01-31_Minutes_of_Research_Seminar_%23324#5c5298c11309ba00005254b8"
    team, title = parse_url(url)
    assert team == "tohoku-nlp"
    assert title == "2019-01-31_Minutes_of_Research_Seminar_%23324"
