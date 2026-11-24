# Module 7 — AI as a Junior Engineer

> **Why this matters for us.** AI coding assistants (Claude Code, and chat assistants
> like Claude and ChatGPT) are part of a computational researcher's toolkit now — I
> use them every day. The useful question isn't *whether* to use them. It's **what
> role you put them in.** In this lab they have exactly one: a capable **junior
> engineer**. Fast, broadly trained, genuinely helpful, and accountable for nothing.
> The accountable role is yours, and it's the harder one.

---

## The one principle: you sign the drawing

A licensed engineer stamps a set of drawings. A whole team may have drafted them —
but the stamp says one thing: *I examined this, and I stand behind it.* No one has
ever accepted "the drafter made the error" as a defense. The stamp **is** the
accountability.

Reporting a number from a simulation is the same act. The moment a modulus goes into
your slide, your paper, or your advisor's inbox, you have stamped it.

> **An AI assistant drafts. You audit, and you sign.** You are accountable for every
> line of code you run and every number you report, no matter who — or what — wrote it.

If you take one thing from this whole tutorial, take that. Everything below follows
from it.

And notice what it implies about your training. The skill that will define your
career is not producing a first draft faster than everyone else — a machine does that
now, cheaply. It's being the person who can **look at work you did not produce and
tell whether it's right.** That is a deeper skill than drafting, it takes longer to
build, and it's the one this module is really teaching.

---

## What an audit actually looks like

"Review it carefully" is advice, not a skill. An audit is a specific sequence of
checks — and it's the same sequence whether you're checking a junior engineer's beam
calculation or an assistant's analysis script.

1. **Check the inputs.** Did it use *your* data, *your* units, *your* boundary
   conditions? The most common failure by far is a perfectly correct method applied
   to the wrong thing.
2. **Check the method against theory.** Does the approach match what the physics
   says it should be? If it fit a modulus, did it fit over a region that's actually
   linear?
3. **Check a case where you already know the answer.** A limiting case, an analytical
   solution, a published result, a tiny system you can work out by hand. This is the
   single highest-value check you can run.
4. **Check the magnitude.** Is 2 GPa believable for this material? Order-of-magnitude
   sense is engineering judgment, and it catches the errors the other checks miss —
   especially unit errors, which are silent and catastrophic.
5. **Check what it *didn't* tell you.** Silent defaults, dropped data points,
   assumptions it never surfaced. Ask directly: *what did you assume here, and where
   would this break?*
6. **Check that you can explain it.** If you can't walk a labmate through why it
   works, the audit isn't finished — no matter how good the output looks.

Run this on your own code too. It was never only about the AI.

---

## Where a junior engineer helps (delegate freely)

- **Explaining unfamiliar things.** A cryptic SLURM error, a dense LAMMPS command, a
  chunk of a labmate's code. Assistants are excellent tutors — *if you ask them to
  teach you, not just to hand you the answer.*
- **Scaffolding.** Turning "plot toughness vs crosslink density with error bars" into
  a first draft you then audit.
- **Debugging.** Paste the code and the error; ask for the root cause and *why*.
- **Refactoring.** Making working-but-ugly code readable.
- **Brainstorming.** Pressure-testing an idea, listing approaches you hadn't
  considered, arguing the other side.
- **Boilerplate.** Argument parsing, file I/O, plot styling — tedious, not
  intellectually load-bearing.

## Where they fail (audit hardest here)

- **Specifics.** LAMMPS commands, library APIs, and numerical details come out subtly
  wrong, outdated, or version-mismatched — delivered with total confidence. Check the
  official docs, and check that the thing runs and gives sane numbers.
- **Physical judgment.** Whether a modulus is believable, whether a model learned
  physics or an artifact. This cannot be delegated. It's the job.
- **Citations.** Assistants invent plausible references. Never cite a paper you
  haven't found and read yourself.
