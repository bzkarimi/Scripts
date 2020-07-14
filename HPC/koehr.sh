#!/bin/bash

#PBS -A AFOSR35083MAV
#PBS -l select=1:ncpus=48:mpiprocs=48
#PBS -l walltime=08:00:00
#PBS -q standard
#PBS -N pt2sn4-al2o3 
#PBS -j oe

PBS_O_WORKDIR=/p/home/ana/borna/test
export JOBID=`echo ${PBS_JOBID} | cut -f1 -d'.'`
cd $PBS_O_WORKDIR
source ~/.bashrc

. $MODULESHOME/init/bash 2> /dev/null

module unload compiler/intel
module unload mpt
module load compiler/intel/18.0.1.163
module load compiler/intelmpi/18.0.1.163


date
x=`date "+%s"`

mpirun -n 48 $VASPHOME/vasp_std > OUT

date

y=`date "+%s"`
echo "TOTAL TIME IN SECONDS: "`expr $y - $x`

