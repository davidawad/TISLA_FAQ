# -*- coding: utf-8 -*-:w
import os
import sys
import json
import requests

from datetime import datetime
from fuzzywuzzy import process
from flask import Flask, request

# import constants
from constants import *

app = Flask(__name__)


# TODO use a dictionary to map the responses or something better?
def find_response(key):
    # find replies for a given string
    return (raw_response_data['responses'].get(key),
            raw_response_data['replies'].get(key),
            raw_response_data['buttons'].get(key))


def bot_response(message):
    # determine the response and properly format it
    # TODO should be separated

    ret_obj = {}
    ret_text = 'DEFAULT MESSAGE'
    ret_replies = []
    ret_buttons = []

    # filter what to send back based on what's given
    # lowercase message to make searching easier
    message = message.lower()

    # run a fuzzy match to find the closest response mapping to a key in the data
    mapped_input = process.extractOne(message.lower(), input_message_key_mappings.keys())[0]

    # use the mapping dict to map the input to the proper response
    bot_response_key = input_message_key_mappings[mapped_input]

    # retrieve the response object components
    ret_text, ret_replies, ret_buttons = find_response(bot_response_key)


    # stitch together the return object
    # TODO cleaner way to do this setting?
    ret_obj["text"] = ret_text

    if ret_replies:
        ret_obj["quick_replies"] = ret_replies

    if ret_buttons:
        ret_obj["buttons"] = ret_buttons

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

                # someone sent us a message
                if messaging_event.get("message"):

                    # the facebook ID of the person sending you the message
                    sender_id = messaging_event["sender"]["id"]
                    # the recipient's ID, which should be your page's facebook ID
                    recipient_id = messaging_event["recipient"]["id"]
                    # the message's text
                    message_text = messaging_event["message"]["text"]


                    log("Received message: " + message_text +
                            " from sender id: " + recipient_id)

                    # generate response with the message text and send it back to the user
                    send_content(sender_id, bot_response(message_text))


                # delivery confirmation
                if messaging_event.get("delivery"):
                    pass

                # optin confirmation
                if messaging_event.get("optin"):
                    pass

                # user clicked/tapped "postback" button in earlier message
                if messaging_event.get("postback"):
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