- **Your data.** They can't see whether your simulation converged, and they don't
  know your system unless you tell them.

The pattern: **excellent for accelerating things you could verify yourself; dangerous
for anything you'd be taking on faith.**

---

## Claude Code (a junior engineer with hands)

Beyond chat, **Claude Code** works directly in your terminal and files — it reads your
repo, runs commands, edits scripts, and iterates. It's genuinely useful for the
setup-heavy parts of the work: wiring a new analysis pipeline, sweeping parameters,
organizing a messy project folder, drafting a plotting script against your real data.

Because it can *act*, the audit tightens rather than relaxes. Read every diff before
accepting it. Run the code and look at the output yourself. A junior engineer who can
also push buttons is more useful and more dangerous at the same time.

---

## A day in the life (how I actually use these)

The copy-pasteable versions live in
[`prompts/ai_prompt_library.md`](../prompts/ai_prompt_library.md):

- **Morning, decoding an overnight job failure:** paste the SLURM error and script,
  ask for the root cause *and* an explanation I can learn from.
- **Setting up a new sweep:** have Claude Code draft a job-array script, then read
  every line before submitting.
- **Mid-analysis sanity check:** "here's my curve and my fit — suggest a diagnostic I
  can run *myself* to confirm the elastic region is really linear."
- **Brainstorming a direction:** "here's my research question and what I've tried;
  argue the strongest case *against* my current approach."
- **Cleaning code before sharing:** "refactor for readability without changing
  behavior; explain each change."

Notice the shape: the assistant drafts, the judgment stays with me.

---

## Engineering judgment: the non-negotiables

These aren't bureaucratic rules bolted onto the science. Engineering has always tied
competence to responsibility — the stamp means something precisely because someone
can be held to it. These are what that looks like for us.

1. **Understand what you submit.** Never run code, or report a number from it, that
   you can't explain. If you don't understand it, ask the assistant to *teach* you
   until you do. "The AI wrote it" has never excused an error in a paper, and it
   never will.
2. **Verify against ground truth.** MD, the LAMMPS docs, the real paper, a known
   limiting case. The chatbot is never the arbiter of truth in this lab — the physics
   is.
3. **Never fabricate.** Don't let a model generate data, fill a missing number, or
   invent a citation. That's research misconduct, full stop, regardless of intent.
4. **Be transparent.** Follow the norms of Northwestern, our field, and each journal
   on disclosing AI assistance. When in doubt, disclose, and ask me.
5. **Mind confidentiality.** Don't paste unpublished data, private results, or
   anything sensitive into an external tool without checking that it's appropriate.
   Ask first.
6. **Protect your own growth.** The point of a PhD is to *become* the person who can
   do the audit. If you let the assistant do the thinking, you'll graduate unable to
   do the thing you trained for. The gut check: *am I using this to understand
   something, or to avoid understanding it?*

---

## A healthy default workflow

1. **Ask it to explain, not just produce.** "Explain the approach before writing code."
2. **Read it critically.** Does it make sense? Would you have done it this way?
3. **Run it on something you can check.** A tiny case with a known answer.
4. **Verify against an external source of truth.** Docs, theory, a second method.
5. **Make it yours.** Rewrite until you understand every line. Now you can sign it.

---

## ✅ Checkpoint (and the end of the core tutorial)

You've arrived when you can:
1. state the principle — the assistant drafts, you audit and you sign;
2. run the six-step audit on a script you didn't write;
3. name one task you'd happily delegate and one you never would, and say why;
4. explain why "the AI wrote it" never excuses an error in your research.

---

You've gone from an empty terminal to running molecular dynamics, extracting
mechanical properties, touching the lab's machine-learning core, and holding AI tools
to an engineer's standard. **Welcome to the lab.** 🎉

Head back to the [README](../README.md) for where to go next, or open
[`prompts/ai_prompt_library.md`](../prompts/ai_prompt_library.md) and start building
your own prompt habits.
