import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # 1. Input ko NumPy array mein convert karo with float dtype
    x_arr = np.asarray(x, dtype=float)
    
    # 2. Vectorized Sigmoid formula apply karo
    result = 1 / (1 + np.exp(-x_arr))
    
    # 3. Scalar inputs ke liye standard Python float return karo (0D array checking)
    if x_arr.ndim == 0:
        return float(result)
        
    return result# Write code here
    pass