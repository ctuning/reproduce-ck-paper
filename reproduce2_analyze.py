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

####################################################################
ii={"action":"get",
    "module_uoa":"experiment",
    "experiment_module_uoa":"experiment",
    "experiment_data_uoa":euoa0,
    "flat_keys_list":[
      "##characteristics#run#execution_time#all"
    ],
   "ignore_point_if_none":"yes",
   "expand_list":"yes"}

r=ck.access(ii)
if r['return']>0: ck.err(r)

ctable0=r.get('table',{}).get('0',[])
if len(ctable0)==0:
   ck.err({'return':1,'error':'no expeirmental results found'})

ii['experiment_data_uoa']=euoa1
r=ck.access(ii)
if r['return']>0: ck.err(r)

ctable1=r.get('table',{}).get('0',[])
if len(ctable1)==0:
   ck.err({'return':1,'error':'no expeirmental results found'})

ii['experiment_data_uoa']=euoa2
r=ck.access(ii)
if r['return']>0: ck.err(r)

ctable2=r.get('table',{}).get('0',[])
if len(ctable2)==0:
   ck.err({'return':1,'error':'no expeirmental results found'})

####################################################################
# Apply statistics
r=ck.access({'action':'analyze',
             'module_uoa':'math.variation',
             'characteristics_table':ctable0})
if r['return']>0: ck.err(r)
evx0=r['xlist2s']
evy0=r['ylist2s']
nev0=len(evx0)

r=ck.access({'action':'analyze',
             'module_uoa':'math.variation',
             'characteristics_table':ctable1})
if r['return']>0: ck.err(r)
evx1=r['xlist2s']
evy1=r['ylist2s']
nev1=len(evx1)

r=ck.access({'action':'analyze',
             'module_uoa':'math.variation',
             'characteristics_table':ctable2})
if r['return']>0: ck.err(r)
evx2=r['xlist2s']
evy2=r['ylist2s']
nev2=len(evx2)

####################################################################
ck.out('All merged experimental results (high and low frequency):')
ck.out('  Number of detected expected values: '+str(nev0))
if nev0==2:
   ck.out('    Result reproduced! EV1/EV2='+('%2.2f'%(evx0[1]/evx0[0]))+' - should be high_freq/low_freq')
else:
   ck.out('    Result unexpected!')

ck.out('')
ck.out('High frequency experimental results:')
ck.out('  Number of detected expected values: '+str(nev1))
if nev1==1:
   ck.out('    Result reproduced!')
else:
   ck.out('    Result unexpected!')

ck.out('')
ck.out('Low frequency experimental results:')
ck.out('  Number of detected expected values: '+str(nev2))
if nev2==1:
   ck.out('    Result reproduced!')
else:
   ck.out('    Result unexpected!')

exit(0)

