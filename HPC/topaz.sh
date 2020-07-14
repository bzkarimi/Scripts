#!/bin/bash

#PBS -A AFOSR35083MAV
#PBS -l select=4:ncpus=36:mpiprocs=36
#PBS -l walltime=08:00:00
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

module unload compiler/intel
module unload mpi/sgimpt
module load compiler/intel/16.0.0
module load mpi/intelmpi/16.0.0


date
x=`date "+%s"`

mpirun -n 144 $VASPHOME/vasp_std > OUT

date

y=`date "+%s"`
echo "TOTAL TIME IN SECONDS: "`expr $y - $x`

