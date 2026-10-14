import numpy as np

def mov_average(data, span):
    """
    Apply a moving average filter to a time series.
    
    Args:
        data (np.ndarray): Time series data to filter
        span (int): Span of the moving average window (must be odd)
    
    Returns:
        np.ndarray: Filtered data with the same shape as input
    
    Notes:
        - Edge points use asymmetric windows to handle boundaries
        - Center points use symmetric windows of the specified span
    """
    # Calculate number of points on each side of center
    p = int(np.floor(span / 2))
    
    # Initialize output array with NaN values
    data_smooth = np.ones(data.shape) * np.nan
    
    # Apply moving average
    for i in range(len(data)):
        if i < p:
            # Left edge: use available points from start to i+p
            window = data[:i + p + 1]
            data_smooth[i] = np.sum(window) / float(len(window))
        elif i > (len(data) - p - 1):
            # Right edge: use available points from i-p to end
            window = data[i - p:]
            data_smooth[i] = np.sum(window) / float(len(window))
        else:
            # Center: use symmetric window
            window = data[i - p:i + p + 1]
            data_smooth[i] = np.sum(window) / float(span)
    
    return data_smooth
