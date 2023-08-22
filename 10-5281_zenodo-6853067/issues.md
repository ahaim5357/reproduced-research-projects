## Issues

### Figures 2-5

Based on some analysis of the graphs, this assumes that condition A is condition 1 and condition B is condition 3.

* The graphs reported for Figure 2 roughly follow similar trends after running multiple attempts of the codebase; however, the individaul shape differs quite a bit, likely due to randomness.
* Aside from AUC, the graphs reported for Figure 3 can widely greatly, having different trends across multiple attempts.
* Aside from AUC and rθ, the graphs reported for Figure 4 can widely greatly, having different trends across multiple attempts.
* The train time for hyperparameters in Figure 5 is similar except for the SPARFA model, which had an odd training time on the reproduced machine.

### Reported Results in Table 2

* After running the fixed methods multiple times, there are likely a few typos in the result:
    * SparFAE_f (AUC)
        * 0.88 +- 0.04 -> 0.88 +- 0.05
* The following are likely due to differences in the machines used:
    * VIBO_f (Training Time)
        * 8.01 +- 5.59 -> 10.62 +- 6.97
    * SparFAE_f (Training Time)
        * 0.05 +- 0.03 -> 0.05 +- 0.02
    * VIBO_f (Prediction Time)
        * 1.31 +- 2.76 -> 2.01 +- 2.56
    * SparFAE_f (Prediction Time)
        * 0.15 +- 0.13 -> 0.18 +- 0.00

* After running the experiment methods multiple times, there are likely a few typos in the result:
    * SPARFA (Sparsity)
        * 0.16 +- 0.06 -> 0.16 +- 0.07
    * VIBO (Sparsity)
        * 0.00 +- 0.00 -> 0.00 +- 0.01
    * SparFAE2 (Sparsity)
        * 0.33 +- 0.10 -> 0.33 +- 0.11
* The following are likely due to differences in the machines used; however, the results are quite similar to those reported, so it could also be interpreted as a potential typo:
    * Training Time
        * SPARFA: 31.0 +- 20.9 -> 31.0 +- 21.2
        * VIBO: 7.83 +- 5.12 -> 7.83 +- 5.21
        * SparFAE1: 1.94 +- 1.78 -> 1.94 +- 1.95
        * SparFAE2: 15.7 +- 15.9 -> 15.7 +- 18.8
    * Prediction Time
        * SPARFA: 633 +- 444 -> 634 +- 458
        * VIBO: 0.31 +- 0.18 -> 0.31 +- 0.50
        * SparFAE1: 0.19 +- 0.12 -> 0.19 +- 0.35
        * SparFAE2: 0.20 +- 0.13 -> 0.20 +- 0.36

* The Wilcoxon Signed-Rank Test is reported backwards, meaning that the sentence should read, "Method 1 has lower AUC than Method 2".

### Figures 6-8

* Figures 7 and 8 are not generated in the codebase.
* Only the number of skills in Figure 6 is generated, but without the lines of best fit. However, the points are essentially accurate to those in the paper.
