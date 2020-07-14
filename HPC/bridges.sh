#!/bin/bash

#SBATCH -N 2
#SBATCH -p RM
#SBATCH -t 24:00:00
#SBATCH --ntasks-per-node 28

export JOBID=`echo ${SLURM_JOB_ID} | cut -f1 -d'.'`
source ~/.bashrc
cd $WORKDIR
mpirun -n 56 $VASPHOME/vasp_std > OUT.$JOBID

