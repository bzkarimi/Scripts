#!/usr/bin/env python

import numpy as np

unitcelly = 13.113524


def distance(x1, y1, z1, x2, y2, z2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    dz = abs(z1 - z2)
    if ( dy > unitcelly/2 ):
        r = (dx**2.0 + (dy - unitcelly)**2.0 + dz**2.0)**(0.5)
    else:
        r = (dx**2.0 + dy**2.0 + dz**2.0)**(0.5)
    return r

def angle(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    dy1 = y1 - y2
    dy2 = y3 - y2
    if ( abs(dy1) > unitcelly/2 ):
        dy1 = y1 - y2 - unitcelly
        if ( abs(dy1) > unitcelly/2 ):
            dy1 = unitcelly + (y1 - y2)
    if ( abs(dy2) > unitcelly/2 ):
        dy2 = y3 - y2 - unitcelly
        if ( abs(dy2) > unitcelly/2 ):
            dy2 = unitcelly + (y3 - y2)

    r21 = [x1-x2, dy1, z1-z2]
    r23 = [x3-x2, dy2, z3-z2]
    theta = np.degrees (np.arccos( (r21[0]*r23[0]+ r21[1]*r23[1] + r21[2]*r23[2])/
                     ( (r21[0]**2+r21[1]**2+r21[2]**2)**0.5 *  (r23[0]**2+r23[1]**2+r23[2]**2)**0.5) ) )
    return theta

#H190 H191 C188 Pt185
#H192 H193 C189 pt187
pt1 = 1
c1  = 2
c2  = 3
h1  = 4
h2  = 5
h3  = 6
h4  = 7
ln  = 90000
ln1 = 8
xyz = []
C1Pt1_all = []
C2Pt1_all = []
C1C2_all  = []
d1 = []
d2 = []
d3 = []

Pt1C1C2_all = []
H1C1C2_all  = []
a1 = []
a2 = []

d_c1pt1 = True
d_c2pt1 = True
d_c1c2  = True

a_pt1c1c2 = True
a_h1c1c2  = True

with open('coord.xyz', 'r') as f1:
    data = f1.readlines()
    for line in data:
        if ( len(line.split()) != 1):
            xyz.append([ str(line.split()[0]),
                         float(line.split()[1]),
                         float(line.split()[2]),
                         float(line.split()[3]) ]) 
        else:
            xyz.append([int(line.split()[0])])
for i in range(10000):
    if (d_c1pt1 == True):
        with open('c1pt1', 'a') as f2:
            R = distance(xyz[pt1 + ln1*i ][1],xyz[pt1 + ln1*i ][2],xyz[pt1 + ln1*i ][3],
                         xyz[c1 + ln1*i ][1],xyz[c1 + ln1*i ][2],xyz[c1 + ln1*i ][3])
            d1.append(R)
            C1Pt1_all.append([i, R])
            f2.write('%5i %16.8f\n' % (i, R))
    if(d_c2pt1 == True):
        with open('c2pt2', 'a') as f3:
            R = distance(xyz[pt1 + ln1*i ][1],xyz[pt1 + ln1*i ][2],xyz[pt1 + ln1*i ][3],
                         xyz[c2 + ln1*i ][1],xyz[c2 + ln1*i ][2],xyz[c2 + ln1*i ][3])
            d2.append(R)
            C2Pt1_all.append([i, R])
            f3.write('%5i %16.8f\n' % (i, R))
            if (i == 5095):
                print (xyz[pt1 + ln1*i][1],xyz[pt1 + ln1*i][2],xyz[pt1 + ln1*i][3])
    if(d_c1c2 == True):
        with open('c1c2', 'a') as f4:
            R = distance(xyz[c1 + ln1*i ][1],xyz[c1 + ln1*i ][2],xyz[c1 + ln1*i ][3],
                         xyz[c2 + ln1*i ][1],xyz[c2 + ln1*i ][2],xyz[c2 + ln1*i ][3])
            d3.append(R)
            C1C2_all.append([i, R])
            f4.write('%5i %16.8f\n' % (i, R))
    if(a_pt1c1c2 == True):
        with open('pt1c1c2', 'a') as f5:
            a = angle(xyz[pt1 + ln1*i ][1],xyz[pt1 + ln1*i ][2],xyz[pt1 + ln1*i ][3],
                      xyz[c1 + ln1*i ][1],xyz[c1 + ln1*i ][2],xyz[c1 + ln1*i ][3],
                      xyz[c2 + ln1*i ][1],xyz[c2 + ln1*i ][2],xyz[c2 + ln1*i ][3])
            a1.append(a)
            Pt1C1C2_all.append([i, a])
            f5.write('%5i %16.8f\n' % (i, a))
    if(a_h1c1c2 == True):
        with open('h1c1c2', 'a') as f6:
            a = angle(xyz[h1 + ln1*i ][1],xyz[h1 + ln1*i ][2],xyz[h1 + ln1*i ][3],
                      xyz[c1 + ln1*i ][1],xyz[c1 + ln1*i ][2],xyz[c1 + ln1*i ][3],
                      xyz[c2 + ln1*i ][1],xyz[c2 + ln1*i ][2],xyz[c2 + ln1*i ][3])
            a2.append(a)
            H1C1C2_all.append([i, a])
            f6.write('%5i %16.8f\n' % (i, a))



if (d_c1pt1 == True):
    C1Pt1_all.sort(key=lambda x: x[1])
    print('min C1-Pt1 distance =',C1Pt1_all[0])
    print('max C1-Pt1 distance =',C1Pt1_all[-1])
    print('avg C1-Pt1 distance =',sum(d1)/len(d1))
if(d_c2pt1 == True): 
    C2Pt1_all.sort(key=lambda x: x[1])
    print('min C2-Pt2 distance =',C2Pt1_all[0])
    print('max C2-Pt2 distance =',C2Pt1_all[-1])
    print('avg C2-Pt2 distance =',sum(d2)/len(d2))
if(d_c1c2 == True):
    C1C2_all.sort(key=lambda x: x[1])
    print('min C1-C2 distance =',C1C2_all[0])
    print('max C1-C2 distance =',C1C2_all[-1])
    print('avg C1-C2 distance =',sum(d3)/len(d3))
if(a_pt1c1c2 == True):
    Pt1C1C2_all.sort(key=lambda x: x[1])
    print('min Pt1-C1-C2 angle =',Pt1C1C2_all[0])
    print('max Pt1-C1-C2 angle =',Pt1C1C2_all[-1])
    print('avg Pt1-C1-C2 angle =',sum(a1)/len(a1))
if(a_h1c1c2 == True):
    H1C1C2_all.sort(key=lambda x: x[1])
    print('min H1-C1-C2 angle =',H1C1C2_all[0])
    print('max H1-C1-C2 angle =',H1C1C2_all[-1])
    print('avg H1-C1-C2 angle =',sum(a2)/len(a2))
