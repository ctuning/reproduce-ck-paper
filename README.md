# paper-ck-2015
Shared artifacts for our project and papers
on "Collective Mind" and "Collective Knowledge".

# Contact
* Grigori Fursin, Grigori.Fursin@cTuning.org
* Anton Lokhmotov, anton@dividiti.com

# Compatibility
* Linux, Windows, Android

# Dependencies:
* CK: http://github.com/ctuning/ck
* Various python packages:
** Linux: sudo apt-get install python-numpy python-scipy python-matplotlib 

# Installation using CK
> ck pull repo:ck-reproduce-paper-cm-2014-ck-2015

> ck pull repo:ck-env

> ck pull repo:ck-autotuning

> ck pull repo:ck-analytics

##########################################################
# Reproducible experiments (collaboratively validate assumption and report unexpected behavior for further analysis):

1) Validating that threshold filter needs 
run-time adaptation to achieve best performance 
and energy usage depending on the type of image:

To reproduce/validate expectation:

> cd script/reproduce-filter-speedup

> python reproduce.py

# From ipython notebook (check that CK is installed as python module): 
> ipython notebook reproduce.ipynb

##########################################################
2) Analysis of variation of experimental results
(for the same experiment) - density analysis
and peak detection can provide expected values
and missing features.

To reproduce/validate expecation (ck should be installed
as Python package using "ck setup kernel --install):
> cd script/reproduce-filter-visualize
> python reproduce2.py
