#!/bin/csh

#$ -pe shared 8
#$ -l h_data=4G,h_rt=16:00:00
#$ -N cu5o5-fdm
#$ -M bzkarimi@mail
#$ -cwd
#$ -m bea

set FDMNES_par=/u/home/b/bzkarimi/project-ana/fdmnes/parallel_fdmnes

HOST_NUM_FOR_MUMPS=4 $FDMNES_par/mpirun_fdmnes -np 8

wait 
exit
