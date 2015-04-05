# paper-ck-2015
Shared artifacts for our project and papers
on "Collective Mind" and "Collective Knowledge".

# Installation using CK
ck pull repo:paper-ck-2015
ck pull repo:ck-env
ck pull repo:ck-autotuning
ck pull repo:ck-analytics

##########################################################
# Reproducible experiments:
1) Validating that threshold filter needs 
run-time adaptation to achieve best performance
and energy usage depending on the type of image:

To reproduce/validate expectation:
> python reproduce1.py

# From ipython notebook (check that CK is installed as python module): 
> iptyhon notebook reproduce1.ipynb

##########################################################
2) Analysis of variation of experimental results
(for the same experiment) - density analysis
and peak detection can provide expected values
and missing features.

To reproduce/validate expecation (ck should be installed
as Python package using "ck setup kernel --install):
> python reproduce2.py
