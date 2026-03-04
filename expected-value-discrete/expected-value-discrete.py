import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    values = np.asarray(x)
    weights = np.asarray(p)
    result = (values * weights).sum()
    if (weights.sum() != 1): 
        raise ValueError
    return result
    pass
