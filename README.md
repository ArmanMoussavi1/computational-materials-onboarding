# Computational Materials — Research Onboarding

**Welcome!** This tutorial takes you from an empty terminal to running molecular
dynamics simulations, extracting mechanical properties, and touching the
machine-learning tools we use to connect a material's structure to how it behaves.

It's built for **everyone**: if you've never opened a terminal — several of us
hadn't when we started — begin at the top and walk through in order; it assumes no
prior experience and builds from nothing. If you're a seasoned MD user, skim to the
parts that are new (there's a fast track below). Either way, by the end of ~two weeks
you'll be set up to do real research.

---

## The idea that organizes everything

![Processing → structure → property, with design tracing the chain backward](assets/01_research_vision.svg)

Nearly all of what we do follows **a chain of three links**:

> **Processing conditions set the structure. The structure sets the mechanical
> response. And a desired response must trace back to the conditions that produce it.**

Read that chain **left to right and you're doing discovery**; read it **right to left
and you're doing design**. This tutorial gives you the tools for both directions:

1. **How structure forms.** Processing conditions — concentration, temperature,
   kinetics — drive **self-assembly and phase separation** into a microstructure: a
   particular network, its crosslinks, its entanglements. *How does order emerge?*
2. **How structure sets mechanics.** That topology decides whether the material is
   stiff, tough, or brittle. **Molecular dynamics** measures it directly, and
   **machine learning** (our GNN surrogate, **TANGO**) learns the map from wiring to
   response — fast enough to explore structures simulation alone could never reach.
3. **How to design.** Once you can predict response from structure, you can run the
   chain *backwards*: start from a target property and use **theory and inverse
   design** to ask what structure — and what processing — would produce it.

*At bottom this is an engineer's way of seeing a material — structure, load, response,
and design — the same logic a civil engineer brings to a bridge, carried down to the
scale of a molecule.*

The long horizon this points at: materials that don't just *have* good properties but
actively **manage their own behavior** — sensing, adapting, healing. Every skill here
is a rung on that ladder. You'll build the ladder from the bottom.

> **A note on ML.** Throughout, machine learning is treated as *instrumentation* — a
> fast, flexible tool for answering physical questions — never as a replacement for
> the physics or a stand-in scientist. That framing is deliberate, and Module 7 makes
> it concrete.

---

## The learning path

Work through the modules in order (or jump around if you know the material). Each ends
with a checkpoint so you know you're ready for the next.

| # | Module | You'll learn to… | New to computing? | Seasoned MD user? |
|---|---|---|---|---|
| 0 | [Set Up Your Workstation](modules/00_setup.md) | get VS Code + the toolkit running as your hub | **start here** | skim the toolkit table |
| 1 | [Files & the Terminal](modules/01_terminal.md) | navigate in VS Code, then find, edit & automate with bash | **essential** | skim |
| 2 | [The Cluster: Quest & SLURM](modules/02_hpc_quest.md) | run heavy work on Northwestern's HPC | **essential** | check the Quest specifics |
| 3 | [Compiling LAMMPS](modules/03_compiling_lammps.md) | build the MD engine from source | recommended | skim |
| 4 | [MD & Deforming Materials](modules/04_md_and_deformation.md) | simulate + deform (tensile/shear/etc.) | **core** | jump to Part D (deformation) |
| 5 | [Mechanical Properties](modules/05_mechanical_properties.md) | extract modulus, strength, toughness | **core** | skim; grab the analysis script |
| 6 | [AI for Materials](modules/06_ai_for_materials.md) | surrogates & GNNs, TANGO-style, from scratch | **core** | **start here** |
| 7 | [AI Assistants, Responsibly](modules/07_ai_assistants.md) | use Claude Code & LLMs with rigor and ethics | **everyone** | **everyone** |

### 📅 A suggested 1–2 week pace

The goal is to get you doing real work fast. Adjust to your background — an
experienced MD user might compress Week 1 into a day.

**Week 1 — get simulating.**
- **Day 1:** Module 0 (set up VS Code + toolkit) and Module 1 (terminal); request your
  accounts so access is ready when you need it.
- **Day 2:** Module 2 (Quest & SLURM) — log in, move files, submit a hello-world job.
- **Day 3:** Module 3 (compile LAMMPS) — get a working `lmp` binary.
- **Days 4–5:** Module 4 (MD & deformation) — run the bead-spring melt, then deform it.
  Take this one in two sittings; it's the heart of the week.

**Week 2 — measure, model, and work like a researcher.**
- **Day 6:** Module 5 (mechanical properties) — turn a curve into modulus, strength,
  toughness on your own data.
- **Days 7–8:** Module 6 (AI for materials) — run `tiny_surrogate.py` and `tiny_gnn.py`;
  understand the surrogate → graph → TANGO progression.
- **Day 9:** Module 7 (AI assistants) + skim the [prompt library](prompts/ai_prompt_library.md).
- **Day 10:** A first tiny independent project — pick one material knob (e.g. crosslink
  density), sweep it, and plot a property vs. that knob. That single plot is a real
  structure→property result, and you made it.

### ⚡ Fast track for experienced MD users
Skim **Module 2** for the Quest account/storage conventions, grab
[`scripts/deform.in`](scripts/deform.in) and
[`scripts/stress_strain.py`](scripts/stress_strain.py) from **Modules 4–5**, and spend
your real time in **Module 6** (the ML core and research vision) and **Module 7** (how
we use AI tools).

---

## What's in this repo

```
computational-materials-onboarding/
├── README.md                     ← you are here
├── modules/                      ← the lessons, in order
│   ├── 00_setup.md
│   ├── 01_terminal.md
│   ├── 02_hpc_quest.md
│   ├── 03_compiling_lammps.md
│   ├── 04_md_and_deformation.md
│   ├── 05_mechanical_properties.md
│   ├── 06_ai_for_materials.md
│   └── 07_ai_assistants.md
├── scripts/                      ← working, commented starter code
│   ├── slurm_lammps_template.sh  ← SLURM job template for LAMMPS on Quest
│   ├── compile_lammps.sh         ← build LAMMPS from source (CMake)
│   ├── deform.in                 ← LAMMPS: all 4 deformation modes, one switch
│   ├── stress_strain.py          ← extract mechanical properties + plot
│   ├── tiny_surrogate.py         ← "AI for materials" in one screen (a surrogate)
│   └── tiny_gnn.py               ← TANGO in miniature (a graph neural network)
├── prompts/
│   └── ai_prompt_library.md      ← copy-pasteable prompts for daily work
└── assets/                       ← schematics (SVG); swap in your own snapshots
```

The scripts are meant to be **read, run, broken, and rebuilt** — they're teaching
tools, not black boxes.

---

## Before you start: accounts & software

**Software:** all of it — VS Code (your hub), WSL, Git, OVITO, conda, and the
file-transfer tools — is installed in **[Module 0](modules/00_setup.md)**, which also
explains what each one is for. Start there.

**Accounts to request early** (they can take a day or two to activate, so line them up
now; ask a labmate or your group's manager if stuck):

- [ ] **Northwestern NetID** and **Duo** set up.
- [ ] **Quest access** — request through Northwestern Research Computing. Everyone gets
      a **home directory** to start in (enough for this whole tutorial). For research
      space and compute, **apply for a research allocation** — that gives you a project
      directory and an allocation ID for your jobs. Docs: rcdsdocs.it.northwestern.edu ·
      help: quest-help@northwestern.edu.
- [ ] **A GitHub account** — how we share code (including this repo).

---

## Reference code worth bookmarking

The tutorial points to these public repositories as real, working examples:

- [**build_polymer_systems**](https://github.com/ArmanMoussavi1/build_polymer_systems) — build coarse-grained polymer models → LAMMPS data files
- [**KG_PGNs**](https://github.com/keten-group/KG_PGNs) — polymer-grafted nanoparticle mechanical models (a published shear-response study)
- [**Interatomic_Potential_Functions**](https://github.com/ArmanMoussavi1/Interatomic_Potential_Functions) — build intuition for the potentials behind MD
- [**polymer_entanglement_analysis**](https://github.com/ArmanMoussavi1/polymer_entanglement_analysis) — measure network topology (Z1+)
- [**general_helpful_coding**](https://github.com/ArmanMoussavi1/general_helpful_coding) — handy snippets worth having around

(There are more specialized repositories — e.g. machine-learned interatomic potentials
— that you'll be pointed to individually once a project calls for them.)

---

## A word on AI tools

We use AI coding assistants (Claude Code, and chat assistants) every day, and this
tutorial teaches you to use them **well** — as fast, fallible collaborators that
accelerate your work, never as authorities you outsource your thinking to. You'll see
🤖 boxes throughout, and there's a full [prompt library](prompts/ai_prompt_library.md)
and a dedicated [Module 7](modules/07_ai_assistants.md). The guiding line:

> You are the accountable scientist. Use these tools to *understand faster* — never to
> *avoid understanding*.

---

## Getting unstuck

Everyone hits walls — that's the job. In order: re-read the relevant module, check the
official docs (LAMMPS, Quest), ask an AI assistant to *explain* (not just fix), search
the error, ask a labmate, and bring good questions to group meeting. A well-formed
question — what you tried, what happened, what you expected — is itself a research
skill.

**Welcome aboard. Let's build something that matters.**

---

## License

Released under the [MIT License](LICENSE) — free to use, adapt, and share, with
attribution. © 2026 Arman Moussavi.
