import urllib.request, json

LOCAL_JSON_FILE = "cardlist.json"

JSON_URL = "https://eternalwarcry.com/content/cards/eternal-cards.json"
USER_AGENT = "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"

req = urllib.request.Request(JSON_URL)
req.add_header("User-Agent", USER_AGENT)
response = urllib.request.urlopen(req)

card_json = json.loads(response.read())

with open(LOCAL_JSON_FILE, 'w') as f:
    json.dump(card_json, f)
