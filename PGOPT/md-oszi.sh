#!/bin/bash

mkdir OSZI
cd OSZI
RM=`pgopt show`
for i in `ls $RM/restarts/1.0/restart*`; do
    echo $i
    IP=${i#$RM/restarts/1.0/}
    tar xvf $i '*.chk/OSZI*'
    mv *.chk OSZI-$IP
    NN=`ls OSZI-$IP | wc -l`
    NNG=`expr $NN - 1`
    mv OSZI-$IP/OSZICAR OSZI-$IP/OSZICAR.$NNG
done

