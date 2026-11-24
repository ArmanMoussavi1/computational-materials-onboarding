#!/usr/bin/env python3
"""
tiny_surrogate.py — the whole idea of "AI for materials" in one screen.

A molecular dynamics run that measures a material's stiffness is expensive:
hours on the cluster for ONE structure. A *surrogate* is a cheap model that,
once trained on a handful of those expensive runs, predicts the answer for new
structures in microseconds. That is the seed of everything the lab does — TANGO
is just a much fancier surrogate whose input is a whole network graph.

Here the "structure" is a single number (crosslink density) and the "property"
is stiffness. We:
   1. pretend we ran 6 expensive MD simulations,
   2. fit a surrogate that also reports how *unsure* it is,
   3. use it to (a) predict everywhere instantly and (b) decide which structure
      to simulate NEXT — the core move of active learning / the lab's
      falsification loop.

Only needs numpy, scikit-learn, matplotlib.
    python tiny_surrogate.py
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel, WhiteKernel

rng = np.random.default_rng(1)

# ---- 1. the "ground truth" we normally have to pay MD to learn --------------
# A made-up but physically-flavored law: stiffness rises with crosslink density,
# then saturates. In real life you do NOT know this curve — that's the point.
def true_stiffness(x):
    return 5.0 * (1 - np.exp(-3.0 * x)) + 0.4 * x

# ---- 2. our few precious, expensive MD measurements -------------------------
x_md = np.array([0.05, 0.15, 0.30, 0.55, 0.75, 0.95])          # crosslink densities we simulated
y_md = true_stiffness(x_md) + rng.normal(0, 0.15, x_md.size)   # MD is noisy

# ---- 3. train the surrogate (a Gaussian process => predictions WITH error) --
kernel = ConstantKernel(1.0) * RBF(length_scale=0.2) + WhiteKernel(0.02)
gp = GaussianProcessRegressor(kernel=kernel, normalize_y=True, n_restarts_optimizer=5)
gp.fit(x_md.reshape(-1, 1), y_md)

# ---- 4. predict across the ENTIRE design space, instantly -------------------
x_grid = np.linspace(0, 1, 300).reshape(-1, 1)
mean, std = gp.predict(x_grid, return_std=True)

# ---- 5. active learning: where is the surrogate LEAST sure? -----------------
# That's the most informative place to spend the next expensive simulation.
next_x = x_grid[np.argmax(std), 0]

# inverse-design flavor: which structure hits a target stiffness of 4.0?
target = 4.0
best_x = x_grid[np.argmin(np.abs(mean - target)), 0]

print(f"\n  surrogate trained on {x_md.size} MD points.")
print(f"  most informative structure to simulate next : crosslink density = {next_x:.3f}")
print(f"  structure predicted to hit stiffness {target}    : crosslink density = {best_x:.3f}\n")

# ---- 6. picture is worth a thousand epochs ----------------------------------
g = x_grid.ravel()
fig, ax = plt.subplots(figsize=(6.4, 4.3))
ax.plot(g, true_stiffness(g), "k:", lw=1.4, label="true law (unknown in practice)")
ax.plot(g, mean, color="#4E2A84", lw=2, label="surrogate prediction")
ax.fill_between(g, mean - 2 * std, mean + 2 * std, color="#4E2A84", alpha=0.15,
                label="surrogate uncertainty")
ax.plot(x_md, y_md, "o", color="#e6a817", ms=8, label="the 6 MD runs")
ax.axvline(next_x, color="#c0392b", ls="--", lw=1.4, label="simulate here next")
ax.set_xlabel("structure:  crosslink density")
ax.set_ylabel("property:  stiffness")
ax.set_title("A surrogate learns structure -> property from a few simulations")
ax.legend(frameon=False, fontsize=8.5, loc="lower right")
fig.tight_layout()
fig.savefig("tiny_surrogate.png", dpi=150)
print("  saved figure -> tiny_surrogate.png\n")
