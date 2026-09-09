# Module 1 — Files & the Terminal

> **Why this matters for us.** We build molecular models, launch simulations on a
> supercomputer, and train neural networks — mostly by *typing commands*, not clicking
> buttons. The good news: you'll do it all from inside **VS Code**, which wraps a
> friendly visual file explorer, a built-in terminal, and even AI assistants into one
> window. This module teaches you to get around **both ways** — clicking through the
> Explorer when that's easiest, and typing in the terminal when that's faster (or when
> you're on the cluster, where there's no GUI at all). Fluency in both is the
> foundation for everything else.

**Time:** ~1 hour to read + try. **You'll be able to:** move around a computer,
find and edit files, and chain commands together like a power user.

> 👋 **Never opened a terminal before? You're in exactly the right place.** Plenty of
> us started a PhD not knowing what a terminal even was — this assumes zero
> experience and builds up from nothing. Nothing below will break your computer, and
> you can't "look dumb" to a machine that's just waiting for input.

### First: how to open one

If you did [Module 0](00_setup.md), your home base is the **integrated terminal in VS
Code** — open it with `` Ctrl+` `` (the backtick key) and you're ready; skip ahead to the
mental model below. If you're starting cold, here's how to open a terminal directly:

- **macOS** — open the **Terminal** app (Spotlight: `⌘ + Space`, type "Terminal").
- **Windows** — install **WSL** (Windows Subsystem for Linux) once, then open
  "Ubuntu" from the Start menu. Or open the terminal built into **VS Code**
  (`Terminal → New Terminal`). WSL gives you a real Linux environment, which is what
  you want. *(Module 0 walks through this.)*
- **Linux** — open the **Terminal** app (you likely already know where it is).

You'll see a **prompt** — a line ending in `$` waiting for you to type. That `$` is
the computer saying "ready." Type a command, press Enter, and it runs. That's the
whole loop.

---

## Two ways to get around: click or type

VS Code gives you a **visual file explorer**, and for browsing a project it's often the
fastest, friendliest way to move around:

- **Open your project once** — `File → Open Folder` (`Ctrl+K Ctrl+O`). The whole folder
  tree appears in the **Explorer** on the left.
- **Click to explore** — expand/collapse folders with a click, single-click a file to
  open it. The **breadcrumb bar** along the top shows exactly where you are — the visual
  version of `pwd`.
- **Jump to any file by name** — `Ctrl+P` (`Cmd+P` on Mac), start typing a filename,
  press Enter. Faster than clicking through ten folders.
- **Make things** — right-click in the Explorer → *New File* / *New Folder*.
- **Open a terminal already in the right place** — right-click a folder → *Open in
  Integrated Terminal*. Now your typed commands start exactly where you're looking.

So why learn the typed commands at all? Two reasons. They're **faster** once they're in
your fingers — especially for finding, filtering, and automating — and on the
**supercomputer there is no GUI**: when you connect to Quest, typing is the *only* way
to get around. (VS Code's Remote-SSH, in Module 2, softens this by showing a file tree
even on the cluster — but the commands below are daily-use skills.) Learn both, and
reach for whichever is faster in the moment.

---

## The one-sentence mental model

A terminal is just a **conversation with the computer**: you type a command, it
does the thing, it waits for the next command. That's it. The scary black box is
really the most *honest* interface a computer has — it does exactly what you say,
nothing more.

Every command follows the same grammar:

```bash
command  -flags  arguments
```

For example, `ls -l my_folder` = *"list (`ls`) in long format (`-l`) the contents
of `my_folder`."* Once you see that pattern, every command looks familiar.

---

## Getting around by typing (your daily bread)

| Command | What it does | Analogy |
|---|---|---|
| `pwd` | print working directory — *where am I?* | reading the street sign you're standing on |
| `ls` | list what's here | looking around the room |
| `cd folder` | change directory — *go into* a folder | walking through a door |
| `cd ..` | go up one level | walking back out |
| `cd ~` | go to your home directory | teleport home |
| `mkdir name` | make a new folder | building a new room |
| `cp a b` | copy file `a` to `b` | photocopy |
| `mv a b` | move/rename `a` to `b` | move a box (or relabel it) |
| `rm file` | delete a file **(no undo!)** | shredder — there is no recycle bin |
| `cat file` | dump a file to the screen | reading a page aloud |
| `less file` | scroll through a file (`q` to quit) | flipping through a book |
| `head -n 20 file` / `tail -n 20 file` | first / last 20 lines | peeking at the start or end |

> ⚠️ **`rm` is permanent.** There's no trash can on the command line. Double-check
> before you delete, and *never* run `rm -rf` unless you are certain of the path.

**Try it:**
```bash
mkdir onboarding_practice && cd onboarding_practice
echo "hello lab" > note.txt      # create a file with some text in it
cat note.txt                     # read it back
pwd                              # confirm where you are
```

---

## Finding things (before you drown in files)

By month three you'll have thousands of files. These four commands save you:

```bash
find . -name "*.data"          # find every LAMMPS data file below the current folder
grep "fracture" notes.md       # find lines containing "fracture" in a file
grep -r "erate" .              # search ALL files below here for "erate"
history | grep lammps          # what was that lammps command I ran last week?
```

`grep` (search inside files) and `find` (search *for* files) are the two you'll
reach for constantly.

---

## Pipes and redirection (the superpower)

This is the idea that makes the terminal more than a file browser. The output of
one command can become the input of the next. Think of it like connecting garden
hoses.

- `|` (a **pipe**) sends one command's output into another:
  ```bash
  cat log.lammps | grep "Step" | head       # find step lines, show the first few
  ls | wc -l                                # count how many files are here
  ```
- `>` **writes** output to a file (overwriting); `>>` **appends**:
  ```bash
  ls -l > file_listing.txt                  # save a listing to a file
  echo "run finished" >> progress.log       # add a line to a log
  ```

**Try it:** count how many `.py` files live below your home directory:
```bash
find ~ -name "*.py" | wc -l
```

---

## A few commands you'll thank yourself for later

```bash
du -sh *          # how big is each thing here? (find the disk hogs)
df -h             # how much disk space is left?
top   (or htop)   # what's running right now? (q to quit)
chmod +x run.sh   # make a script executable so you can run ./run.sh
which python       # which python am I actually using?
```

### Loops in one line (automation starts here)

Running the same command over many files is where scripting begins:

```bash
# make five folders named run_1 ... run_5
for i in 1 2 3 4 5; do mkdir run_$i; done

