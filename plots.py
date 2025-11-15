# plots.py
"""
Plotting functions for continuous distributions.

Each function expects a distribution object with:
- pdf(x)
- cdf(x)
- sample(n)

All functions now support saving images via: save_as="filename.png"
"""

import numpy as np
import matplotlib.pyplot as plt
import os


# Utility to save figure inside images/ folder
def save_plot(fig, filename):
    folder = "images"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    fig.savefig(path, dpi=300, bbox_inches="tight")


def plot_pdf(dist, x_min, x_max, num_points=500,
             ax=None, title="PDF", save_as=None):

    x = np.linspace(x_min, x_max, num_points)
    y = dist.pdf(x)

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))
    else:
        fig = ax.figure

    ax.plot(x, y, linewidth=2)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(title)
    ax.grid(True)

    if save_as is not None:
        save_plot(fig, save_as)

    return ax


def plot_cdf(dist, x_min, x_max, num_points=500,
             ax=None, title="CDF", save_as=None):

    x = np.linspace(x_min, x_max, num_points)
    y = dist.cdf(x)

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))
    else:
        fig = ax.figure

    ax.plot(x, y, linewidth=2)
    ax.set_xlabel("x")
    ax.set_ylabel("F(x)")
    ax.set_title(title)
    ax.grid(True)

    if save_as is not None:
        save_plot(fig, save_as)

    return ax


def plot_pdf_with_interval(dist, x_min, x_max, a, b, num_points=500,
                           ax=None, title="PDF with interval", save_as=None):

    if a > b:
        a, b = b, a

    x = np.linspace(x_min, x_max, num_points)
    y = dist.pdf(x)

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))
    else:
        fig = ax.figure

    ax.plot(x, y, linewidth=2)

    mask = (x >= a) & (x <= b)
    ax.fill_between(x[mask], y[mask], alpha=0.3)

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(title)
    ax.grid(True)

    prob = dist.cdf(b) - dist.cdf(a)

    if save_as is not None:
        save_plot(fig, save_as)

    return ax, float(prob)


def plot_sample_histogram(dist, sample_size, x_min, x_max,
                          bins=30, ax=None, title="Histogram", save_as=None):

    samples = dist.sample(sample_size)
    x = np.linspace(x_min, x_max, 500)
    pdf_vals = dist.pdf(x)

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))
    else:
        fig = ax.figure

    ax.hist(samples, bins=bins, density=True, alpha=0.4, edgecolor="black")
    ax.plot(x, pdf_vals, linewidth=2)

    ax.set_xlabel("x")
    ax.set_ylabel("Density")
    ax.set_title(title)
    ax.grid(True)

    if save_as is not None:
        save_plot(fig, save_as)

    return ax
