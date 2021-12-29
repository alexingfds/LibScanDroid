

# LibScanDroid

Recomandation Tool :  library recommendation

We make available the source code of LisbScanDroid for study and experimentation in this directory
GitHub: : https://github.com/alexingfds/LibScanDroid.
This directory contains four (4) main directories. The
The Results directory contains the results that were generated. The experimentation directory contains the results of the
experiments that have been done with LibScanDroid and another CrossRec library recommendation tool. 

The Resources directory contains the database we used. The viewing directory contains
json format files that allow you to view with the LibScanDroid site. The LibScanDroid website is
available in the following directory: https://github.com/stilab-ets/LibScanDroid.  This directory contains a file
index.html which allows you to launch the site for viewing libraries. The data directory contains the
json format for visualization. 

## Installation

Install [python 3.9](https://phoenixnap.com/kb/upgrade-python) .

```bash
sudo apt install python3.9
```
## Configuration

In this directory there is  the following files that can be run separately:
* VisualisatonLibScanDroidRUN.py : For genarting recommandations and visualistion file. We can set the value of parameters (maxEpsiolon, Epsion, minPoint ..)
* tenFoldsTrainingRUN : perfoming ten folds cross validation (PUC: pattern usage cohesion)
* RecallRateDBSCANRUN : Evaluate Recall rate and MRR. (Evaluation of recommandation)

# Troubleshooting
If you encounter any difficulties in working with the tool or the datasets, please do not hesitate to contact us at githe following email:  richardson.alexandre.1@ens.etsmtl.ca . We will try our best to answer you as soon as possible.