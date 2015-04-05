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
import ck.kernel as ck

sep='***************************************************************************'

euoa0='demo-variation-all'
euoa1='demo-variation-freq-high'
euoa2='demo-variation-freq-low'

puoa='3a2498cb437a87aa'
duoa='c8848a1b1fb1775e'

######################################################################
def run(i):

    euoa=i['data_uoa']
    n=i['repetitions']
    repeat=i.get('repeat',-1)
    
    for k in range(0,n):
        ck.out(sep)
        ck.out('Statistical repetition '+str(k+1)+' out of '+str(n)+' ...')

        ii={'action':'run',
            'module_uoa':'program',
            'data_uoa':puoa,
            'dataset_uoa':duoa,
            'out':'con'}
        if repeat!=-1: ii['repeat']=repeat

        r=ck.access(ii)
        if r['return']>0: return r

        misc=r['misc']
        ch=r['characteristics']

        rs=misc['run_success']
        if rs!='yes':
           return {'return':1, 'error':'execution failed! Check above output'}

        repeat=ch['repeat']
        et=ch['execution_time']
        tet=ch['total_execution_time']

        # Try to add to experiment
        ii={'action':'add',
            'module_uoa':'experiment',
            'experiment_uoa':euoa,
            'dict':{'characteristics':{'run':ch}, 'features':{'1':'thesame'}},
            'ignore_update':'yes',
            'process_multi_keys':['characteristics'],
            'search_point_by_features':'yes',
            'record_all_subpoints':'yes',
            'out':'con',
            'sort_keys':'yes'}
        r=ck.access(ii)
        if r['return']>0: return r

        ii['experiment_uoa']=euoa0
        r=ck.access(ii)
        if r['return']>0: return r

    return {'return':0, 'repeat':repeat}

######################################################################
n=10

ck.out('')
ck.out('Variation in results of the same experiments is not always considered')
ck.out('or results with high variation are simply removed.')

ck.out('')
ck.out('However, analysis of the density of such results ')
ck.out('together with peak detection can provide information ')
ck.out('about stable states in the system as well as missing features.')

ck.out('')
ck.out('Here, we show variation of execution time of the same benchmark')
ck.out('with the same data set executed multiple times with different')
ck.out('CPU frequency.')

ck.out('')

# Select number of repetitions
ck.out(sep)
r=ck.inp({'text':'Select number of repetitions of the experiment (or Press Enter for 10): '})
if r['return']>0:
   ck.err(r)
x=r['string'].strip()
if x!='': n=int(x)

# Trying to compile kernel
ck.out(sep)
ck.out('Compiling kernel ...')
ck.out('')

r=ck.access({'action':'compile',
             'module_uoa':'program',
             'out':'con',
             'data_uoa':puoa,
             'clean':'yes'})
if r['return']>0:
   ck.err(r)

# Check if data already exists and ask if should be cleaned
r=ck.access({'action':'load',
             'module_uoa':'experiment',
             'data_uoa':euoa1})
if r['return']==0:
   ck.out(sep)
   r=ck.inp({'text':'Old experimental data already exists, delete (Y/n):'})
   if r['return']>0: 
      ck.err(r)
   x=r['string'].strip().lower()
   if x!='n' and x!='no':
      ii={'action':'delete',
          'module_uoa':'experiment',
          'data_uoa':euoa0,
          'out':'con',
          'force':'yes'}

      r=ck.access(ii)

      ii['data_uoa']=euoa1
      r=ck.access(ii)

      ii['data_uoa']=euoa2
      r=ck.access(ii)

# Check if data already exists and ask if should be cleaned
r=ck.access({'action':'load',
             'module_uoa':'experiment',
             'data_uoa':euoa1})
if r['return']==0:
   r=ck.inp({'text':'Old experimental data already exists, delete (y/N):'})
   if r['return']>0: 
      ck.err(r)

########################
ck.out(sep)
ck.inp({'text':'Set power plan of your OS to "High performance" and press Enter'})

ii={'repetitions':n,
    'data_uoa':euoa1}

r=run(ii)
if r['return']>0:
   ck.err(r)

repeat=r['repeat']

########################
ck.out(sep)
ck.inp({'text':'Set power plan of your OS to "Energy saver" and press Enter'})

ii['repeat']=repeat
ii['data_uoa']=euoa2

r=run(ii)
if r['return']>0:
   ck.err(r)

exit(0)

