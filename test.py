#!/usr/bin/env python

import urllib
import json
import os
import csv
import io

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


"""
matches = [events[idx] for idx, name in enumerate(names) if search_name.upper() in name.upper()]
print(matches)
"""

chessdb = {}
with io.open('connor_history.csv','r',encoding='utf8') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        chessdb[row[2]] = row[0]
        #events.append(row[0])
        #names.append(row[2])

print(chessdb)
search_name = "nathan"
event_matches = [(name, event) for name, event in chessdb.items() if search_name.upper() in name.upper()]
print(event_matches)

#speech = "Event: Name\n"
speech = ""
for (name,event) in event_matches:
    speech += "At {}, you played {}.\n".format(event,name)
print(speech)

"""
i = 0
speech = ""
for name in names:
    if search_name.upper() in name.upper():
        print("match found {}".format(name))
        speech = events[i]
        i += 1

"""

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
    if req.get("result").get("action") != "lookup":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    search_name = parameters.get("given-name")

    i = 0
    speech = ""
    for name in names:
        if search_name.upper() in name.upper():
            speech = events[i]
            i += 1
    #cost = {'Chris':100, 'John':200, 'Sarah':300, 'Karen':400, 'Phil':500}
    #speech = "You played " + zone + " " + str(cost[zone]) + " days ago."

    print("Response:")
    #print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }

"""
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d".format(port))

    app.run(debug=True, port=port, host='0.0.0.0')
"""