# Module 0 — Set Up Your Workstation (Start Here)

> **Why this matters for us.** A little setup now saves you months of friction. The
> goal of this module is to get you one **home base** — Visual Studio Code — from
> which you can edit code, run commands, connect to the supercomputer, manage Git, and
> open notebooks, all in one window. Do this first and every later module gets easier.

**Time:** ~1 hour, mostly downloads. **You'll end with:** VS Code set up as your hub,
the key tools installed, and a clear picture of what each one is *for*.

---

## The philosophy: one hub, a few specialized tools

You *can* stitch your workflow together from a dozen separate programs. Don't. We
standardize on **VS Code as the base**, plus a small set of specialized tools for the
things VS Code doesn't do (visualizing simulations, bulk file transfer). Fewer moving
parts means less that can break and less to explain when you ask for help.

Here's the whole recommended toolkit at a glance — the rest of this module installs and
explains each one:

| Job | Tool (our default) | Cross-platform alternatives | Why |
|---|---|---|---|
| **Edit code, run terminals, connect remotely — your hub** | **VS Code** | — | one window for everything below |
| **A real Linux environment on Windows** | **WSL** (Ubuntu) | native on macOS/Linux | the cluster is Linux; match it locally |
| **Connect to & edit files on Quest** | **VS Code Remote-SSH** | — | edit remote files as if they're local |
| **Bulk / GUI file transfer to the cluster** | **MobaXterm** or **Bitvise** (Windows) | **FileZilla**, **Cyberduck** (all) | drag-and-drop big folders; visual SFTP |
| **Very large datasets to/from Quest** | **Globus** | — | robust, resumable transfers (Quest supports it) |
| **Visualize MD trajectories** | **OVITO** | VMD | see and analyze your simulations |
| **Version control** | **Git** (+ GitHub) | GitHub Desktop (GUI) | share and back up code |
| **Python environments** | **conda** (Miniconda) | mamba (faster) | isolate project dependencies |
| **Exploratory analysis** | **Jupyter** (inside VS Code) | JupyterLab | quick plots and prototyping |

You don't need all of these today — install VS Code, WSL (if on Windows), and Git now;
add OVITO before Module 4 and conda before Module 6. The table is your map.

---

## Step 1 — Install VS Code (everyone)

Download from [code.visualstudio.com](https://code.visualstudio.com) and install. This
is the one program you'll open every day.

Take two minutes to learn three things:
- **The integrated terminal** — `` Ctrl+` `` (backtick) opens a real terminal *inside*
  VS Code. From here on, this is where you'll run the commands in Module 1.
- **The Explorer** — the file tree on the left. Open a folder with `File → Open Folder`.
- **The Command Palette** — `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac). Type what you want
  ("Python: Select Interpreter", "Remote-SSH: Connect to Host") instead of hunting menus.

---

## Step 2 — Windows only: install WSL

Our simulations run on Linux, so you want Linux locally too. **WSL** (Windows Subsystem
for Linux) gives you a real Ubuntu environment inside Windows — no dual-boot, no VM
hassle. In **PowerShell** (run as Administrator), once:

```powershell
wsl --install
```

Restart, and you'll have "Ubuntu" in your Start menu. Then, in VS Code, install the
**WSL** extension (next step) and click the blue `><` corner → **Connect to WSL**. Now
VS Code — terminal, files, and all — runs inside Linux. This is the single biggest
quality-of-life win for Windows users. *(macOS and Linux users already have a Unix
shell and can skip this.)*

---

## Step 3 — Install the essential VS Code extensions

Open the Extensions panel (`Ctrl+Shift+X`) and install:

| Extension | What it gives you |
|---|---|
| **Remote - SSH** | edit files and run terminals *on Quest* from your laptop |
| **WSL** (Windows) | run VS Code inside your Linux environment |
| **Python** (by Microsoft) | linting, debugging, environment selection |
| **Jupyter** | run notebooks right inside VS Code |
| **Pylance** | fast Python autocomplete and type hints |

