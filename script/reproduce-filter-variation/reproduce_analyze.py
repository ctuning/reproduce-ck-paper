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

euoax='reproduce-ck-paper-variation-'
euoa1=euoax+'high'
euoa2=euoax+'low'

####################################################################
ii={"action":"get",
    "module_uoa":"experiment",
    "experiment_module_uoa":"experiment",
    "data_uoa_list":[euoa1,euoa2],
    "flat_keys_list":["##characteristics#run#execution_time_kernel_0#all"],
    "ignore_point_if_none":"yes",
    "ignore_graph_separation":"yes",
    "expand_list":"yes"}
r=ck.access(ii)
if r['return']>0: ck.err(r)
xctable0=r.get('table',{}).get('0',[])
if len(xctable0)==0:
   ck.err({'return':1,'error':'no expeirmental results found'})

ii['data_uoa_list']=[euoa1]
r=ck.access(ii)
if r['return']>0: ck.err(r)
xctable1=r.get('table',{}).get('0',[])
if len(xctable1)==0:
   ck.err({'return':1,'error':'no expeirmental results found'})

ii['data_uoa_list']=[euoa2]
r=ck.access(ii)
if r['return']>0: ck.err(r)
xctable2=r.get('table',{}).get('0',[])
if len(xctable2)==0:
   ck.err({'return':1,'error':'no expeirmental results found'})

####################################################################
ii={"action":"get",
    "module_uoa":"experiment",
    "experiment_module_uoa":"experiment",
    "data_uoa_list":[euoa1,euoa2],
    "flat_keys_list":["##features#platform#cpu#current_freq#0#all"],
    "ignore_point_if_none":"yes"}
r=ck.access(ii)
if r['return']>0: ck.err(r)
yctable0=r.get('table',{}).get('0',[])

ii['data_uoa_list']=[euoa1]
r=ck.access(ii)
if r['return']>0: ck.err(r)
yctable1=r.get('table',{}).get('0',[])

ii['data_uoa_list']=[euoa2]
r=ck.access(ii)
if r['return']>0: ck.err(r)
yctable2=r.get('table',{}).get('0',[])

# Convert all sub-points into a list
ctable0=[]
ctable1=[]
ctable2=[]

for q in xctable0:
    q0=q[0]
    ctable0.append(q0)

for q in xctable1:
    q0=q[0]
    ctable1.append(q0)

for q in xctable2:
    q0=q[0]
    ctable2.append(q0)

ftable0=[]
ftable1=[]
ftable2=[]

for q in yctable0:
    q0=q[0]
    ftable0.append(q0)

for q in yctable1:
    q0=q[0]
    ftable1.append(q0)

for q in yctable2:
    q0=q[0]
    ftable2.append(q0)

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

ratio0=evx0[1]/evx0[0]

####################################################################
if len(ftable1)>0 and len(ftable2)>0:
   ratio1=ftable1[0]/ftable2[0]

   print ratio0, ratio1

####################################################################
ck.out('All merged experimental results (high and low frequency):')
ck.out('  Number of detected expected values: '+str(nev0))
if nev0==2:
   ck.out('    Result reproduced! EV1/EV2='+('%2.2f'%(ratio0))+' - should be high_freq/low_freq')
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

