Threat Intel Risk Analysis A2 (Milestone2)

Mustafa Al-Obaidi October 2022

1  Introduction

During this milestone, there has been a significant amount of research and data collection performed by a group of students. I was able to work with a few of my classmates to collect the data from an online source. Also, the data was then processed and formatted into a Comma-separated values (CSV) file.

In this report, the collection and processing of the data will be explained. Also, the models that were used will be discussed in detail, including the results of each model. Additionally, we will look at the results and decide which model performed the best. Finally, we conclude by providing a possible improvement for the project.

2  Data Collection

The data collection was the challenging part of this assignment, as we spent a significant amount of time searching for the ideal data set to be used. While many websites provided access to phishing emails data sets, they were only a few that had new emails, as the majority had phishing emails that are older than 8 years. There is no doubt that attackers keep updating their methods of phishing attacks, and if we do not keep collecting evidence of those up- dated methods, then the detection models will not work against those new phishing emails. Thus, the majority of the phishing emails included in our data set are no older than 4 years.

The data was captured from two public sources namely Enron and mon- key.org [1, 2]. Also, the data set that was used to train the models consisted of more than 2300 phishing emails and more than 3050 legitimate emails.

3  Data Processing

The idea of processing the data is inspired by a paper that discusses phishing detection using Machine Learning. The data extracted from the email was parsed into a row with 8 columns namely Dots, PayPal, Bank, Account, Click, Fill, URL, and JavaScript. Dots is referred to the number of dots in the domain email of the sender, having more than one dot in the domain is an indicator of a possible phishing email. Also, words like PayPal, account, click, and fill are high indicators of a phishing email. Additionally, if the email contains a URL that could also be an indicator of a phishing email. Finally, if the email contains an embedded JavaScript then it is an indicator of a phishing email [3].

4  Models Used

In order to decide which models are the ideal solution for the current problem, different models were implemented. The three models that were used in this project were SVM, Logistic Regression, and Decision Tree. The detailed result of each model is provided in tables in the following subsections.

1. SVM

Table 1 provides a summary of the evaluation metrics of SVM using 10% testing size, 20% testing size and 30%testing size. While, The highest preci- sion was achieved using 30% testing size, the f1 score and recall were achieved using 20% testing size.

2. Logistic Regression

Table 2 provides a summary of the evaluation metrics of Logistic Regression using 10% testing size, 20% testing size and 30%testing size. The highest



|Evaluation Criteria of SVM|
| - |
|Metrics:|Precision|F1-Score|Recall|
|10% testing size:|0.814%|0.871%|0.936%|
|20% testing size:|0.836%|0.881%|0.931%|
|30% testing size:|0.840%|0.879%|0.921%|
Table 1: SVM Metrics

precision, f1 score and recall was accomplished using 20% testing size.



|Evaluation Criteria of Logistic Regression|
| - |
|Metrics:|Precision|F1-Score|Recall|
|10% testing size:|0.795%|0.861%|0.940%|
|20% testing size:|0.790%|0.864%|0.951%|
|30% testing size:|0.788%|0.858%|0.941%|
Table 2: Logistic Regression Metrics

3. Decision Tree

Table 3 provides a summary of the evaluation metrics of Decision Tree using 10% testing size, 20% testing size and 30%testing size. While, The highest precision was achieved using 30% testing size, the f1 score and recall were achieved using 10% testing size.



|Evaluation Criteria of Decision Tree|
| - |
|Metrics:|Precision|F1-Score|Recall|
|10% testing size:|0.837%|0.853%|0.870%|
|20% testing size:|0.848%|0.849%|0.85%|
|30% testing size:|0.871%|0.848%|0.827%|
Table 3: Decision Tree Metrics

5  Results Summary

From the previous sections we were able to observe that using SVM gave the overall best results when using 20% testing size with a precision value of 0.836, f1 score of 0.881 and a recall value of 0.931. Additionally, when using Decision Tree model, the overall best results were found using 10% testing size with a precision value of 0.837, f1 score of 0.853 and a recall value of 0.870. Similar to SVM, Logistic Regression gave the overall best results using a 20% testing size, with a precision value of 0.790, f1 score of 0.864 and a recall value of 0.951.

After constructing all the tables and comparing the results of each model to another, we are able to see that Logistic Regression model gave the highest recall value with 0.951. However, Logistic Regression gave the least precision value out of the three models. When deciding which model is the best to use, we need to look at the f1 score as it is balance between the precision and recall score. Therefore, in my personal opinion I think that it SVM is the ideal solution to the problem on hand [4].

6  Conclusion

After analyzing the results we were able to find that the model that performed the best was SVM. However, the results are not optimized, as there is room for improvement in the future. To find a better solution we need to either improve the precision value of the Logistic Regression or the Recall value of the SVM.

References

1. “Enron email dataset.” [Online]. Available: https://www.cs.cmu.edu/ en- ron/
1. [Online]. Available: https://monkey.org/ jose/phishing/
1. S. Rawal, B. Rawal, A. Shaheen, and S. Malik, “Phishing detection in e-mails using machine learning,” International Journal of Applied Infor- mation Systems, vol. 12, pp. 21–24, 2017.
1. J. Brownlee, “How to calculate metrics for imbalanced classification.” [Online]. Available: https://machinelearningmastery.com/precision- recall-and-f-measure-for-imbalanced-classification
5
