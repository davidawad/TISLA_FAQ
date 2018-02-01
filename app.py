import os
import sys
import json
from constants import *
from datetime import datetime

import requests
from flask import Flask, request

app = Flask(__name__)



def bot_response(message):
    # mapping of responses to content

    # if nothing matches, send back the intro message
    ret_obj = {}
    ret_text = 'DEFAULT MESSAGE'
    ret_replies = []

    # user sent reset command
    if message.lower() in ["restart", 'reset']:
        ret_text = intro_message
        ret_replies = [
          {
            "content_type": "text",
            "title": "Loan forgiveness?",
            "payload": "<POSTBACK_PAYLOAD>",
            "image_url": "https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/256/check.png"
          },
          {
            "content_type": "location"
          },
          {
            "content_type": "text",
            "title": "Something Else",
            "payload": "<POSTBACK_PAYLOAD>"
          }
        ]

    if message == "HELLO ROBOT":
        ret_text = "ROBOT SAYS HELLO FROM MAPPING FUNCTION"

    if message == "Loan forgiveness?":
        ret_text = "I can make your loans dissapear with bitcoin! :D"


    # set up return object
    ret_obj["text"] = ret_text

    if ret_replies:
        ret_obj["quick_replies"] = ret_replies


    return ret_obj



@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events
    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text


                    log("Received message: " + message_text +
                            " from sender id: " + recipient_id)

                    # generate response with the message text and send it back to the user
                    send_content(sender_id, bot_response(message_text))


                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


def send_content(recipient_id, content):

    # fails with unicode errors
    #  log("sending message to {recipient}: {content}".format(recipient=recipient_id, content=str(content)))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    # update data with json formatted passed content
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": content
    })

    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r)


def log(msg, *args, **kwargs):
    # simple wrapper for logging to stdout on heroku
    try:
        if type(msg) is dict:
            msg = json.dumps(msg)
        else:
            msg = unicode(msg).format(*args, **kwargs)
        print u"{}: {}".format(datetime.now(), msg)
    except UnicodeEncodeError:
        pass  # squash logging errors in case of non-ascii text
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
