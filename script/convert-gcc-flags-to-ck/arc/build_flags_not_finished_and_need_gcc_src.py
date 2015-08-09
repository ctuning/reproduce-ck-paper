#!/usr/bin/python

import re
from pyparsing import *
import json
import sys

var_gcc_path ='/home/abdul/damm02/compilers/gcc-5.2.0/src-infra/'
var_inv_texi_path = var_gcc_path + 'gcc-5.2.0/gcc/doc/invoke.texi'
var_gcc_params_path = var_gcc_path + 'gcc-5.2.0/gcc/params.def'

json_out = open ("desc.json", "w")

var_inv_texi = open (var_inv_texi_path, 'r').read ()
var_params = open (var_gcc_params_path, 'r').read ()

data = {'all_compiler_flags_desc':{}}
data['all_compiler_flags_desc']['##base_opt'] = {}
data['all_compiler_flags_desc']['##base_opt']['choice'] = []

match = re.search (r'(?:@item Optimization.*?)(?:gccoptlist)(.*?)(?=\n\n)', var_inv_texi, re.DOTALL | re.MULTILINE)

result = match.group(1).replace('\n', ' ').replace('\r', ' ').replace('@gol', '')
result = result.lstrip("{")
result = result[:-2]
result = result.split()

flag = Word (alphas+"-"+nums+"@")
enclosed = Forward()
nestedBrackets = nestedExpr('[', ']', content=enclosed) 
nestedCurlies = nestedExpr('{', '}', content=enclosed) 
enclosed << (OneOrMore(flag) | Literal("=") | Suppress(oneOf("@")))

for i in result:
    if i.startswith ('-f'):
        d1 = enclosed.scanString (i)
        d1 = list (d1)

        if (len (d1) > 1):
            str1 = d1[0][0][0] + d1[1][0][0]
            str1_ = str1.replace('-', '##', 1)
            str1_ = str1_.replace('-', '_')
            str1_ = str1_[:-1]
            str2 = 'integer'
        else:
            str1 = d1[0][0][0]
            str1_ = str1.replace('-', '##', 1)
            str1_ = str1_.replace('-', '_')
            str2 = 'text'
        
        data['all_compiler_flags_desc'][str1_] = {}
        data['all_compiler_flags_desc'][str1_]['can_omit'] = 'yes'

        if (str1.endswith('=') == False):
            data['all_compiler_flags_desc'][str1_]['choice'] = [str1, str1.replace('-f', '-fno-')]
            
        data['all_compiler_flags_desc'][str1_]['default'] = ''
        data['all_compiler_flags_desc'][str1_]['desc'] = 'compiler flag: ' + str1

        if (str1.endswith ('=')):
            data['all_compiler_flags_desc'][str1_]['explore_prefix'] = str1
            data['all_compiler_flags_desc'][str1_]['explore_start'] = 1
            data['all_compiler_flags_desc'][str1_]['explore_step'] = 1
            data['all_compiler_flags_desc'][str1_]['explore_stop'] = 64

        data['all_compiler_flags_desc'][str1_]['tags'] = ['basic', 'optimization']
        data['all_compiler_flags_desc'][str1_]['type'] = str2
    
    if i.startswith ('-O'):
        data['all_compiler_flags_desc']['##base_opt']['choice'].append(i)
        data['all_compiler_flags_desc']['##base_opt']['default'] = ''
        data['all_compiler_flags_desc']['##base_opt']['desc'] = "base compiler flags"
        data['all_compiler_flags_desc']['##base_opt']['tags'] = ['base', 'basic', 'optimization']
        data['all_compiler_flags_desc']['##base_opt']['type'] = 'text'

'''
Process parameters
'''

match = re.search (r'(?:@item --param.+?)(?:gcctabopt)(.+?)(?=@end table)', var_inv_texi, re.DOTALL | re.MULTILINE)
match = re.findall (r'(?:@item\s)(.*)', match.group(1))

flag = Word(alphas+nums+'_ -  \n .')
enclosed = Forward()
nestedBrackets = nestedExpr('(', ')', content=enclosed)
enclosed << (flag | nestedBrackets)

match_1 = re.findall(r'(DEFPARAM ?\(.*?)(?=\)\n)', var_params, re.DOTALL | re.MULTILINE)

params_values={}

for i in match_1:
    str3 = list (enclosed.searchString(i))
    params_values[str3[2][0]] = [ str3[len (str3)-1][0], str3[len (str3)-2][0], str3[len (str3)-3][0] ]

for i in match:
    str1_ = "##param_" + i
    str1_ = str1_.replace('-', '_')
    data['all_compiler_flags_desc'][str1_]={}
    data['all_compiler_flags_desc'][str1_]['can_omit'] = 'yes'
    
    if i in params_values:
        data['all_compiler_flags_desc'][str1_]['default'] = params_values[i][2]
    else:
        data['all_compiler_flags_desc'][str1_]['default'] = ''
        
    data['all_compiler_flags_desc'][str1_]['desc'] = "compiler flag: --param " + i
    data['all_compiler_flags_desc'][str1_]['explore_prefix'] = "--param " + i + "="

    if i in params_values:
        data['all_compiler_flags_desc'][str1_]['explore_start'] = params_values[i][1]
        data['all_compiler_flags_desc'][str1_]['explore_step'] = 1
        data['all_compiler_flags_desc'][str1_]['explore_stop'] = params_values[i][0]
    else:
        data['all_compiler_flags_desc'][str1_]['explore_start'] = 0
        data['all_compiler_flags_desc'][str1_]['explore_step'] = 0
        data['all_compiler_flags_desc'][str1_]['explore_stop'] = 0
        
    data['all_compiler_flags_desc'][str1_]['tags'] = ['basic', 'optimization']
    data['all_compiler_flags_desc'][str1_]['type'] = 'integer'

json.dump (data, json_out, sort_keys=True, indent=2)
json_out.flush()
