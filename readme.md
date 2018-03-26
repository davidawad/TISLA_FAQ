# TISLA-FAQ

[![Build Status](https://travis-ci.org/davidawad/TISLA_FAQ.svg?branch=master)](https://travis-ci.org/davidawad/TISLA_FAQ) [![Coverage Status](https://coveralls.io/repos/github/davidawad/TISLA_FAQ/badge.svg?branch=master)](https://coveralls.io/github/davidawad/TISLA_FAQ?branch=master)  [![Maintainability](https://api.codeclimate.com/v1/badges/74a0339033d7f15a68e7/maintainability)](https://codeclimate.com/github/davidawad/TISLA_FAQ/maintainability)


This bot was built to handle FAQ's for TISLA (The Institute for Student Loan Advice).

TISLA is a 501(c)(3) nonprofit that aims to educate the public about how to deal with student loans and manage your debt. [You can find out more about them here](https://freestudentloanadvice.org)

Apparently 40% of people look for advice about student loans on social media; HENCE THIS BOT WAS BORN!
The goal of the bot is to simply engage with users on social media who might have questions about managing student debt.


## How it works
This is a simple python bot that uses Flask to build a webhook for Facebook's Messenger Bot API.
It uses cosine simularity to map a dictionary of input messages to output messages that come with quick replies.


The bot essentially implements a "decision tree" for a conversation about student loans, and links back to TISLA with more free information.

It's built based on this [tutorial](https://blog.hartleybrody.com/fb-messenger-bot/).


#### "Callback verification failed"

![Facebook Error](https://cloud.githubusercontent.com/assets/18402893/21538944/f96fcd1e-cdc7-11e6-83ee-a866190d9080.png)

The #1 error that gets reported in issues is that facebook returns an error message (like above) when trying to add the heroku endpoint to your facebook chat application.

If you're getting this error, it likely means that you didn't set your heroku config values properly. Run `heroku config` from the command line within your application and verify that there's a key called `VERIFY_TOKEN` that has been set, and that it's set to the same value as what you've typed into the window on facebook.



Thank you for reading and feel free to reach out if there's anything I can do.
