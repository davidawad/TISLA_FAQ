# -*- coding: utf-8 -*-

# import functions from app.py
from app import *
from constants import *


# FIXME this shouldn't exist, we should have separate functions to do these things
def return_response_object(text, quick_replies=None, buttons=None):
    ret_obj = {}
    ret_obj['text'] = text
    ret_obj['quick_replies'] = quick_replies
    ret_obj['buttons'] = buttons
    return ret_obj


class TestBotResponses(object):

    def test_intro_message_response(self):
        reply = bot_response("Hello")
        response_obj = return_response_object("Hello! I’m Sloan, your automated guide for advice on your student loans brought to you by TISLA. This is not legal advice but simple guidance to help you manage your student loan debt. Send 'restart' at any time to restart. Ready? Simply type your question and I’ll try and guide you to the best way to manage your student debt!", raw_response_data['replies']['intro'])

        assert reply.get('text', None) == response_obj.get('text')
        assert reply.get('buttons', None) == response_obj.get('buttons')
        assert reply.get('quick_replies', None) == response_obj.get('quick_replies')


    #  def test_pslf_message_response(self):
        #  reply = bot_response("What is pslf?")
        #  response_obj = return_response_object("Public Service Loan Forgiveness (PSLF) tends to be the most commonly known federal student loan forgiveness program. Some also call it the “Obama Forgiveness Program” although you should note that nobody with any real knowledge of the student loan programs will ever call it that. In fact, this misnomer is one of the clues we use to identify potential student loan scams. You should too.")

        #  assert reply.get('text', None) == response_obj.get('text')
        #  assert reply.get('buttons', None) == response_obj.get('buttons')
        #  assert reply.get('quick_replies', None) == response_obj.get('quick_replies')


