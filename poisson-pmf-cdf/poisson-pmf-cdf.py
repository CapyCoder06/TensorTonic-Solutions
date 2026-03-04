import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    Returns: (pmf, cdf)
    """
    
    if lam <= 0 or k < 0 or k > 50:
        raise ValueError("Invalid input")

    # compute log factorials up to k
    log_fact = np.zeros(k + 1)
    if k > 0:
        log_fact[1:] = np.cumsum(np.log(np.arange(1, k + 1)))

    # log pmf values
    i = np.arange(k + 1)
    log_p = i * np.log(lam) - lam - log_fact

    p = np.exp(log_p)

    pmf = p[k]
    cdf = p.sum()

    return float(pmf), float(cdf)