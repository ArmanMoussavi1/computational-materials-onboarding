#!/usr/bin/env python3
"""
stress_strain.py — turn a raw stress-strain trace into mechanical properties.

Reads a two-column file (strain, stress) like the one deform.in writes, then
extracts the numbers that actually describe a material:

    * Young's modulus E   — stiffness  (slope at small strain)
    * ultimate stress     — strength   (the peak)
    * toughness           — energy absorbed before failure (area under the curve)
    * fracture strain     — how far it stretched before breaking

Usage:
    python stress_strain.py stress_strain.txt
    python stress_strain.py stress_strain.txt --elastic-limit 0.03 --out curve.png

Everything here is plain numpy + matplotlib — read it, break it, make it yours.
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt

# numpy >= 2.0 renamed trapz -> trapezoid; support both.
_trapz = getattr(np, "trapezoid", getattr(np, "trapz", None))


def load(path):
    """Load two columns (strain, stress), skipping comment lines starting with #."""
    data = np.loadtxt(path, comments="#")
    strain, stress = data[:, 0], data[:, 1]
    # keep only the loading part (strain increasing) and drop any NaNs
    good = np.isfinite(strain) & np.isfinite(stress)
    return strain[good], stress[good]


def youngs_modulus(strain, stress, elastic_limit):
    """Slope of stress vs strain in the initial (elastic) region, through the origin-ish."""
    mask = strain <= elastic_limit
    if mask.sum() < 2:
        mask = strain <= np.quantile(strain, 0.1)  # fallback: first 10% of the data
    # least-squares slope of stress = E * strain
    E, intercept = np.polyfit(strain[mask], stress[mask], 1)
    return E, intercept, mask


def toughness(strain, stress):
    """Area under the stress-strain curve up to the peak = energy density absorbed."""
    peak_i = int(np.argmax(stress))
    return _trapz(stress[: peak_i + 1], strain[: peak_i + 1]), peak_i


def fracture_point(strain, stress, drop_frac=0.5):
    """First strain, after the peak, where stress has fallen below drop_frac * peak."""
    peak_i = int(np.argmax(stress))
    peak = stress[peak_i]
    after = stress[peak_i:]
    below = np.where(after < drop_frac * peak)[0]
    if len(below) == 0:
        return strain[-1]  # never dropped far -> ductile / didn't fully break in this run
    return strain[peak_i + below[0]]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("file", help="two-column strain/stress file (e.g. stress_strain.txt)")
    p.add_argument("--elastic-limit", type=float, default=0.05,
                   help="strain below which the response is treated as elastic (default 0.05)")
    p.add_argument("--out", default="stress_strain.png", help="output figure name")
    args = p.parse_args()

    strain, stress = load(args.file)

    E, b, emask = youngs_modulus(strain, stress, args.elastic_limit)
    tough, peak_i = toughness(strain, stress)
    ult_stress = stress[peak_i]
    ult_strain = strain[peak_i]
    frac_strain = fracture_point(strain, stress)

    print("\n  mechanical properties (LJ units)")
    print("  " + "-" * 38)
    print(f"  Young's modulus  E        : {E:10.4f}")
    print(f"  ultimate stress           : {ult_stress:10.4f}   at strain {ult_strain:.3f}")
    print(f"  toughness (area to peak)  : {tough:10.4f}")
    print(f"  fracture strain (~50% drop): {frac_strain:9.3f}\n")

    # ---- plot ----
    fig, ax = plt.subplots(figsize=(6, 4.2))
    ax.fill_between(strain[: peak_i + 1], stress[: peak_i + 1], alpha=0.15,
                    color="#4E2A84", label="toughness (area)")
    ax.plot(strain, stress, color="#4E2A84", lw=2, label="stress-strain")
    ax.plot(strain[emask], E * strain[emask] + b, "--", color="#e6a817", lw=1.8,
            label=f"elastic slope  E={E:.2f}")
    ax.plot(ult_strain, ult_stress, "o", color="#e6a817", ms=7, label="ultimate stress")
    ax.set_xlabel("strain  $\\epsilon$")
    ax.set_ylabel("stress  $\\sigma$  (LJ units)")
    ax.set_title("Mechanical response")
    ax.legend(frameon=False, fontsize=9)
    fig.tight_layout()
    fig.savefig(args.out, dpi=150)
    print(f"  saved figure -> {args.out}\n")


if __name__ == "__main__":
    main()
