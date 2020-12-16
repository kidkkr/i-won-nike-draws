from os import environ
import requests
import crawler
import json

result = lambda message, event: { "message": message, "event": event }

def crawl(event, context):
    data = crawler.run()

    if len(data) == 0:
        return result("skipped", event)

    try:
        requests.post(environ['WEBHOOK_URL'], data=json.dumps(data))
    except:
        return result("failed", event)

    return result("succeed", event)

