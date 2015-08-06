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

euoax='reproduce-ck-paper-variation-'
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
    ck.out('You can find more details in our paper https://hal.inria.fr/hal-01054763')

    ck.out('')
    ck.out('Note: please, check that SciPy and NumPy are installed!')

    ck.out('')

    # Read json file
    r=ck.load_json_file({'json_file':'reproduce.json'})
    if r['return']>0: return r
    d=r['dict']

    ap_max=d.get('add_to_pipeline_max',{})
    ap_min=d.get('add_to_pipeline_min',{})

    # Check if data already exists and ask if should be cleaned
    r=ck.access({'action':'list',
                 'module_uoa':'experiment',
                 'data_uoa':euoax+'*'})
    if r['return']==0:
       lst=r['lst']
       if len(lst)>0:
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
    ck.inp({'text':'Set power plan of your OS to "maximum (high) performance" and press Enter'})

    iii={'action':'run',
         'module_uoa':'pipeline',
         'data_uoa':'program',
         'program_uoa':puoa,
         'dataset_uoa':duoa,
         'repetitions':n,
         'record':'yes',
         'record_uoa':euoa1,
         'out':'con'}
    iii.update(ap_max)

    ii=copy.deepcopy(iii)
    r=ck.access(ii)
    if r['return']>0: return r

    lio=r.get('last_iteration_output',{})

    fail=lio.get('fail','')

    if fail=='yes':
       return {'return':1, 'error':'universal program pipeline execution failed ('+lio.get('fail_reason','')+')- check above output and possibly report to the authors!'}

    # Reuse later state and deps
    lio=r.get('last_iteration_output',{})
    state=lio.get('state',{})

    ed=r.get('experiment_desc',{})
    deps=ed.get('dependencies',{})

    ########################
    ck.out(sep)
    ck.inp({'text':'Set power plan of your OS to "power saver (minimal performance)" and press Enter'})

    ii=copy.deepcopy(iii)
    ii['record_uoa']=euoa2
    ii['state']=state          # reuse found run-time repetitions, etc
    ii['dependencies']=deps    # reuse compiler dependencies
# remark next 2 lines, otherwise we will not be able to replay this experiment (no compile)
#    ii['clean']='no'           # do not clean tmp directory, i.e. do not delete executable
#    ii['no_compile']='yes'     # no need recompile code
    ii['no_state_check']='yes' # otherwise, universal program autotuning pipeline should detect that frequency changed during experiments!
    ii.update(ap_min)

    r=ck.access(ii)
    if r['return']>0: return r

    lio=r.get('last_iteration_output',{})

    fail=lio.get('fail','')

    if fail=='yes':
       return {'return':1, 'error':'universal program pipeline execution failed ('+lio.get('fail_reason','')+')- check above output and possibly report to the authors!'}

    ########################
    ck.out(sep)
    ck.inp({'text':'Experiments finished. Press Enter to analyze them'})

    os.chdir(curdir)
    os.system("python reproduce_analyze.py")

    return {'return':0}

######################################################################
r=run({})
if r['return']>0:
   ck.err(r)
   exit(1)
