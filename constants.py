# -*- coding: utf-8 -*-

# this file contains constant data that the bot gives back to users


# hash to map input messgages to the keys in the response object
input_message_key_mappings = {
        # intro mappings
         'restart': 'intro',
         'hey': 'intro',
         'hello': 'intro',
         'hi': 'intro',
         'hi there': 'intro',

         # loan forgiveness
         "Loan forgiveness" : "loan_forgiveness",

         "Public Service Loan forgiveness" : "pslf",
         'Teacher Loan Forgiveness': 'teacher_lf',
         'Department of Defense Loan Forgiveness': 'dod_lf',
         'Americorps and Peace Corps Loan Repayment': 'dod_lf',
         'Perkins Loan Forgiveness': 'perkins_lf',


         # repayment plans
         'Repayment Plans': 'payment_plans',

         'I have federal loans': 'federal_loans',
         'I have private loans': 'private_loans',
         'I have both federal and private loans': 'fnpl',
         "I'm not sure": 'not_sure',


         # past due or default
         "Past due or Default": 'pdod',

         "Federal loans past due": 'flpd',
         "Private loans past due": 'plpd',
         "I have federal loans in default": 'flid',
         'Am I eligible for bankruptcy?': 'bankruptcy',

         # consolidate my loans?
         "Should I consolidate my loans?": 'consolidate_1',

         # fraud
         'fraud' : 'fraud',
         'borrower defense' : 'fraud',
         'scams' : 'fraud',


         'unpaid refund' : 'unpaid',

         # identity theft
         "id theft": 'id',
         "identity": 'id',
         "identity theft": 'id',
         'false certification': 'id',

         # school closed
         'school closed' : 'school_closed',

         # D & D
         'death' : 'death',
         'disability' : 'disability',

         "Thanks" : 'thank_you'
        }