Nice-to-haves once you're comfortable: **GitLens** (see who changed what), **Rainbow
CSV** (readable data files), **Error Lens** (inline error messages), and a **LAMMPS
syntax** highlighting extension for `.in` files.

**AI coding assistants (optional but recommended).** Extensions like **Claude Code** and
**Codex** (and GitHub Copilot) put an AI chat/agent panel right beside your files — handy
for explaining commands, debugging, and scaffolding code without leaving the editor.
Install whichever your group uses; [Module 7](07_ai_assistants.md) covers how to use
them responsibly (the *how* matters as much as the *which*).

---

## Step 4 — Install Git

Version control is how we share and back up code (it's how you'll grab and publish repos
like this one).

- **Windows:** `winget install --id Git.Git` in a terminal, or download from
  [git-scm.com](https://git-scm.com). *(Inside WSL, instead run `sudo apt install git`.)*
- **macOS:** `brew install git` (or it comes with the Xcode command-line tools).
- **Linux:** `sudo apt install git` (or your distro's equivalent).

Then tell Git who you are (once):
```bash
git config --global user.name "Your Name"
git config --global user.email "you@u.northwestern.edu"
```
Prefer clicking to typing? The **GitHub Desktop** app is a friendly GUI for the basics.

---

## Step 5 — A file-transfer client (before you hit the cluster)

VS Code Remote-SSH already lets you edit and move individual files on Quest. But for
**bulk transfers** — pushing a whole simulation folder, pulling gigabytes of results — a
dedicated SFTP client with a drag-and-drop window is much nicer:

- **Windows:** **MobaXterm** (terminal + SFTP + X11 in one; very popular in HPC) or
  **Bitvise SSH Client** (clean SFTP GUI). Either is a great pick.
- **Any platform:** **FileZilla** or **Cyberduck** — simple, visual drag-and-drop SFTP.

For **very large datasets**, Northwestern's Quest supports **Globus** — a robust,
resumable transfer service that beats plain `scp` for big moves. Set it up when you
first need to shuttle a large dataset; Module 2 covers the everyday `scp`/`rsync`
commands.

---

## Step 6 — Install OVITO (before Module 4)

**OVITO** ([ovito.org](https://www.ovito.org)) is how you'll *see* your simulations —
load a LAMMPS trajectory, watch the material deform, color atoms by stress or type. The
free **Basic** version is plenty to start. It's the fastest way to catch a broken
simulation: if it looks wrong, it probably is. (VMD is a capable alternative, more
common in the biomolecular world.)

---

## Step 7 — Install conda (before Module 6)

For Python work — especially the machine-learning modules — **Miniconda** lets you keep
each project's packages in an isolated **environment** so they never clash. Install from
[docs.conda.io](https://docs.conda.io/en/latest/miniconda.html); Module 6 walks through
creating your first environment. (On Quest you'll load conda as a module instead.)

---

## 🤖 Use your AI assistant here

Setup is a great place to lean on an assistant, because every answer is easy to verify —
it either installs or it doesn't:

> "I'm on Windows and just installed WSL with Ubuntu. Walk me through connecting VS Code
> to it, step by step, and tell me how to confirm it worked."

If a command fails, paste the exact error back and ask for the cause. (More on using
these tools well in [Module 7](07_ai_assistants.md).)

---

## ✅ Checkpoint

You're ready for Module 1 when you can:
1. open VS Code and bring up its integrated terminal (`` Ctrl+` ``);
2. (Windows) open a terminal that says you're in Linux/Ubuntu, not Windows;
3. run `git --version` and see a version number.

Don't worry about Remote-SSH, OVITO, or conda working yet — you'll set those up exactly
when the module that needs them arrives.

**Next:** [Module 1 — Files & the Terminal →](01_terminal.md)
