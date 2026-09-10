# Module 7 — Using AI Assistants Responsibly

> **Why this matters for us.** AI coding assistants (Claude Code, and chat
> assistants like Claude and ChatGPT) are now part of a computational
> researcher's toolkit — I use them every day. Used well, they let you move faster,
> learn faster, and spend your energy on the science instead of on syntax. Used
> badly, they quietly erode the two things a scientist can't afford to lose:
> **understanding** and **integrity**. This module is about using them the first way.

---

## The one principle everything follows from

> **An AI assistant is a tireless, knowledgeable, occasionally-wrong collaborator —
> never an authority.** You remain the scientist. You are accountable for every line
> of code you run and every number you report, no matter who (or what) wrote it.

If you internalize only one thing from this tutorial, make it that. Everything below
is a consequence of it.

---

## What these tools are good at (use them here)

- **Explaining unfamiliar things.** A cryptic SLURM error, a dense LAMMPS command, a
  chunk of a labmate's code. Assistants are excellent tutors — *if you ask them to
  teach you, not just to hand you the answer.*
- **Scaffolding.** Turning "I want to plot toughness vs crosslink density with error
  bars" into a first-draft script you then read, test, and fix.
- **Debugging.** Paste the code and the error; ask for the root cause and *why*.
- **Refactoring and cleanup.** Making working-but-ugly code readable.
- **Brainstorming.** Pressure-testing a research idea, listing approaches you hadn't
  considered, playing devil's advocate.
- **Boilerplate.** Argument parsing, file I/O, plot styling — the stuff that's
  tedious but not intellectually load-bearing.

## What they're bad at (verify or avoid)

- **Being correct about specifics.** LAMMPS commands, library APIs, and numerical
  details are often subtly wrong, outdated, or version-mismatched — delivered with
  total confidence. *Always* check against official docs and, above all, against
  whether the code runs and gives sane results.
- **Physical judgment.** Whether a modulus is believable, whether a model learned
  physics or an artifact — this is *your* job and cannot be delegated.
- **Citations and facts.** Assistants invent plausible-sounding references. Never
  cite a paper an AI gave you without finding and reading the real thing.
- **Knowing your data.** They don't know your system unless you tell them, and they
  can't see whether your simulation actually converged.

The pattern: **great for accelerating things you could verify yourself; dangerous for
things you're taking on faith.**

---

## Meet Claude Code (the agentic assistant)

Beyond chat, **Claude Code** is an assistant that works directly in your terminal and
files — it can read your repo, run commands, edit scripts, and iterate. It's
genuinely useful for the setup-heavy parts of our work: wiring up a new analysis
pipeline, sweeping parameters, organizing a messy project folder, drafting a first
version of a plotting script against your actual data.

The same principle applies, only more so: because it can *act*, you must stay in the
loop. Read its diffs before accepting them. Run its code and check the output. Treat
it like a fast junior collaborator whose work you always review — never a black box
you rubber-stamp.

---

## A day in the life (how I actually use these)

To make it concrete, here's the rhythm — the full, copy-pasteable versions live in
[`prompts/ai_prompt_library.md`](../prompts/ai_prompt_library.md):

- **Morning, decoding an overnight job failure:** paste the SLURM error and script,
  ask for the root cause *and* an explanation I can learn from.
- **Setting up a new sweep:** ask Claude Code to draft a job-array script for a
  parameter range, then read every line before submitting.
- **Mid-analysis sanity check:** "here's my curve and my fit — suggest a diagnostic I
  can run *myself* to confirm the elastic region is really linear."
- **Brainstorming a direction:** "here's my research question and what I've tried;
  argue the strongest case *against* my current approach."
- **Cleaning code before sharing:** "refactor this for readability without changing
  behavior; explain each change."

Notice the shape of all of these: the assistant accelerates the work, but the
judgment, verification, and understanding stay with me.

---

## The ethics: non-negotiables

These aren't bureaucratic rules — they're what keeps your science trustworthy and
your name clean.

1. **Understand what you submit.** Never run code — or report a result from it — that
   you can't explain. If you don't understand it, ask the assistant to *teach* you
   until you do. "The AI wrote it" is never an excuse for a mistake in your paper.
2. **Verify against ground truth.** MD, the LAMMPS docs, the real paper, a known
   limiting case. The chatbot is never the arbiter of truth in this lab — the physics
   is.
3. **Never fabricate.** Don't let a model generate data, fill in a missing number, or
   invent a citation. This is research misconduct, full stop, regardless of intent.
4. **Be transparent.** Follow the norms of Northwestern, our field, and each journal
   on disclosing AI assistance. When in doubt, disclose.
5. **Mind confidentiality.** Don't paste unpublished data, private results, or
   anything sensitive into an external tool without checking it's appropriate. Ask
   first.
6. **Protect your own growth.** The point of a PhD is to *become* an expert. If you
   let the assistant do the thinking, you'll graduate unable to do the thing you
   trained for. Use it to learn faster, never to avoid learning. A good gut check:
   *am I using this to understand something, or to avoid understanding it?*

---

## A healthy default workflow

For any assisted task:

1. **Ask it to explain, not just produce.** "Explain the approach before you write
   the code."
2. **Read the output critically.** Does it make sense? Would you have done it this way?
3. **Run it on something you can check.** A tiny case with a known answer.
4. **Verify against an external source of truth.** Docs, theory, a second method.
5. **Make it yours.** Rewrite until you understand every line. Now it's your work.

---

## ✅ Checkpoint (and the end of the core tutorial)

You've arrived when you can:
1. state the one principle — you're the accountable scientist, the assistant is a
   fallible collaborator;
2. give one task you'd happily use an assistant for and one you'd never delegate;
3. explain why "the AI wrote it" never excuses an error in your research.

---

You've now gone from an empty terminal to running molecular dynamics, extracting
mechanical properties, touching the lab's machine-learning core, and using AI tools
like a responsible researcher. **Welcome to the lab.** 🎉

Head back to the [README](../README.md) for where to go next, or open
[`prompts/ai_prompt_library.md`](../prompts/ai_prompt_library.md) and start building
your own prompt habits.
