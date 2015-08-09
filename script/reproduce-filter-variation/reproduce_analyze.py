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
    "load_json_files":["features"],
    "expand_list":"yes"}
r=ck.access(ii)
if r['return']>0: ck.err(r)

features={}
xchoices={}

points=r.get('points',[])
if len(points)>0:
   x=points[0].get('features',{})
   features=x.get('features',{})
   xchoices=x.get('choices',{})

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

result={}

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
ratio1=-1
if len(ftable1)>0 and len(ftable2)>0:
   ratio1=ftable1[0]/ftable2[0]

   result['freq_max']=ftable1[0]
   result['freq_min']=ftable2[0]

####################################################################
ck.out('')
ck.out('Validation of experimental results on your machine and detection of unexpected behavior (crowdsourcing experimentation):')

xunexpected=False

######################################
ck.out('')
ck.out('All merged experimental results (high and low frequency):')
ck.out('  Number of detected expected values (should be 2): '+str(nev0))

result['num_expected_values_all']=nev0
unexpected=False
if nev0==2:
   ck.out('    Result reproduced!')
else:
   unexpected=True
   xunexpected=True
   ck.out('    Result unexpected!')
result['unexpected_all']=unexpected

######################################
ck.out('')
ck.out('  Ratio of Expected value for low freq/expected value for high freq')
ck.out('    Should be approximately equal for high freq/low freq: '+'%2.2f'%(ratio0)+' vs '+'%2.2f'%(ratio1))

result['char_expected_value_low_div_expected_value_high']=ratio0
result['char_freq_low_div_freq_high']=ratio1

dif=ratio0/ratio1

result['char_ratio_expected_value_div_ratio_freq']=dif
unexpected=False
if dif<0.91 or dif>1.1:
   unexpected=True
   xunexpected=True
   ck.out('    Result unexpected!')
else:
   ck.out('    Result reproduced!')
result['unexpected_dif_between_ratios']=unexpected

######################################
ck.out('')
ck.out('High frequency experimental results:')
ck.out('  Number of detected expected values (should be 1): '+str(nev1))

result['num_expected_values_high']=nev1
unexpected=False
if nev1==1:
   ck.out('    Result reproduced!')
else:
   unexpected=True
   xunexpected=True
   ck.out('    Result unexpected!')
result['unexpected_high']=unexpected

######################################
ck.out('')
ck.out('Low frequency experimental results:')
ck.out('  Number of detected expected values (should be 1): '+str(nev2))

result['num_expected_values_low']=nev2
unexpected=False
if nev2==1:
   ck.out('    Result reproduced!')
else:
   unexpected=True
   xunexpected=True
   ck.out('    Result unexpected!')
result['unexpected_low']=unexpected

# Sharing unexpected behavior
if xunexpected:
   # Read config json file
   r=ck.load_json_file({'json_file':'reproduce_analyze.json'})
   if r['return']>0: 
      ck.err(r)
      exit(r['return'])
   dd=r['dict']

   e_repo_uoa=dd.get("experiment_repo_uoa","")
   e_remote_repo_uoa=dd.get("experiment_remote_repo_uoa","")
   e_uoa=dd.get("experiment_uoa","")

   ck.out('')
   ck.out('Warning: unexpected behavior detected!')
   r=ck.inp({'text':'Would you like to share this result with the community, author or Artifact Evaluation Committee via public "remote-ck" web service (Y/n): '})
   x=r['string'].lower()
   if x=='' or x=='yes' or x=='y':
      ii={'action':'add',
          'module_uoa':'experiment',

          'repo_uoa':e_repo_uoa,
          'experiment_repo_uoa':e_remote_repo_uoa,
          'experiment_uoa':e_uoa,

          'sort_keys':'yes',

          'dict':{
            'dict':{'subview_uoa':'reproduce-ck-paper-variation'},

            'tags':['crowdsource experiments','ck-paper','filter','variation'],

            'features':features,
            'choices':xchoices,
            'characteristics': result
          }
         }

      r=ck.access(ii)
      if r['return']>0: 
         ck.err(r)
         exit(r['return'])

      ck.out('')
      ck.out('  Results shared successfully!')

      ck.out('')
      ck.out('  You can see all shared results at http://cknowledge.org/repo/web.php?wcid=bc0409fb61f0aa82:8404df882462f978&subview=reproduce-ck-paper-filter')

ck.out('')
ck.out('Thank you for participating in experiment crowdsourcing!')

exit(0)

