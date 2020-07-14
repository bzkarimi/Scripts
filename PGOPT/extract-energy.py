#!/usr/bin/python

import json

g = json.load(open('par_props.json.0', 'r'))

with open('final_E.xyz','w') as f:

  for i in range(len(g)):
 
    f.write('%-6s  %6s %16.8f\n' % ('ID=',str(i)+".0",g[str(i)+".0"]["energy"]))
