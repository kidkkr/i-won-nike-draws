from os import environ
import request
import crawler

result = lambda message, event: { "message": message, "event": event }

def crawl(event, context):
    data = crawler.run()

    if len(data) == 0:
        return result("skipped", event)

    try:
        request.post(environ['WEBHOOK_URL'], data=data)
    except:
        return result("failed", event)

    return result("succeed", event)

