#!/usr/bin/bash

VASPHOME=/u/home/h/hczhai/project-cnsi/program/VASP-VTST-SOL/vtstscripts-927

echo 'POSCARs' >> ../distance.txt
for i in 01 02 03 04 05 06;do
    $VASPHOME/dist.pl 00/POSCAR $i/POSCAR >> ../distance.txt 
done

echo 'CONTCARs' >> ../distance.txt
for i in 01 02 03 04 05;do
    $VASPHOME/dist.pl 00/POSCAR $i/CONTCAR >> ../distance.txt 
done
