#!/bin/bash
# =============================================================================
#  slurm_lammps_template.sh
#  A starter SLURM job script for running LAMMPS on Northwestern's Quest.
#
#  Submit it with:      sbatch slurm_lammps_template.sh
#  Watch it with:       squeue -u $USER
#  Kill it with:        scancel <jobid>
#
#  Everything after "#SBATCH" is a request to the scheduler. Everything else
#  is a normal bash script that runs *on the compute node* once your job starts.
# =============================================================================

#SBATCH --account=pXXXXX            # <-- your research allocation ID (you get this when it is approved; see Module 2)
#SBATCH --partition=short           # short (<4h), normal (<48h), long (<7d). Match this to --time.
#SBATCH --nodes=1                   # how many machines
#SBATCH --ntasks-per-node=16        # how many MPI ranks (parallel processes) per machine
#SBATCH --time=01:00:00             # wall-clock limit HH:MM:SS. Job is killed when it runs out.
#SBATCH --mem=8G                    # memory per node
#SBATCH --job-name=deform_test      # shows up in squeue
#SBATCH --output=slurm.%j.out       # stdout  (%j = the job ID)
#SBATCH --error=slurm.%j.err        # stderr
#SBATCH --mail-type=END,FAIL        # email me when it finishes or dies
#SBATCH --mail-user=NETID@u.northwestern.edu

# ---- 1. Set up the software environment -------------------------------------
module purge                        # start from a clean slate every time (reproducibility!)
module load lammps                  # use `module spider lammps` to see exact versions available
# If you compiled your own LAMMPS, skip the module and point at your binary instead:
# LMP=$HOME/lammps-src/.../build/lmp

# ---- 2. Move to the folder the job was submitted from ------------------------
cd $SLURM_SUBMIT_DIR

# ---- 3. Run LAMMPS in parallel ----------------------------------------------
# $SLURM_NTASKS is filled in automatically from the #SBATCH lines above.
# -in : the input script.  -var : pass a variable into the script at launch.
srun lmp -in deform.in -var mode tensile -var erate 1.0e-4

# Tip: to sweep several deformation modes, submit this script several times,
# each with a different -var mode (tensile / compression / shear / dilation),
# or use a SLURM job array (see modules/02_hpc_quest.md).
