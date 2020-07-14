# Scripts
Useful scripts that can be used for various computational software

## VASP

* **DOS_extractor.py**: Extract DOS and PDOS from xml file of **VASP** after performing DOS calculations. All Information about how to use it can be found inside the file.

* **dist.sh**: Calculate the distance between two images of NEB using dist.pl script found in **VASP-VTST**.

* **bader.sh**: Extracts the bader charges after performing bader charge analysis using **VASP**.

* **workfunction**: Extracts the information needed to plot a 1D planar averaged electrostatic potential from a 3D potential grid that can be used to compute workfunction.

## PGOPT

* **extract-bader.sh**: Extracts bader charges after performing bader charge analysis using **PGOPT**.

* **extract-displacement.sh**: Extracts displacements after performing frequency calculations using **PGOPT**.

* **extract-energy.sh**: Extracts energy after performing single point calculations using **PGOPT**.

* **extract-freq.sh**: Extracts frequencies after performing frequency calculations using **PGOPT**.

* **md-oszi.sh**: Extracts **OSZICAR** (to get the information about temperature) after performing MD calculations using **PGOPT**.

## HPC

* Submission scripts for **VASP**, **FDMNES**, and **MOLPRO** on super computers (HPC).

## PYTHON

* **sort-atoms-by-z.py**: It sorts all atoms in the system based on their z coordinate. 

* **md-analysis.py**: Calculates the evolution of bond distance and angle of interest for an MD trajcetory.

* **boltzmann.py**: Calculates the Boltzmann distribution in an ensemble of clusters. 

