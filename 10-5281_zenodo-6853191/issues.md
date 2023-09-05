## Issues

There are numerous differences within Table 3 from the reproduced run, but all of the values seems within a reasonable bound of the reported results.

The BERT model with a Binary classifier, the Random Forest (RF) model with a Multi-class Multi-label (MCML) classifier, and the BERT model with a MCML classifier have differing results on each run. The best results for each column switches between the Binary and MCML classifier with the BERT model.

There are also some results for the Naive Baves (NB), Random Forest (RF), and Logistic Regression (LR) models with a Binary classifier which could either be considered typos or a more significant difference. Though, the results would still be within a reasonable bound:

* Apply
    * NB
        * F1 0.668 -> 0.669
* Analyze
    * RF
        * Acc 0.961 -> 0.959
        * Cohen's K 0.851 -> 0.843
        * AUC 0.902 -> 0.897
        * F1 0.874 -> 0.866
* Evaluate
    * RF
        * Cohen's K 0.887 -> 0.888
        * F1 0.907 -> 0.908
* Create
    * LR
        * Cohen's K 0.604 -> 0.605
    * RF
        * Acc 0.943 -> 0.944
        * Cohen's K 0.792 -> 0.794
        * AUC 0.877 -> 0.875
        * F1 0.826 -> 0.827
