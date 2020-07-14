#!/usr/bin/python

import json

g = json.load(open('par_props.json.0', 'r'))

with open('final_charges_extract.xyz','w') as f:

  for i in range(len(g)):
 
    f.write('%-6s  %6s\n' % ('ID=',str(i)+".0"))

    for j in range(len(g[str(i)+".0"]["bader_charges"])):
  
      f.write('%16.8f\n' % (g[str(i)+".0"]["bader_charges"][j]) )

