In the report I have included a section that explains the data Collection and data Processing, but I am also including them here as 
requested in the assignment description.

dataset description:

Data Collection:

The data collection was the challenging part of this assignment, as we spent a
significant amount of time searching for the ideal data set to be used. While
many websites provided access to phishing emails data sets, they were only a
few that had new emails, as the majority had phishing emails that are older
than 8 years. There is no doubt that attackers keep updating their methods
of phishing attacks, and if we do not keep collecting evidence of those updated methods, then the detection models will not work against those new
phishing emails. Thus, the majority of the phishing emails included in our
data set are no older than 4 years.
The data was captured from two public sources namely Enron and monkey.org [1, 2]. Also, the data set that was used to train the models consisted
of more than 2300 phishing emails and more than 3050 legitimate emails.



Data Processing:

The idea of processing the data is inspired by a paper that discusses phishing
detection using Machine Learning. The data extracted from the email was
parsed into a row with 8 columns namely Dots, PayPal, Bank, Account,
Click, Fill, URL, and JavaScript. Dots is referred to the number of dots in
the domain email of the sender, having more than one dot in the domain is
an indicator of a possible phishing email. Also, words like PayPal, account,
click, and fill are high indicators of a phishing email. Additionally, if the
email contains a URL that could also be an indicator of a phishing email.
Finally, if the email contains an embedded JavaScript then it is an indicator
of a phishing email [3].


References:

[1] “Enron email dataset.” [Online]. Available: https://www.cs.cmu.edu/ enron/
[2] [Online]. Available: https://monkey.org/ jose/phishing/
[3] S. Rawal, B. Rawal, A. Shaheen, and S. Malik, “Phishing detection in
e-mails using machine learning,” International Journal of Applied Information Systems, vol. 12, pp. 21–24, 2017.



