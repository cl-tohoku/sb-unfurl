from sb_unfurl.scrapbox import parse_url


def test_parse_url():
    url = "https://scrapbox.io/tohoku-nlp/2019-01-31_Minutes_of_Research_Seminar_%23324"
    team, title, line_id = parse_url(url)
    assert team == "tohoku-nlp"
    assert title == "2019-01-31_Minutes_of_Research_Seminar_%23324"
    assert line_id == ""

    url = "https://scrapbox.io/tohoku-nlp/2019-01-31_Minutes_of_Research_Seminar_%23324#5c5298c11309ba00005254b8"
    team, title, line_id = parse_url(url)
    assert team == "tohoku-nlp"
    assert title == "2019-01-31_Minutes_of_Research_Seminar_%23324"
    assert line_id == "5c5298c11309ba00005254b8"

    url = "https://scrapbox.io/tohoku-nlp/2019-02-22;_%E5%A4%A7%E7%AB%B9,_%E4%BA%95%E4%B9%8B%E4%B8%8A,_%E6%A8%AA%E4%BA%95"
    team, title, line_id = parse_url(url)
    assert team == "tohoku-nlp"
    assert (
        title
        == "2019-02-22;_%E5%A4%A7%E7%AB%B9,_%E4%BA%95%E4%B9%8B%E4%B8%8A,_%E6%A8%AA%E4%BA%95"
    )
    assert line_id == ""
