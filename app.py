import urllib
import json
import os
import csv
import logging
import codecs
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from discordWebhooks import Webhook, Attachment, Field

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    url = "https://discordapp.com/api/webhooks/272907589010980865/c8rT5C_NY55zh6zL9ja0VPCIMGOFhl5AKvrD8H611en17vjvY5TI2sgDEQeuSVn_o3Yo"
    wh = Webhook(url, "Coucou tout le monde", "Pseudo")

    at = Attachment(author_name = "Derpolino", color = "#ff0000", title = "Discord webhooks")

    field = Field("Version", "1.0", True)
    at.addField(field)
    field = Field("Last update", "27/10/2016", True)
    at.addField(field)
    field = Field("Changelog", "Initiale release !", False)
    at.addField(field)

    wh.addAttachment(at)

    at = Attachment(author_name = "Github", color = "#0000ff", title = "Hello world")
    wh.addAttachment(at)

    wh.post()


    """
    if req.get("result").get("action") != "lookup":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    search_name = parameters.get("given-name")

    chessdb = {}
    with codecs.open('connor_history.csv','r',encoding='utf8') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            chessdb[row[2]] = row[0]
    logging.info("ChessDB is {}".format(chessdb))

    #search_name = "Michael"
    event_matches = [(name, event) for name, event in chessdb.items() if search_name.upper() in name.upper()]
    logging.info("Matched events are {}".format(event_matches))

    speech = ""
    if not event_matches:
        speech = "Didn't find that person!"
    for (name,event) in event_matches:
        speech += "At {}, you played {}. ".format(event,name)

    print("Response:")
    print(speech)
    """
    speech = "Requesting troops for ya..."

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port {}".format(port))

    app.run(debug=True, port=port, host='0.0.0.0')
