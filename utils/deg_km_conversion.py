### Geographic distance conversion utilities.

import numpy as np

def deg2km(lon1, lat1, lon2, lat2):
    """
    Convert geographic coordinates to Cartesian distances.
    
    Args:
        lon1 (float): Longitude of first point in degrees
        lat1 (float): Latitude of first point in degrees
        lon2 (float): Longitude of second point in degrees
        lat2 (float): Latitude of second point in degrees
    
    Returns:
        tuple: (dx, dy) where:
            - dx (float): Distance in km Eastwards
            - dy (float): Distance in km Northwards
    """
    # Calculate distance in degrees
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    # Calculate mean latitude for projection
    latm = (lat1 + lat2) / 2.0
    
    # Convert to Cartesian distances (km)
    # Earth radius: 6371 km
    EARTH_RADIUS_M = 6371000
    DEG_TO_RAD = np.pi / 180.0
    
    dx = DEG_TO_RAD * np.cos(np.radians(latm)) * EARTH_RADIUS_M * dlon
    dy = DEG_TO_RAD * EARTH_RADIUS_M * dlat
    
    return (dx / 1000.0, dy / 1000.0)


def km2deg(dx, dy, latm):
    """
    Convert Cartesian distances to geographic coordinate differences.
    
    Inverse function of deg2km.
    
    Args:
        dx (float): Distance in km Eastwards
        dy (float): Distance in km Northwards
        latm (float): Mean latitude in degrees for projection
    
    Returns:
        tuple: (dlon, dlat) where:
            - dlon (float): Longitude difference in degrees
            - dlat (float): Latitude difference in degrees
    """
    # Convert distances to meters
    dx_m = dx * 1000
    dy_m = dy * 1000
    
    # Earth radius: 6371 km
    EARTH_RADIUS_M = 6371000
    RAD_TO_DEG = 180.0 / np.pi
    
    # Convert to degree differences
    dlon = (dx_m / (np.cos(np.radians(latm)) * EARTH_RADIUS_M)) * RAD_TO_DEG
    dlat = (dy_m / EARTH_RADIUS_M) * RAD_TO_DEG
    
    return (dlon, dlat)
