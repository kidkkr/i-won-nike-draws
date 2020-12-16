import requests
from bs4 import BeautifulSoup


def extract_data(page_source):
    soup = BeautifulSoup(page_source, "html.parser")
    items = soup.select("li.upcomingItem")
    results = []

    for item in items:
        try:
            link = item.select_one("a")
            title = item.select_one("p.txt-description")
            result = {
                "link": link["href"],
                "date": item["data-active-date"],
                "title": title.text
            }
            results.append(result)
        except:
            break

    return results

def run():
    headers = {
        "user-agent": "Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405"
    }
    target_url = "https://www.nike.com/kr/launch/?type=upcoming"
    raw = requests.get(target_url, headers=headers)
    return extract_data(raw.content)

