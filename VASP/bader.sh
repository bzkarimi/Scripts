#!/usr/bin/bash

VASPHOME=~/hczhai/program/VASP-CUDA/vtstscripts-927
BADERHOME=~/hczhai/program/VASP-CUDA/bader

$VASPHOME/chgsum.pl AECCAR0 AECCAR2
$BADERHOME/bader -vac off CHGCAR -ref CHGCAR_sum
mv ACF.dat bader-charges.dat
