import ck.kernel as ck
import json
import sys


def filter_data(i):
    changed='no'

    dd=i['dict']

    cols=dd.get('##features#image cols#min','')
    rows=dd.get('##features#image cols#min','')

    cpu_freq=dd.get('##features#cpu_freq#min','')
    gpu_freq=dd.get('##features#gpu_freq#min','')
    size=dd.get('##features#size#min','')

    cpu=dd.get('##characteristics#cpu#min','')
    cpur=dd.get('##characteristics#cpu#range_percent','')

    gpu_only=dd.get('##characteristics#gpu_only#min','')
    gpu_onlyr=dd.get('##characteristics#gpu_only#range_percent','')

    gpu_copy=dd.get('##characteristics#gpu_copy#min','')
    gpu_copyr=dd.get('##characteristics#gpu_copy#range_percent','')

    if cols!='' and rows!='':
       changed='yes'

       icols=int(cols)
       irows=int(rows)

       icpu_freq=int(cpu_freq)
       igpu_freq=int(gpu_freq)
       isize=int(size)

       fcpu=float(cpu)
       fgpu_only=float(gpu_only)
       fgpu_copy=float(gpu_copy)

       isize=icols*irows
       dd['##features#image size#min']=isize

       fsize_div_cpu_freq=float(isize/icpu_freq)
       fsize_div_gpu_freq=float(isize/igpu_freq)

       dd['##features#size_div_by_cpu_freq#min']=fsize_div_cpu_freq
       dd['##features#size_div_by_gpu_freq#min']=fsize_div_gpu_freq

       factor=float(icpu_freq)/float(igpu_freq)
       dd['##features#cpu_freq_div_by_gpu#min']=factor

       dd['##features#size_div_by_cpu_div_by_gpu_freq#min']=float(isize/factor)

       fimage_size_div_by_cpu_freq=float(isize/icpu_freq)
       dd['##features#image_size_div_by_cpu_freq#min']=fimage_size_div_by_cpu_freq

       fcpur=float(cpur)
       fgpu_onlyr=float(gpu_onlyr)
       fgpu_copyr=float(gpu_copyr)

       if '##characteristics#cpu_div_by_gpu_copy#min' in dd: del(dd['##characteristics#cpu_div_by_gpu_copy#min'])
       if '##characteristics#cpu_div_by_gpu_only#min' in dd: del(dd['##characteristics#cpu_div_by_gpu_only#min'])
       if '##characteristics#cpu_div_by_gpu_copy' in dd: del(dd['##characteristics#cpu_div_by_gpu_copy'])
       if '##characteristics#cpu_div_by_gpu_only' in dd: del(dd['##characteristics#cpu_div_by_gpu_only'])
       if '##features#processed#min' in dd: del(dd['##features#processed#min'])
       if '##characteristics#cpu_div_by_gpu_copy' in dd: del(dd['##characteristics#cpu_div_by_gpu_copy'])
       if '##characteristics#cpu_div_by_gpu_only' in dd: del(dd['##characteristics#cpu_div_by_gpu_only'])

#       if fcpur<0.07 and fgpu_onlyr<0.07 and fgpu_copyr<0.07:
#       dd['##features#processed#min']='yes'

       dd['##characteristics#cpu_div_by_gpu_copy#min']=fcpu/fgpu_copy
       dd['##characteristics#cpu_div_by_gpu_only#min']=fcpu/fgpu_only
       
       if (fcpu/fgpu_copy)>1.07:
          dd['##characteristics#gpu_copy_is_much_better_cpu#min']=True
       else:
          dd['##characteristics#gpu_copy_is_much_better_cpu#min']=False

       if (fcpu/fgpu_only)>1.07:
          dd['##characteristics#gpu_only_is_much_better_cpu#min']=True
       else:
          dd['##characteristics#gpu_only_is_much_better_cpu#min']=False

    return {'return':0, 'changed':changed, 'dict':dd}

########################################################
ff=getattr(sys.modules[__name__], 'filter_data')

ii={'action':'filter',
    'module_uoa':'experiment',
    'out':'con',
    'filter_func_addr':ff}

r=ck.load_json_file({'json_file':'filter-add-characteristic-gpu-copy-is-much-better-cpu.py'})
if r['return']>0: 
   ck.out('Error:'+r['error'])
   exit(1)

ii.update(r['dict'])

r=ck.access(ii)
if r['return']>0: 
   ck.out('Error:'+r['error'])
   exit(1)

exit(0)
