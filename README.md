CK repository to reproduce our recent papers
============================================

[![logo](https://github.com/ctuning/ck-guide-images/blob/master/logo-powered-by-ck.png)](http://cKnowledge.org)
[![logo](https://github.com/ctuning/ck-guide-images/blob/master/logo-validated-by-the-community-simple.png)](http://cTuning.org)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Shared artifacts in the [Collective Knowledge Format](https://github.com/ctuning/ck) 
with JSON API and JSON meta information to reproduce and extend techniques from
the following papers on "Collective Mind" and "Collective Knowledge":

* http://arxiv.org/abs/1506.06256
* http://hal.inria.fr/hal-01054763
* https://hal.inria.fr/inria-00436029
* http://arxiv.org/abs/1407.4075

Status
======
This is more a proof-of-concept repository. You can find reproducible workflows
and articles in the CK format from the latest computer systems' conferences
[here](http://cTuning.org/ae).

For example, check out this reusable and customizable artifact from [CGO'17](http://cgo.org/cgo2017) 
with automatic cross-platform software installation and web-based experimental dashboard powered 
by the CK framework: 
* [GitHub CK repo](https://github.com/SamAinsworth/reproduce-cgo2017-paper)
* [Paper with artifact appendix](http://cTuning.org/ae/resources/paper-with-distinguished-ck-artifact-and-ae-appendix-cgo2017.pdf)
* [PDF snapshot of the interactive CK dashboard](https://github.com/SamAinsworth/reproduce-cgo2017-paper/files/618737/ck-aarch64-dashboard.pdf)
* [CK concepts](https://michel-steuwer.github.io/About-CK)

Authors
=======

* [Grigori Fursin](http://fursin.net/research.html), dividiti/cTuning foundation
* [Anton Lokhmotov](https://www.hipeac.net/~anton), dividiti

Prerequisites
=============
* [Collective Knowledge Framework](http://github.com/ctuning/ck)

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

> python reproduce.py

Feedback
========
* https://groups.google.com/forum/#!forum/collective-knowledge
