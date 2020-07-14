#!/usr/bin/bash

import json

num_structs = 26
g = json.load(open('./master/1.0/par_props.json.1', 'r'))
print (g["0.0"]["freqs"])

with open('final_freq','w') as f:
    for i in range(num_structs + 1):
        f.write('%-6s  %6s\n' % ('ID=',str(i)+".0"))
        for j in range(len(g[str(i)+".0"]["freqs"])):
            f.write('%16.8f\n' %  (g[str(i)+".0"]["freqs"][j]))
            if (g[str(i)+".0"]["freqs"][j] < 0):
                print ("TS found! ID=",str(i)+".0")
