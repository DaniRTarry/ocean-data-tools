import pandas as pd

def get_time(time):
    """
    Convert MATLAB time format to seconds within the current minute.
    
    Args:
        time (float): MATLAB serial date number (days since January 0, 0000)
    
    Returns:
        float: Time in seconds (minutes * 60 + seconds + microseconds)
    """
    # Convert MATLAB serial date to datetime
    t = pd.to_datetime(time, unit='D')
    
    # Extract time components and convert to seconds
    tsec = t.minute * 60 + t.second + t.microsecond * 1e-6
    
    return tsec
