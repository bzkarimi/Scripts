#!/bin/bash

#PBS -A AFOSR35083MAV
#PBS -l select=5:ncpus=32:mpiprocs=32
#PBS -l walltime=16:00:00
#PBS -q standard
#PBS -N NEB-A
#PBS -j oe

PBS_O_WORKDIR=/u/ana/borna/neb/c2h4-pt4-A-1
export JOBID=`echo ${PBS_JOBID} | cut -f1 -d'.'`
cd $PBS_O_WORKDIR
source ~/.bashrc

. $MODULESHOME/init/bash


module swap PrgEnv-pgi PrgEnv-intel/5.2.82
module swap intel intel/14.0.2.144

date
x=`date "+%s"`

aprun -n 160 $VASPHOME/vasp_std > OUT

date

y=`date "+%s"`
echo "TOTAL TIME IN SECONDS: "`expr $y - $x`

