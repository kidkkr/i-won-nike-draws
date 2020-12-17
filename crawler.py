import requests
from bs4 import BeautifulSoup


def extract_data(page_source):
    soup = BeautifulSoup(page_source, "html.parser")
    items = soup.select("li.upcomingItem")
    results = []

    for item in items:

        subject = item.select_one("p.txt-subject")
        if subject is None or "응모" not in subject.text:
            continue

        active_date = item["data-active-date"].split(" ")
        subject_text = subject.text.split(" ")
        date = active_date[0]
        time = subject_text[1]
        am_or_pm = "AM" if subject_text[0] == "오전" else "PM"
        datetime = "{} {} {}".format(date, time, am_or_pm)

        try:
            link = item.select_one("a")["href"]
            title = item.select_one("p.txt-description").text
            result = {
                "title": title,
                "date": datetime,
                "link": link
            }
            results.append(result)
        except:
            continue

    return results

def run():
    headers = {
        "user-agent": "Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405"
    }
    target_url = "https://www.nike.com/kr/launch/?type=upcoming"
    raw = requests.get(target_url, headers=headers)
    return extract_data(raw.content)

