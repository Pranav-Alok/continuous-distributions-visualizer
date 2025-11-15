# utils.py
"""
Utility functions for the continuous distributions visualizer.

Includes:
- probability_between(...) using the CDF
- suggest_plot_range(...) to get a suitable [x_min, x_max] for plotting
"""

import numpy as np


def probability_between(dist, a, b):
    """
    Compute P(a <= X <= b) using the CDF of the distribution.

    Parameters
    ----------
    dist : object
        Distribution object with .cdf(x).
    a, b : float
        Interval bounds. Order does not matter.

    Returns
    -------
    float
        Probability P(a <= X <= b).
    """
    if a > b:
        a, b = b, a  # swap
    return float(dist.cdf(b) - dist.cdf(a))


def suggest_plot_range(dist_name, **params):
    """
    Suggest a reasonable [x_min, x_max] range for plotting
    given the distribution name and its parameters.

    This is not mathematically exact, but it gives visually
    meaningful ranges in most common cases.

    Parameters
    ----------
    dist_name : str
        One of: "uniform", "exponential", "normal",
                "gamma", "beta", "chi-square"
    params : dict
        Parameters of the distribution, e.g.
        - uniform: a, b
        - exponential: lam
        - normal: mu, sigma
        - gamma: alpha, beta_param
        - beta: alpha, beta_param
        - chi-square: k

    Returns
    -------
    (x_min, x_max) : tuple of floats
    """

    dist_name = dist_name.lower()

    if dist_name == "uniform":
        a = params["a"]
        b = params["b"]
        margin = 0.1 * (b - a)
        return a - margin, b + margin

    elif dist_name == "exponential":
        lam = params["lam"]
        # Mean = 1/lam, variance = 1/lam^2, so std = 1/lam
        mean = 1 / lam
        std = 1 / lam
        # from 0 to mean + 5 std is usually enough
        return 0, mean + 5 * std

    elif dist_name == "normal":
        mu = params["mu"]
        sigma = params["sigma"]
        # 4 standard deviations on both sides
        return mu - 4 * sigma, mu + 4 * sigma

    elif dist_name == "gamma":
        alpha = params["alpha"]
        beta_param = params["beta_param"]
        mean = alpha / beta_param
        var = alpha / (beta_param**2)
        std = np.sqrt(var)
        # from 0 to mean + 4 std
        return 0, mean + 4 * std

    elif dist_name == "beta":
        # Beta is always on [0, 1]
        return 0, 1

    elif dist_name in ["chi-square", "chisquare", "chi2"]:
        k = params["k"]
        mean = k
        var = 2 * k
        std = np.sqrt(var)
        return 0, mean + 4 * std

    else:
        # Fallback: simple default range
        return -5, 5
