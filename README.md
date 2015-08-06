CK repository to reproduce paper
================================

Shared artifacts to reproduce and extend techniques from
the following papers on "Collective Mind" and "Collective Knowledge":

* http://arxiv.org/abs/1506.06256
* http://hal.inria.fr/hal-01054763
* https://hal.inria.fr/inria-00436029
* http://arxiv.org/abs/1407.4075

Status
======
THIS REPOSITORY IS NOT STABLE AND IS 
IN ACTIVE DEVELOPMENT. PLEASE, USE IT 
AT YOUR OWN RISK UNTIL OFFICIAL RELEASE!

Authors
=======

* Grigori Fursin, cTuning foundation (France) / dividiti (UK), Grigori.Fursin@cTuning.org
* Anton Lokhmotov, dividiti (UK), anton@dividiti.com

Installation
============

Compatibility
* Linux, Windows, Android

Dependencies:
* CK: http://github.com/ctuning/ck
* Various python packages on Linux: sudo apt-get install python-numpy python-scipy python-matplotlib 

> ck pull repo:reproduce-ck-paper

Usage
=====

##########################################################
# Reproducible experiments (collaboratively validate assumption and report unexpected behavior for further analysis):

1) Validating that threshold filter needs 
run-time adaptation to achieve best performance 
and energy usage depending on the type of image:

To reproduce/validate expectation:

> cd script/reproduce-filter-speedup

> python reproduce.py

# From ipython notebook (check that CK is installed as python module): 

If (un)expected behavior is reported (considerable slow downs or speedups
for the first 2 optimizations), you will be asked to share results
in a public cknowledge.org/repo to demonstrate crowdsourcing
of experimentation and validation of results.

You can later view shared results at
 http://cknowledge.org/repo/web.php?wcid=bc0409fb61f0aa82:8404df882462f978&subview=reproduce-ck-paper-filter

> cp reproduce.ipynb.remove_this_extension reproduce.ipynb
> ipython notebook reproduce.ipynb

##########################################################
2) Analysis of variation of experimental results
(for the same experiment) - density analysis
and peak detection can provide expected values
and missing features.

To reproduce/validate expecation (ck should be installed
as Python package using "ck setup kernel --install):
> cd script/reproduce-filter-variation

> python reproduce2.py
