# -*- coding: utf-8 -*-:w

# import functions from app.py
from app import *
from constants import *

def _bot_response(message, response_obj):
    reply = bot_response(message)
    assert reply.get('text', None) == response_obj.get('text')
    assert reply.get('buttons', None) == response_obj.get('buttons')
    assert reply.get('quick_replies', None) == response_obj.get('quick_replies')


def return_response_object(text, quick_replies=None, buttons=None):
    ret_obj = {}
    ret_obj['text'] = text
    ret_obj['quick_replies'] = quick_replies
    ret_obj['buttons'] = buttons
    return ret_obj


_bot_response("Hello", return_response_object("Hello! I’m Sloan, your automated guide for advice on your student loans brought to you by TISLA. This is not legal advice but simple guidance to help you manage your student loan debt. Send 'restart' at any time to restart. Ready? Simply type your question and I’ll try and guide you to the best way to manage your student debt!", raw_response_data['replies']['intro']))




#  test_bot_response("What is pslf?" , return_response_object("Public Service Loan Forgiveness (PSLF) tends to be the most commonly known federal student loan forgiveness program. Some also call it the “Obama Forgiveness Program” although you should note that nobody with any real knowledge of the student loan programs will ever call it that. In fact, this misnomer is one of the clues we use to identify potential student loan scams. You should too."))


#  test_bot_response("I have private loans", return_response_object("""Private student loan options vary by lender, but are generally few and far between. This is because the Federal Trade Commission (FTC) considers private student loans as the same as most other consumer debts and do not allow lenders to substantially alter the original terms of the loan.

#  Generally the only option available to lower your private student loan payment is to refinance the loan. Refinancing can lower your interest rate and/or extend the term of the loan which will result in a lower monthly payment. It can also be a way to remove your co-signer from the debt. Eligibility for consolidation will depend heavily on your credit score and debt to income ratio.

#  Our policy is to not recommend one lender over another, but coming soon is a list of every organization we could find that offers private loan consolidation, in alphabetical order"""))


#  test_response_bot("Repayment Plans", return_response_object("""Choosing the right repayment plan can be confusing. It’s important to think not only about the short term, but the long term. While you are (rightly) concerned about your current financial situation, it’s also important to think about the long term. With that in mind, if you remember nothing else remember that the name of the game is to pay the least amount over time.

#  With that in mind, let’s go through a few questions to make sure we are heading in the right direction."""))



#  test_response_bot("Repayment Plans", return_response_object("""Hello!  I’m Sloan, your automated guide for advice on your student loans brought to you by TISLA.  This is not legal advice but simple guidance to help you manage your student loan debt.  Send 'restart' at any time to restart.  Ready?  Simply type your question and I’ll try and guide you to the best way to manage your student debt!"""))