raw_response_data = {

  'responses' : {

      'intro' : "Hello! I’m Sloan, your automated guide for advice on your student loans brought to you by TISLA. This is not legal advice but simple guidance to help you manage your student loan debt. Send 'restart' at any time to restart. Ready? Simply type your question and I’ll try and guide you to the best way to manage your student debt!",


    'loan_forgiveness' : "First the bad news, most borrowers should expect to repay their student loans as agreed. With that said, there are many student loan repayment, discharge and forgiveness programs out there. Over time, we plan on having a comprehensive list, but for now, we'll just talk about the most common programs.",


    'pslf' : """ Public Service Loan Forgiveness (PSLF) tends to be the most commonly known federal student loan forgiveness program. Some also call it the “Obama Forgiveness Program” although you should note that nobody with any real knowledge of the student loan programs will ever call it that. In fact, this misnomer is one of the clues we use to identify potential student loan scams. You should too.

    To be eligible to get the balance of your loan forgiven under PSLF, the borrower will need to make 120 payments, on eligible loans, while working full time for an eligible employer. It’s important to note that all three of these things have to happen at the same time. Once you complete the 120 payments, the balance of your loans are forgiven, tax free. You can find more information on PSLF on our website here:  http://freestudentloanadvice.org/loan-forgiveness/""",


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


  'flpd' : 'If your federal loans are past due, it’s important to find out how far past due they are by calling or logging on to your loan servicer’s website. Take a look at our site for some milestones to look out for: http://freestudentloanadvice.org/past-due/federal-loan-delinquency/',


  'plpd' : """Unfortunately, most private loan programs do not have lower payment or deferment options for when you are struggling. In their defense, they are for the most part not allowed to offer anything that would “substantially alter the terms of the loan.” This is because private student loans fall under the category of “retail credit” for which the federal Office of the Comptroller of the Currency and the Federal Trade Commission have oversight. So in most cases, it’s not that the lender doesn’t want to help you, it’s that they can’t. You can read more about these situations in this article. Usually the only thing they can offer you is to postpone payments with forbearance for a few months. This can often cost a fee of as much as $150.

Ironically, much like mortgages, once the loan is in default or charge off status (which for most private loans is at 120 days past due) the lenders have more flexibility to assist you. They are no longer restricted in offering options that may alter the terms of the loan you agreed to. Some lenders will offer a temporary lowering of the interest rate to allow you a lower payment. Others will offer interest only payments for a year. All private loans are different so your best recourse is to contact the lender to see what is available.

If you find yourself unable to pay, one strategy is to pay as much as you can, every single month while keeping the lender appraised of your situation. This shows good faith and can often prevent the lender from resorting to litigation to collect the loan. Even if you have no funds now, litigation can add significant fees to the loan and can haunt you down the road so it’s best to avoid it if possible.""",


    'flid' : "Federal law defines default as 270 days past due. Defaulted loans are not eligible for deferments, lower payment options or other benefits. Defaulted loans are also eligible for wage and tax refund garnishment, significant collection costs, and have significant implications to the borrower’s credit report. While the first set of rules take effect as soon as the loan becomes 270 days past due, the rest don’t come into effect until the loan transfers to a guaranty agency (for FFEL loans) or a collections agency (for Direct Loans). There's a lot more information, feel free to take a look at our page on the subject: http://freestudentloanadvice.org/past-due/federal-loan-default/",



    'bankruptcy' : 'We would be remiss if we didn’t bring up bankruptcy as part of this discussion. While student loans are technically not dischargeable in bankruptcy, there are exceptions. We will expand this section in the future to go into more detail, but in the meantime, you can read about student loans and bankruptcy here: https://www.usnews.com/education/blogs/student-loan-ranger/2014/08/13/debunking-the-student-loan-bankruptcy-myth',


   'consolidate_1': "There's a lot to read about consolidating loans, take a look at our site and you can find a lot more information: http://freestudentloanadvice.org/should-i-consolidate-my-loans/",



   'fraud' : 'Sometimes bad things happen to good people. Thankfully, there are often remedies for these things for borrowers of federal student loans. For the most part, student loan discharges are for situations where the loan should not have been made in the first place or for when something terrible happens, such as the death or disability of the borrower. Below are the requirements for the discharges that are currently available. You should note that in several of these cases, the discharged amount is taxed as income. Take a look at our page on loan forgiveness for more information: http://freestudentloanadvice.org/loan-forgiveness/',


   'id' : 'You can find more information on what to do about false identification on our site here: http://freestudentloanadvice.org/loan-forgiveness/false-certification/',


   'school_closed' : 'If your school has closed there may be other options, take a look on our site: http://freestudentloanadvice.org/loan-forgiveness/closed-school-discharge/',


   'death' : 'If the borrower of the loan, or, in the case of a Parent Plus loan either the borrower or the student for whom the loan was taken should pass away, the loan will be fully discharged. To apply, first contact the loan holder by phone, who will put the loan on hold for up to sixty days. Submit to them a certified copy of the death certificate to obtain the discharge. If there are loans at multiple loan holders, you will need to notify and submit these certificates to all of them. Note that the amount of the discharge may be taxed to the deceased estate as income: http://freestudentloanadvice.org/loan-forgiveness/death-discharge',


   'disability' : "Total and Permanent Disability Discharge (TPD) can be difficult to obtain so it’s very important to follow all instructions and respond to all requests in a timely way. This is due to significant fraud found in past audits of the program. Only the actual borrower of the loans disability status can be submitted for discharge review. All borrowers applying for this discharge must do so at http://www.disabilitydischarge.com. There's more information available here: http://freestudentloanadvice.org/loan-forgiveness/total-and-permanent-disability-discharge/",


   'unpaid': "If you withdrew from school before completing 60% of the academic year or loan period, the school may have been required to return all or a portion of your loan to the loan holder. There's more information here: http://freestudentloanadvice.org/loan-forgiveness/unpaid-refund-discharge/",

   'thank_you': "Thank you! Please feel free to reach out to us anytime either through messenger or on the web.",
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
            },
            {
              "content_type": "text",
              "title": "Should I consolidate my loans?",
              "payload": "<POSTBACK_PAYLOAD>",
              "image_url": "https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/256/refresh.png"
            },
          ],

    'loan_forgiveness' : [
         {
           "content_type": "text",
           "title": "Public Service Loan Forgiveness",
           "payload": "<POSTBACK_PAYLOAD>",
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

    # payment plans
    'payment_plans' : [
        {
          "content_type": "text",
          "title": "I have federal loans",
          "payload": "<POSTBACK_PAYLOAD>",
        },
        {
          "content_type": "text",
          "title": "I have private loans",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "I have both.",
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


    # past due or in default
    'pdod' : [
        {
          "content_type": "text",
          "title": "Federal loans past due but not in default",
          "payload": "<POSTBACK_PAYLOAD>",
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



    # should I consolidate
    'consolidate_1' : [
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


    # should I consolidate
    'fraud' : [
        {
          "content_type": "text",
          "title": "Closed School",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "Borrower Defense",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "False Certification", # TODO
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "Death",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "Disability",
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "Unpaid Refund", #TODO
          "payload": "<POSTBACK_PAYLOAD>"
        },
        {
          "content_type": "text",
          "title": "Bankruptcy",
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
