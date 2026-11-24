#!/bin/bash
# =============================================================================
#  compile_lammps.sh
#  One-shot build of LAMMPS from source with the packages we use for
#  mechanics / deformation of coarse-grained polymer systems.
#
#  Why compile at all? The cluster module gives you a *generic* LAMMPS. When you
#  need a specific version, a package that isn't in the module, or (later) a
#  specialized add-on such as a machine-learned potential, you build your own.
#  This script is a clean, repeatable starting point — read it top to bottom
#  before running it.
#
#  Usage:   bash compile_lammps.sh
#  Result:  a binary called `lmp` inside ./lammps-*/build/
#
#  NOTE: On Quest, run this on a compute node, not the login node:
#        srun -A pXXXXX -p short -N 1 -n 8 -t 1:00:00 --pty bash
#        then: bash compile_lammps.sh
# =============================================================================
set -euo pipefail   # stop immediately if any command fails (fail loud, not silent)

# ---- 0. Environment ---------------------------------------------------------
module purge
module load cmake
module load mpi          # or gcc/openmpi — check `module spider` for the pairing on your cluster
NPROC=8                  # how many cores to compile with

# ---- 1. Download a stable release -------------------------------------------
VERSION="stable_29Aug2024_update1"
mkdir -p lammps-src && cd lammps-src
if [ ! -d "lammps-${VERSION}" ]; then
    wget -q "https://github.com/lammps/lammps/archive/${VERSION}.tar.gz"
    tar xf "${VERSION}.tar.gz"
fi
cd "lammps-${VERSION}"
mkdir -p build && cd build

# ---- 2. Configure the build with CMake --------------------------------------
# Each -D PKG_* turns on a package. These are the ones you need for CG polymer
# mechanics; add more as your projects grow (see the LAMMPS package list).
#   MOLECULE       bonds, angles, dihedrals -- i.e. polymers themselves
#   EXTRA-MOLECULE extra bonded potentials (e.g. FENE variants)
#   MANYBODY       many-body potentials
#   EXTRA-PAIR     extra pair (non-bonded) styles
#   EXTRA-FIX      extra fixes (thermostats, deformation helpers)
#   RIGID          rigid bodies (e.g. nanoparticle cores in PGN models)
#   MC             Monte Carlo moves (e.g. bond swapping for dynamic networks)
#   MISC, REPLICA  assorted useful extras
# (Keep every backslash below as the LAST character on its line -- no trailing comments!)
cmake ../cmake \
    -D CMAKE_BUILD_TYPE=Release \
    -D BUILD_MPI=yes \
    -D PKG_MOLECULE=yes \
    -D PKG_EXTRA-MOLECULE=yes \
    -D PKG_MANYBODY=yes \
    -D PKG_EXTRA-PAIR=yes \
    -D PKG_EXTRA-FIX=yes \
    -D PKG_RIGID=yes \
    -D PKG_MC=yes \
    -D PKG_MISC=yes \
    -D PKG_REPLICA=yes

# ---- 3. Compile -------------------------------------------------------------
make -j "${NPROC}"

# ---- 4. Sanity check --------------------------------------------------------
echo ""
echo "Build finished. Your binary is:"
echo "  $(pwd)/lmp"
echo ""
echo "Test it:"
echo "  ./lmp -h | head          # prints help + the list of compiled packages"
echo ""
echo "Add it to your PATH so you can call it anywhere by typing 'lmp':"
echo "  echo 'export PATH=$(pwd):\$PATH' >> ~/.bashrc && source ~/.bashrc"
