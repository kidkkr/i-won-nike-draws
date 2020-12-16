from os import environ
import requests
import crawler
import json

def crawl():
    draws = crawler.run()
    requests.post("https://hooks.zapier.com/hooks/catch/9108785/oc6oz88", data=json.dumps(draws))

crawl()

