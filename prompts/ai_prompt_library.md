# The Lab's AI Prompt Library

Copy-pasteable prompts for the tasks that come up daily, organized to match the
tutorial. Every one is written to make the assistant **teach and scaffold**, not to
hand you an answer you don't understand. Read [Module 7](../modules/07_ai_assistants.md)
first — these prompts assume that mindset.

Replace anything in `[brackets]` with your own context. The more context you give
(actual error text, actual code, what you've already tried), the better the help.

---

## 🐚 Terminal & bash

**Understand a command instead of memorizing it:**
> Explain this shell command piece by piece: `[paste command]`. Then give me two
> safe variations and explain the underlying pattern so I can build my own next time.

**Turn a repetitive task into a loop:**
> I keep doing `[describe the manual task]` by hand for many files. Show me a bash
> loop that automates it, explain each part, and point out anything that could go
> wrong (especially anything destructive).

---

## 🖥️ Cluster & SLURM

**Decode a job failure (my morning ritual):**
> Here is my SLURM submission script and the error it produced:
> ```
> [paste the #SBATCH script]
> [paste the error / slurm.*.err contents]
> ```
> What is the root cause, and what is the minimal fix? Explain *why*, so I can
> recognize this class of error myself next time.

**Set up a parameter sweep:**
> I want to run the same LAMMPS simulation across `[parameter]` = `[list of values]`,
> one job per value, on Quest (use your allocation ID for --account, short partition). Draft a SLURM job
> array script. Comment every `#SBATCH` line. I'll read it fully before submitting.

**Right-size a job:**
> My last job used `[X]` cores for `[Y]` and took `[Z]`. Here's the `sacct` output:
> `[paste]`. Am I over- or under-requesting resources? What would you change and why?

---

## ⚙️ LAMMPS & MD

**Explain a script I inherited:**
> Walk me through this LAMMPS input script line by line, in plain language. Flag
> anything that looks unusual or version-specific so I can verify it against the
> LAMMPS docs:
> ```
> [paste in.script]
> ```

**Scaffold a new simulation (then verify):**
> Sketch a LAMMPS input that `[e.g. equilibrates a bead-spring melt in NPT, then
> applies uniaxial tension in x while y and z relax to zero pressure]`. Use LJ units
> and Kremer-Grest FENE bonds. Comment every line. I will check each command against
> the official LAMMPS documentation before running — call out any you're unsure about.

**Debug unphysical results:**
> My deformation run gives `[describe: e.g. negative modulus / stress that never
> rises / immediate fracture]`. Here's my input script and a plot of the output.
> List the most likely physical or setup causes, and a quick check for each.

---

## 📊 Analysis & plotting

**Sanity-check my own analysis:**
> Here's my stress-strain analysis script and the resulting plot. Does my
> Young's-modulus fit look like it's using a sensible strain range? Suggest a
> diagnostic *I can run myself* to confirm the elastic region is truly linear.

**Draft a clean figure:**
> Write a matplotlib script that plots `[X vs Y]` from this data format `[describe
> columns]`, with error bars from `[N]` runs, publication-quality styling, and clear
> axis labels with units. Explain any styling choices.

**Explain a method before I trust it:**
> Explain `[statistical method / numerical technique]` at the level of a first-year
> grad student, why it's appropriate for `[my situation]`, and one assumption it makes
> that could bite me.

---

## 🤖 Machine learning

**Understand a model component:**
> In this GNN code, explain what `[e.g. global_mean_pool / message passing / the
> pooling step]` does and why it's necessary to go from per-node features to one
> prediction per graph: `[paste code]`.

**Diagnose training:**
> My training loss isn't decreasing. Here's my model, training loop, and loss curve.
> List the three most likely causes and a quick diagnostic for each. Don't just give
> me a fix — help me find *which* problem I have.

**Guard against fooling myself:**
> My model reports low error on the test set. What are the ways this could be
> misleading (leakage, artifact-learning, distribution shift)? Give me concrete
> checks to run to make sure it learned physics and not a shortcut.

---

## 💡 Brainstorming & thinking

**Steelman the opposite view:**
> Here's my research question and the approach I'm taking: `[describe]`. Argue the
> strongest possible case *against* this approach. What am I not seeing?

**Map the landscape:**
> I'm studying `[topic]`. List the main approaches people use, with one strength and
> one weakness each, and note which are considered current vs. dated. I'll verify the
> key claims against real papers.

**Rubber-duck a stuck problem:**
> I'm stuck on `[problem]`. Here's what I've tried and what happened. Ask me clarifying
> questions until we've narrowed down where the issue likely is — don't jump to a
> solution.

---

## 🧹 Code hygiene

**Refactor without breaking:**
> Refactor this script for readability without changing its behavior. Explain each
> change. Keep it runnable at every step: `[paste code]`.

**Document for future-me and labmates:**
> Add clear comments and a short docstring to this script explaining what it does,
> its inputs/outputs, and how to run it. Don't change the logic: `[paste code]`.

---

## The verification habit (tape this to your monitor)

Before you accept anything an assistant gives you:

1. **Do I understand it?** If not, ask it to teach me until I do.
2. **Did I run it on something I can check?** A tiny case with a known answer.
3. **Did I verify against ground truth?** Docs, theory, MD, a real paper.
4. **Is it mine now?** Could I have written it, and can I defend it?

If any answer is "no," you're not done yet.
