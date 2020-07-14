#!/bin/bash

#PBS -A AFOSR35083MAV
#PBS -l select=1:ncpus=40:mpiprocs=40
#PBS -q standard
#PBS -l walltime=24:00:00
#PBS -N ceo2
#PBS -j oe

PBS_O_WORKDIR=/p/home/ana/borna/ceo2/100

source ~/.bashrc

WTJ=$WORKDIR/wfu
DTJ=$WORKDIR/scratch

mkdir -p $WTJ $DTJ
cd $PBS_O_WORKDIR

$MOLPROHOME/molpro -W $WTJ -d $DTJ -o ceo2.out ceo2.com

