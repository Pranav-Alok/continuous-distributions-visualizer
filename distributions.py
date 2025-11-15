# distributions.py
"""
This module defines Python classes for commonly used continuous probability
distributions. Each class provides:

1. pdf(x)   – Probability density function
2. cdf(x)   – Cumulative distribution function
3. sample(n) – Generate 'n' random samples
4. mean()    – Analytical mean
5. var()     – Analytical variance

All distributions rely only on:
- numpy for array operations
- scipy.stats for reliable PDF/CDF implementations

This structure ensures the code remains readable, extensible, and mathematically correct.
"""

import numpy as np
from scipy.stats import uniform, expon, norm, gamma, beta, chi2


class UniformDist:
    """Uniform distribution U(a, b)"""

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.dist = uniform(loc=a, scale=b-a)

    def pdf(self, x):
        return self.dist.pdf(x)

    def cdf(self, x):
        return self.dist.cdf(x)

    def sample(self, n):
        return self.dist.rvs(size=n)

    def mean(self):
        return (self.a + self.b) / 2

    def var(self):
        return (self.b - self.a)**2 / 12


class ExponentialDist:
    """Exponential distribution with rate λ"""

    def __init__(self, lam):
        self.lam = lam
        self.dist = expon(scale=1/lam)

    def pdf(self, x):
        return self.dist.pdf(x)

    def cdf(self, x):
        return self.dist.cdf(x)

    def sample(self, n):
        return self.dist.rvs(size=n)

    def mean(self):
        return 1 / self.lam

    def var(self):
        return 1 / (self.lam**2)


class NormalDist:
    """Normal distribution N(μ, σ²)"""

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        self.dist = norm(loc=mu, scale=sigma)

    def pdf(self, x):
        return self.dist.pdf(x)

    def cdf(self, x):
        return self.dist.cdf(x)

    def sample(self, n):
        return self.dist.rvs(size=n)

    def mean(self):
        return self.mu

    def var(self):
        return self.sigma**2


class GammaDist:
    """Gamma distribution with shape α and rate β (scale = 1/β)"""

    def __init__(self, alpha, beta_param):
        self.alpha = alpha
        self.beta = beta_param
        self.dist = gamma(a=alpha, scale=1/beta_param)

    def pdf(self, x):
        return self.dist.pdf(x)

    def cdf(self, x):
        return self.dist.cdf(x)

    def sample(self, n):
        return self.dist.rvs(size=n)

    def mean(self):
        return self.alpha / self.beta

    def var(self):
        return self.alpha / (self.beta**2)


class BetaDist:
    """Beta distribution with α, β"""

    def __init__(self, alpha, beta_param):
        self.alpha = alpha
        self.beta = beta_param
        self.dist = beta(a=alpha, b=beta_param)

    def pdf(self, x):
        return self.dist.pdf(x)

    def cdf(self, x):
        return self.dist.cdf(x)

    def sample(self, n):
        return self.dist.rvs(size=n)

    def mean(self):
        return self.alpha / (self.alpha + self.beta)

    def var(self):
        return (self.alpha * self.beta) / \
               ((self.alpha + self.beta)**2 * (self.alpha + self.beta + 1))


class ChiSquareDist:
    """Chi-square distribution with k degrees of freedom"""

    def __init__(self, k):
        self.k = k
        self.dist = chi2(df=k)

    def pdf(self, x):
        return self.dist.pdf(x)

    def cdf(self, x):
        return self.dist.cdf(x)

    def sample(self, n):
        return self.dist.rvs(size=n)

    def mean(self):
        return self.k

    def var(self):
        return 2 * self.k
