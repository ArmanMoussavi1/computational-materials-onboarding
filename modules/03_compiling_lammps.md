# Module 3 — Compiling LAMMPS

> **Why this matters for us.** LAMMPS is the molecular dynamics engine at the
> center of the lab — it's how we push, pull, and break virtual materials to see
> how they respond. The cluster's pre-installed LAMMPS is fine to start, but the
> moment you need a specific version, a special feature, or a machine-learned
> potential, you'll build your own. Doing that once, cleanly, demystifies the whole
> thing.

---

## What is LAMMPS, really?

**LAMMPS** (Large-scale Atomic/Molecular Massively Parallel Simulator) is a program
that answers one question over and over, billions of times: *given where all the
atoms are right now and the forces between them, where will they be a tiny moment
later?* Repeat that step millions of times and you get a movie of how a material
moves, flows, stretches, and fractures.

It's free, open-source, runs beautifully in parallel across cluster nodes, and is
the standard tool in our field. You'll write **input scripts** (plain text files
of commands) that tell it what to simulate — that's Module 4.

---

## "Compiling" in one paragraph

LAMMPS ships as human-readable source code. **Compiling** is translating that
source into a fast executable your specific machine can run — and, crucially,
choosing which optional **packages** to bake in. Think of it like assembling a
custom toolkit: the base is always there, but you decide whether to include the
Monte-Carlo drawer, the rigid-body drawer, the machine-learning drawer, and so on.

You don't compile every day. You compile once per project setup, then reuse the
binary for months.

---

## The fastest path: use the module (start here)

Before building anything, check whether the cluster already has what you need:

```bash
module spider lammps
module load lammps
lmp -h | head -40          # prints the version + which packages are compiled in
```

If the listed packages cover your needs (for basic mechanics they often do), you're
done — skip to Module 4. Come back here when you hit a wall.

---

## Building your own with CMake

When you *do* need a custom build, we use **CMake** (the modern LAMMPS build
system). The full, commented recipe is in
[`scripts/compile_lammps.sh`](../scripts/compile_lammps.sh) — read it top to bottom;
it's designed to be understood, not just run. The shape of it:

```bash
# 1. get a stable release
wget https://github.com/lammps/lammps/archive/stable_29Aug2024_update1.tar.gz
tar xf stable_29Aug2024_update1.tar.gz
cd lammps-stable_29Aug2024_update1
mkdir build && cd build

# 2. configure: choose packages with -D PKG_* flags
cmake ../cmake -D BUILD_MPI=yes -D PKG_MOLECULE=yes -D PKG_EXTRA-FIX=yes ...

# 3. compile (in parallel; grab a compute node first!)
make -j 8
```

The packages that matter most for **CG polymer mechanics**:

| Package | Gives you |
|---|---|
| `MOLECULE` | bonds, angles, dihedrals — i.e. polymers themselves |
| `EXTRA-MOLECULE` | extra bonded styles like FENE variants |
| `EXTRA-FIX` | extra "fixes" — thermostats, deformation controls |
| `EXTRA-PAIR` | extra pair (non-bonded) interaction styles |
| `RIGID` | rigid bodies, e.g. nanoparticle cores in PGN models |
| `MC` | Monte-Carlo moves like bond swapping (dynamic networks) |
| `MANYBODY` | many-body potentials |

> ⚠️ **Compile on a compute node, not the login node.** Building LAMMPS pins several
> cores for a few minutes. Grab an interactive node first (Module 2):
> ```bash
> srun -A pXXXXX -p short -N 1 -n 8 -t 1:00:00 --pty bash   # pXXXXX = your allocation ID
> bash compile_lammps.sh
> ```

When it finishes you'll have a binary called `lmp` inside `build/`. Test it:

```bash
./lmp -h | head           # should list your chosen packages
```

Add its folder to your `PATH` (Module 1) so you can call `lmp` from anywhere.

---

## One step further (for later)

LAMMPS can also run with a **machine-learned interatomic potential** — a neural
network trained to reproduce the physics, compiled in so simulations can call it.
That's a natural meeting point of the two halves of our work (physics-grounded ML as
a *tool*), but it needs a few extra build steps and isn't a day-one concern. When a
project takes you there, ask — there are worked, end-to-end examples to follow.

---

## 🤖 Use your AI assistant here

Compilation errors are dense walls of C++ and CMake complaints — a perfect job for
an assistant, and a safe one (you're debugging *your own* build, not asking it to
invent physics):

> "My LAMMPS CMake build failed with this output: [paste the last ~40 lines].
> What's the root cause, and what's the minimal change to fix it? Explain what that
> flag or missing dependency actually does."

Then re-run the build to confirm. If it works, you learned something; if it doesn't,
you have a sharper question to bring to `quest-help` or a labmate.

---

## ✅ Checkpoint

You're ready to move on when you can:
1. explain, to a friend outside the field, what compiling is and why we choose packages;
2. either load the LAMMPS module *or* build `lmp` yourself and run `lmp -h`;
3. name one package we need for polymers and say what it adds.

**Next:** [Module 4 — Running MD & Deforming Materials →](04_md_and_deformation.md)