# run an analysis on every data file
for f in *.data; do echo "processing $f"; python analyze.py $f; done
```

If you ever catch yourself doing the same thing by hand more than three times,
that's a loop waiting to happen.

---

## Your environment: aliases and `~/.bashrc`

`~/.bashrc` is a file that runs every time you open a terminal. It's where you set
up shortcuts. For example, add these lines to the bottom of it:

```bash
alias ll='ls -lh'                 # nicer listing
alias quest='ssh YOURNETID@quest.northwestern.edu'   # log in with one word
export EDITOR=nano                # your default text editor
```

Then run `source ~/.bashrc` to load the changes (or just open a new terminal).
Small investment, daily payoff.

---

## Editing files: VS Code first, terminal editors when you must

Most of the time you'll edit right in **VS Code** — click a file in the Explorer and go.
With the **Remote-SSH** extension (Module 2) this works even for files *on the cluster*,
so you get your full editor on remote machines. That's the default, and the nicest
experience.

But sometimes you're SSH'd into a machine with just a bare shell and need a quick edit.
For that, know one terminal editor:

- **`nano file`** — beginner-friendly; commands shown at the bottom (`^O` save, `^X`
  exit). Start here.
- **`vim file`** — powerful but steeper (`i` to type, `Esc` then `:wq` to save-and-quit,
  `:q!` to quit without saving). Worth learning eventually.

---

## 🤖 Practice using your AI assistant *well*

Your AI assistants live **right here in VS Code**. Extensions like **Claude Code** and
**Codex** (and GitHub Copilot) add a chat or agent panel beside your files, so you can
ask questions, explain a command, or edit code without leaving the editor — they can
even see the folder you're working in. Set one up from [Module 0](00_setup.md).

Throughout this tutorial you'll see these 🤖 boxes. Getting fluent with these tools is
now part of being a good computational researcher — but the goal is to *understand*, not
to outsource your thinking. A good first prompt:

> "I'm new to the Linux terminal. Explain what `grep -r "erate" .` does, piece by
> piece, and give me two safe variations to try. Don't just give me commands —
> explain the pattern so I can build my own next time."

Then **actually run** what it suggests in your `onboarding_practice` folder and
see if the explanation matches reality. Verifying beats trusting. (Full guidance
in [Module 7](07_ai_assistants.md).)

---

## ✅ Checkpoint

You can move on when you can, from a fresh VS Code window:
1. open a folder and jump to a file with `Ctrl+P`, and open a terminal in that folder;
2. create a folder, `cd` into it, and make a file with some text;
3. use `grep` to find a word inside a file;
4. explain in your own words what `ls | wc -l` does and why.

**Next:** [Module 2 — The Cluster (Quest & SLURM) →](02_hpc_quest.md)
