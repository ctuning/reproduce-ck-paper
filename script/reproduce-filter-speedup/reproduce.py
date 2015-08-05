#
# Collective Knowledge (Experiment to check that filter optimizations 
#  may depend on image features and hence require run-time adaptation)
#
# See CK LICENSE.txt for licensing details
# See CK Copyright.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://cTuning.org/lab/people/gfursin
#

import os
import sys

print('')
print('We found considerable execution times speedup (~20%)')
print('when using -O3 -fno-if-conversion')
print('with older GCC < 4.7.x on different x86 processors')
print('for very dark images during crowd-tuning.')

print('')
print('Interestingly, newer GCC do not show speed up,')
print('and produce slower code than older GCC on such images.')

print('')
print('This motivates our continuous crowd-tuning approach')
print('combined with public repository of optimization knowledge,')
print('as described in http://arxiv.org/abs/1506.06256 .')

print('')
print('This script attemts to reproduce and validate our experiments,')
print('and share results (crowdsourcing experiments).')

print('')
print('Note: if you run this script on Windows, add --target_os=mingw-64')
print('      or --target_os=mingw-32 .')

arg=sys.argv
sarg=''
for q in sys.argv:
    if sarg=='': sarg=' ' # Pass first entry
    else: sarg+=' '+q

os.system('ck reproduce program.experiment.speedup @reproduce.json --check_speedup '+sarg)
