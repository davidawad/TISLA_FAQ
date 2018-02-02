# -*- coding: utf-8 -*-

# this file contains constant data that the bot gives back to users


raw_response_data = {

  'responses' : {

    'intro' : "Hello! Thanks for reaching out to TISLA. You can walk through this guide to get advice on your student loans. Send 'restart' at any time to restart. Or just visit us at freestudentloanadvice.org",


    'loan_forgiveness' : "First the bad news, most borrowers should expect to repay their student loans as agreed. With that said, there are many student loan repayment, discharge and forgiveness programs out there. Over time, we plan on having a comprehensive list, but for now, we'll just talk about the most common programs.",


    'pslf' : """ Public Service Loan Forgiveness (PSLF) tends to be the most commonly known federal student loan forgiveness program. Some also call it the “Obama Forgiveness Program” although you should note that nobody with any real knowledge of the student loan programs will ever call it that. In fact, this misnomer is one of the clues we use to identify potential student loan scams. You should too.

                       To be eligible to get the balance of your loan forgiven under PSLF, the borrower will need to make 120 payments, on eligible loans, while working full time for an eligible employer. It’s important to note that all three of these things have to happen at the same time. Once you complete the 120 payments, the balance of your loans are forgiven, tax free.""",


    'teacher_lf' : """Teacher Loan Forgiveness (TLF) pays up to $17,500 in eligible federal student loans for qualified teachers who teach in a Title I school for five consecutive years.

    To be eligible for TLF you must have had no federal loans made prior to October 1, 1998. This includes any loans made after that date, even if you have paid off the loans made prior to October 1, 1998. If you did have loans made prior to that date, the only way to be eligible is if you pay those loan in full BEFORE taking out new loans after that date. Consolidating loans made prior to October 1, 1998 does not make them eligible, even if done after that date.""",


    'dod_lf' : """There are many state and federal programs that can help you repay your student debt. The most common are the Department of Defense loan repayment program, AmeriCorps and the Peace Corps. The federal government also offers some loan repayment to its employees. We will outline the details of these in the near future here.""",

    'perkins_lf' : """Borrowers with an outstanding balance on a Perkins loan who meet the eligibility criteria can receive a cancellation regardless of when the loan was made for service provided on or after October 7, 1998 even if the borrower’s promissory note does not list the cancellation type. For newer cancellation types, however, the qualifying service or employment must include August 14, 2008 (the date the cancellation type first became available in the law) or begin on or after that date."""

  },


  'replies': {

    'intro' : [
            {
              "content_type": "text",
              "title": "Loan forgiveness?",
              "payload": "<POSTBACK_PAYLOAD>",
              "image_url": "https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/256/check.png"
            },
            {
              "content_type": "text",
              "title": "Something Else",
              "payload": "<POSTBACK_PAYLOAD>"
            }
          ],

    'loan_forgiveness' : [
         {
           "content_type": "text",
           "title": "Public Service Loan Forgiveness",
           "payload": "<POSTBACK_PAYLOAD>",
           "image_url": "https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/256/check.png"
         },
         {
           "content_type": "text",
           "title": "Teacher Loan Forgiveness",
           "payload": "<POSTBACK_PAYLOAD>"
         },
         {
         "content_type": "text",
         "title": "DoD Loan Repayment",
         "payload": "<POSTBACK_PAYLOAD>"
       },
       {
         "content_type": "text",
         "title": "Americorps and Peace Core Repayment",
         "payload": "<POSTBACK_PAYLOAD>"
       },
       {
         "content_type": "text",
         "title": "Perkins Loan Forgiveness",
         "payload": "<POSTBACK_PAYLOAD>"
       }
     ],


    'pslf' : [
        {
          "content_type": "text",
          "title": "Public Service Loan Forgiveness",
          "payload": "<POSTBACK_PAYLOAD>",
          "image_url": "https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/256/check.png"
        },
        {
          "content_type": "text",
          "title": "Teacher Loan Forgiveness",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "DoD Loan Repayment",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "Americorps and Peace Core Repayment",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "Perkins Loan Forgiveness",
          "payload": "<POSTBACK_PAYLOAD>"
        }
      ],


    'SOMETHING ELSE' : [
        {
          "content_type": "text",
          "title": "Public Service Loan Forgiveness",
          "payload": "<POSTBACK_PAYLOAD>",
          "image_url": "https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/256/check.png"
        },
        {
          "content_type": "text",
          "title": "Teacher Loan Forgiveness",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "DoD Loan Repayment",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
            "content_type": "text",
          "title": "Americorps and Peace Core Repayment",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "Perkins Loan Forgiveness",
          "payload": "<POSTBACK_PAYLOAD>"
        }
      ]
    } ,

 'buttons' : {

   "perkins_lf" : [
    {
     "type":  "web_url",
     "url":   "http://freestudentloanadvice.org/loan-forgiveness/perkins-loan-forgiveness-program/",
     "title": "Select Criteria",
     "webview_height_ratio": "full",
     "messenger_extensions": True,
     "fallback_url": "http://freestudentloanadvice.org/loan-forgiveness/perkins-loan-forgiveness-program/"
   }

    ]

 }

}
