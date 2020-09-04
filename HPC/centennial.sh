#!/bin/bash

#PBS -A AFOSR35083MAV
#PBS -l select=2:ncpus=40:mpiprocs=40
#PBS -l walltime=24:00:00
#PBS -q standard
#PBS -N cu-tio2
#PBS -j oe

PBS_O_WORKDIR=/p/home/ana/borna/tio2/model/opt/new-model
export JOBID=`echo ${PBS_JOBID} | cut -f1 -d'.'`
cd $PBS_O_WORKDIR
source ~/.bashrc

. $MODULESHOME/init/bash 2> /dev/null
module unload compiler/intel
module unload mpi/sgimpt
module load compiler/intel/16.0.4.258
module load mpi/intelmpi/2017.1.132

date
x=`date "+%s"`

mpirun -n 80 $VASPHOME/vasp_std > OUT

date

y=`date "+%s"`
echo "TOTAL TIME IN SECONDS: "`expr $y - $x`

