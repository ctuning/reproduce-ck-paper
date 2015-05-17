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
import copy
import ck.kernel as ck

sep='***************************************************************************'

euoax='reproduce-paper-cm2014-variation-'
euoa0=euoax+'all'
euoa1=euoax+'high'
euoa2=euoax+'low'

puoa='3a2498cb437a87aa' # "shared-codelet-filter" can be used, but UIDs allow to fix program version
duoa='c8848a1b1fb1775e' # "image-raw-bin-fgg-office-day-gray" can be used, but UIDs allow to fix data set version

######################################################################
def run(i):

    curdir=os.getcwd()

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
    ck.out('Note: Please, check that SciPy and NumPy are installed!')

    ck.out('')

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
              'data_uoa':euoax+'*',
              'out':'con',
              'force':'yes'}
          r=ck.access(ii)
          if r['return']>0: return r

    # Select number of repetitions
    ck.out(sep)
    n=10
    r=ck.inp({'text':'Select number of repetitions of the experiment (or Press Enter for '+str(n)+'): '})
    if r['return']>0:
       ck.err(r)
    x=r['string'].strip()
    if x!='': n=int(x)

    ########################
    ck.out(sep)
    ck.inp({'text':'Set power plan of your OS to "High performance" and press Enter'})

    iii={'action':'run',
        'module_uoa':'pipeline',
        'data_uoa':'program',
        'program_uoa':puoa,
        'dataset_uoa':duoa,
        'repetitions':n,
        'record':euoa1,
        'out':'con'}

    ii=copy.deepcopy(iii)
    r=ck.access(ii)
    if r['return']>0: return r

    if r.get('fail','')=='yes':
       return {'return':1, 'error':'universal program pipeline execution failed ('+r.get('fail_reason','')+')! Check above output'}

    # Reuse later state and deps
    state=r['state']
    deps=r['dependencies']

    ########################
    ck.out(sep)
    ck.inp({'text':'Set power plan of your OS to "Energy saver" and press Enter'})

    ii=copy.deepcopy(iii)
    ii['record']=euoa2
    ii['state']=state          # reuse found run-time repetitions, etc
    ii['dependencies']=deps    # reuse compiler dependencies
# remark next ones, otherwise we will not be able to replay this experiment (no compile)
#    ii['clean']='no'           # do not clean tmp directory, i.e. do not delete executable
#    ii['no_compile']='yes'     # no need recompile code
    ii['no_state_check']='yes' # otherwise, universal program autotuning pipeline should detect that frequency changed during experiments!

    r=ck.access(ii)
    if r['return']>0: return r

    if r.get('fail','')=='yes':
       return {'return':1, 'error':'universal program pipeline execution failed ('+r.get('fail_reason','')+')! Check above output'}

    ########################
    ck.out(sep)
    ck.inp({'text':'Experiments finished. Press Enter to analyze them'})

    os.chdir(curdir)
    os.system("python reproduce_analyze")

    return {'return':0}

######################################################################
r=run({})
if r['return']>0:
   ck.err(r)
   exit(1)
