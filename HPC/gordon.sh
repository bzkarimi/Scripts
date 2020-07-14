#!/bin/bash

#PBS -A AFOSR35083MAV
#PBS -l select=2:ncpus=32:mpiprocs=32
#PBS -l walltime=24:00:00
#PBS -q standard
#PBS -N pt2sn4-al2o3 
#PBS -j oe
#PBS -M bzkarimi@g.ucla.edu
#PBS -m be

PBS_O_WORKDIR=/p/home/ana/borna/test
export JOBID=`echo ${PBS_JOBID} | cut -f1 -d'.'`
cd $PBS_O_WORKDIR
source ~/.bashrc

. $MODULESHOME/init/bash

LDBAK=$LD_LIBRARY_PATH
LD_LIBRARY_PATH=
module swap PrgEnv-cray PrgEnv-intel/5.2.40
module swap intel intel/16.0.2.181
LD_LIBRARY_PATH=$LDBAK


date
x=`date "+%s"`

aprun -n 64 $VASPHOME/vasp_std > OUT

date

y=`date "+%s"`
echo "TOTAL TIME IN SECONDS: "`expr $y - $x`

