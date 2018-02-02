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

    'perkins_lf' : """Borrowers with an outstanding balance on a Perkins loan who meet the eligibility criteria can receive a cancellation regardless of when the loan was made for service provided on or after October 7, 1998 even if the borrower’s promissory note does not list the cancellation type. For newer cancellation types, however, the qualifying service or employment must include August 14, 2008 (the date the cancellation type first became available in the law) or begin on or after that date.""",




    'payment_plans' : """Choosing the right repayment plan can be confusing. It’s important to think not only about the short term, but the long term. While you are (rightly) concerned about your current financial situation, it’s also important to think about the long term. With that in mind, if you remember nothing else remember that the name of the game is to pay the least amount over time.

With that in mind, let’s go through a few questions to make sure we are heading in the right direction.""",


    'federal_loans' : """Federal student loans have many repayment options. Which ones you are eligible for with depend what type of loans you have and in some cases, when you took those loans out. If you aren’t sure, now is a good time to go to the National Student Loan Data System (NSLDS) to find out.""",


    'private_loans' : """Private student loan options vary by lender, but are generally few and far between. This is because the Federal Trade Commission (FTC) considers private student loans as the same as most other consumer debts and do not allow lenders to substantially alter the original terms of the loan.

Generally the only option available to lower your private student loan payment is to refinance the loan. Refinancing can lower your interest rate and/or extend the term of the loan which will result in a lower monthly payment. It can also be a way to remove your co-signer from the debt. Eligibility for consolidation will depend heavily on your credit score and debt to income ratio.

Our policy is to not recommend one lender over another, but coming soon is a list of every organization we could find that offers private loan consolidation, in alphabetical order""",


    'fnpl' : """There are several strategies to consider if you have both federal and private student loans. We at TISLA tend to be on the financially conservative side so take that into consideration as you go through these suggestions and the order of preference we’ve put them in. One thing to remember as you consider these options, is that no matter what, you are required to pay the minimum due on each loan. The other thing to remember is that no matter if you pay extra or not, payments are applied in the same way as far as what goes to interest and what goes to principal.

Read more about repaying mixed loans here: Take a look at the different types of loans on our website here: http://freestudentloanadvice.org/what-loans/""",


    'not_sure' : "Take a look at the different types of loans on our website here: http://freestudentloanadvice.org/what-loans/",


    'pdod' : "Having student loans that are delinquent or in default can be overwhelming. Many borrowers just assume there’s nothing that can be done and choose to ignore the problem either until they have the money to pay, or hope it will go away altogether. This is almost never the best strategy. To ensure we guide you in the right direction, let’s find out a little more about your situation.",



  },


  'replies': {

    'intro' : [
            {
              "content_type": "text",
              "title": "Loan forgiveness?",
              "payload": "<POSTBACK_PAYLOAD>",
              "image_url": "https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/256/check.png"
            },
            {
              "content_type": "text",
              "title": "Repayment Plans",
              "payload": "<POSTBACK_PAYLOAD>",
              "image_url": "https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/256/key.png"
            },
            {
              "content_type": "text",
              "title": "Past Due or Default",
              "payload": "<POSTBACK_PAYLOAD>",
              "image_url": "https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/256/cloud.png"
            }
          ],

    'loan_forgiveness' : [
         {
           "content_type": "text",
           "title": "Public Service Loan Forgiveness",
           "payload": "<POSTBACK_PAYLOAD>",
           # "image_url": ""
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

    'payment_plans' : [
        {
          "content_type": "text",
          "title": "I have federal loans",
          "payload": "<POSTBACK_PAYLOAD>",
          "image_url": "https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/256/check.png"
        },
        {
          "content_type": "text",
          "title": "I have private loans",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "I have both federal and private loans",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "I'm not sure.",
          "payload": "<POSTBACK_PAYLOAD>"
        }
      ],

    'federal_loans' : [
        {
          "content_type": "text",
          "title": "I have direct loans",
          "payload": "<POSTBACK_PAYLOAD>",
          "image_url": "https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/256/check.png"
        },
        {
          "content_type": "text",
          "title": "I have FFELP",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "I have Perkins Loans",
          "payload": "<POSTBACK_PAYLOAD>"
        },
      ],


    'pdod' : [
        {
          "content_type": "text",
          "title": "Federal loans past due but not in default",
          "payload": "<POSTBACK_PAYLOAD>",
          "image_url": "https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/256/check.png"
        },
        {
          "content_type": "text",
          "title": "Private loans past due",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "Federal loans in default",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "Am I eligible for bankruptcy?",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "I'm not sure",
          "payload": "<POSTBACK_PAYLOAD>"
        },
      ],







    },























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
