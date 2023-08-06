import sys
from os.path import dirname

import numpy as np
from numpy import deg2rad, rad2deg, sin, cos, tan, sqrt

SRC_DIR = dirname(__file__)
sys.path.append(SRC_DIR)

import inputs
import pilotUtils
import wgs84


def earthGeoRad(_lla:       np.ndarray,
                angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate Earth's geocentric radius at a given geodetic latitude in
    meters. "The geocentric radius is the distance from the Earth's
    center to a point on the spheroid surface at geodetic latitude".

    https://en.wikipedia.org/wiki/Earth_radius
    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude angle (True for rad and False for degrees)

    Returns:
    --------
    np.ndarray
        Nx1 array of Earth's geocentric radius in meters at the given latitudes in meters
    '''
    
    lla = _lla.copy()
    
    inputs.assert3Vec(lla)
    
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)
    
    lat = lla[:, [0]]

    if angle_unit == pilotUtils.DEGREES:
        lat = deg2rad(lat)

    num = (wgs84.a_sqrd * cos(lat))**2 + (wgs84.b_sqrd * sin(lat))**2
    den = (wgs84.a * cos(lat))**2 + (wgs84.b * sin(lat))**2

    return sqrt(num / den)

def earthRad(_lla:       np.ndarray,
             angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate Earth's radius of curvature in the prime vertical (East -
    West) - denoted as N - and meridian (North - South) - denoted as
    M - at a given latitude.

    https://en.wikipedia.org/wiki/Radius_of_curvature
    https://en.wikipedia.org/wiki/Earth_radius
    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude angle (True for rad and False for degrees)

    Returns:
    --------
    np.ndarray
        Earth's radii of curvature in meters at a given
        latitude -> [Nx1 prime vertical, Nx1 meridian] 
    '''
    
    lla = _lla.copy()
    
    inputs.assert3Vec(lla)
    
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)
    
    lat = lla[:, [0]]

    if angle_unit == pilotUtils.DEGREES:
        lat = deg2rad(lat)

    R_N = wgs84.a / sqrt(1 - (wgs84.ecc_sqrd * sin(lat)**2))
    R_M = (wgs84.a * (1 - wgs84.ecc_sqrd)) / (1 - (wgs84.ecc_sqrd * sin(lat)**2))**1.5
    
    return np.hstack([R_N,  # Earth's prime-vertical radius of curvature
                      R_M]) # Earth's meridional radius of curvature

def earthGaussRad(_lla:       np.ndarray,
                  angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate Earth's gaussian radius of curvature.

    https://en.wikipedia.org/wiki/Gaussian_curvature
    https://en.wikipedia.org/wiki/Radius_of_curvature
    https://en.wikipedia.org/wiki/Earth_radius
    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude angle (True for rad and False for degrees)

    Returns:
    --------
    np.ndarray
        Nx1 Earth's gaussian radii of curvature
    '''
    
    eradvec = earthRad(_lla       = _lla,
                       angle_unit = angle_unit)
    
    Rns = eradvec[:, [0]]
    Rew = eradvec[:, [1]]
    
    return np.sqrt(Rns * Rew)

def earthAzimRad(_lla:       np.ndarray,
                 _azimuth:   float,
                 angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate azimuthal radius at a given latitude. This is the
    Earth's radius of cuvature at a given latitude in the
    direction of a given asimuth.

    https://en.wikipedia.org/wiki/Radius_of_curvature
    https://en.wikipedia.org/wiki/Earth_radius
    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude angle (True for rad and False for degrees)

    Returns:
    --------
    np.ndarray
        Nx1 Earth's azimuthal radius in meters at a given latitude and azimuth
    '''
    
    if type(_azimuth) is not np.ndarray:
        azimuth = np.array(_azimuth)
    else:
        azimuth = _azimuth.copy()

    if angle_unit == pilotUtils.DEGREES:
        azimuth = deg2rad(azimuth)

    eradvec = earthRad(_lla, angle_unit)
    N = eradvec[:, [0]]
    M = eradvec[:, [1]]

    return 1 / ((cos(azimuth)**2 / M) + (sin(azimuth)**2 / N))

def earthRate(_lla:       np.ndarray,
              angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate Earth's angular velocity in m/s resolved in the NED frame at a given
    latitude.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude angle (True for rad and False for degrees)

    Returns:
    --------
    np.ndarray
        Nx3 Earth's angular velocity resolved in the NED frame at a given latitude
    '''
    
    lla = _lla.copy()
    
    inputs.assert3Vec(lla)
    
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)
    
    lat = lla[:, [0]]

    if angle_unit == pilotUtils.DEGREES:
        lat = deg2rad(lat)

    n =  wgs84.omega_E * cos(lat)
    e =  np.zeros(n.shape)
    d = -wgs84.omega_E * sin(lat)
    
    return np.hstack([n,  # North velocity component
                      e,  # East velocity component
                      d]) # Down velocity component

def llaRate(_vned:      np.ndarray,
            _lla:       np.ndarray,
            angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the latitude, longitude, and altitude (LLA) angular rates
    given the locally tangent velocity in the NED frame and latitude.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _vned
        Nx3 Velocity vector in m/s in the NED frame
    _lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude and longitude angles (rad
        or degrees) (this also affects the output units
        (rad/s or degrees/s)

    Returns:
    --------
    lla_dot
        Nx3 LLA angular rates given the locally tangent velocity
        in the NED frame and latitude
    '''
    
    vned = _vned.copy()
    lla  = _lla.copy()
    
    inputs.assert3Vec(vned)
    inputs.assert3Vec(lla)
    
    if len(vned.shape) == 1:
        vned = vned.reshape(1, 3)
        
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)

    VN = vned[:, [0]]
    VE = vned[:, [1]]
    VD = vned[:, [2]]
    
    lat = lla[:, [0]]
    alt = lla[:, [2]]

    eradvec = earthRad(lla, angle_unit)
    Rew = eradvec[:, [0]]
    Rns = eradvec[:, [1]]

    if angle_unit == pilotUtils.DEGREES:
        lat = deg2rad(lat)
    
    alt = alt.reshape(alt.size, 1)
    lat = lat.reshape(lat.size, 1)

    if angle_unit == pilotUtils.RADIANS:
        lla_dot = np.hstack([VN / (Rns + alt),            # North component angular rate
                             VE / (Rew + alt) / cos(lat), # East component angular rate
                            -VD])                         # Down component angular rate
    
    else:
        lla_dot = np.hstack([rad2deg(VN / (Rns + alt)),            # North component angular rate
                             rad2deg(VE / (Rew + alt) / cos(lat)), # East component angular rate
                            -VD])                                  # Down component angular rate

    return lla_dot

def navRate(_vned:      np.ndarray,
            _lla:       np.ndarray,
            angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the navigation/transport angular rates given the locally tangent
    velocity in the NED frame and latitude. The navigation/transport rate is
    the angular velocity of the NED frame relative to the ECEF frame.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _vned
        Nx3 Velocity vector in m/s in the NED frame
    _lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude and longitude angles (rad
        or degrees) (this also affects the output units
        (rad/s or degrees/s)

    Returns:
    --------
    rho
        Nx3 Navigation/transport angular rates in the ECEF frame given
        the locally tangent velocity in the NED frame and latitude
    '''
    
    vned = _vned.copy()
    lla  = _lla.copy()
    
    inputs.assert3Vec(vned)
    inputs.assert3Vec(lla)
    
    if len(vned.shape) == 1:
        vned = vned.reshape(1, 3)
        
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)
    
    VN = vned[:, [0]]
    VE = vned[:, [1]]

    lat = lla[:, [0]]
    alt = lla[:, [2]]

    eradvec = earthRad(lla, angle_unit)
    Rew = eradvec[:, [0]]
    Rns = eradvec[:, [1]]

    if angle_unit == pilotUtils.DEGREES:
        lat = deg2rad(lat)
        
    Rew = Rew.reshape(Rew.size, 1)
    Rns = Rns.reshape(Rns.size, 1)
    alt = alt.reshape(alt.size, 1)
    lat = lat.reshape(lat.size, 1)
    
    if angle_unit == pilotUtils.RADIANS:
        rho = np.hstack([VE / (Rew + alt),             # ECEF-X component angular rate
                        -VN / (Rns + alt),             # ECEF-Y component angular rate
                        -VE * tan(lat) / (Rew + alt)]) # ECEF-Z component angular rate
    
    else:
        rho = np.hstack([rad2deg(VE / (Rew + alt)),              # ECEF-X component angular rate
                         rad2deg(-VN / (Rns + alt)),             # ECEF-Y component angular rate
                         rad2deg(-VE * tan(lat) / (Rew + alt))]) # ECEF-Z component angular rate

    return rho

def earthGrav(_lla:       np.ndarray,
              angle_unit: bool=False):
    '''
    Calculate the local gravity magnitude due to mass attraction.
    
    Titterton D. and Weston J., "Strapdown Inertial Navigation Technology",
    2nd Edition, eqs (3.89) and (3.91)
    
    Arguments:
    ----------
    _lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude angle (True for rad and False for degrees)
    
    Returns:
    --------
    np.ndarray
        Nx1 Gravity magnitudes (m/s)
    '''
    
    lla  = _lla.copy()
    
    inputs.assert3Vec(lla)
        
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)

    lat = lla[:, [0]]
    alt = lla[:, [2]]
    
    if angle_unit == pilotUtils.DEGREES:
        lat = deg2rad(lat)
    
    g0 = wgs84.ye * (1 + (5.3024e-3 * sin(lat)**2) - (5.9e-6 * sin(2 * lat)**2))
    
    return g0 / (1 + (alt / wgs84.r))**2

def localGrav(_lla:       np.ndarray,
              angle_unit: bool=False):
    '''
    Calculate the local gravity magnitude due to mass attraction and
    centripetal acceleration.
    
    Titterton D. and Weston J., "Strapdown Inertial Navigation Technology",
    2nd Edition, eq (3.75)
    
    Arguments:
    ----------
    _lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude angle (True for rad and False for degrees)
    
    Returns:
    --------
    np.ndarray
        Nx3 Gravity vectors in the navigation frame (m/s)
    '''
    
    lla  = _lla.copy()
    
    inputs.assert3Vec(lla)
        
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)

    lat = lla[:, [0]]
    alt = lla[:, [2]]
    
    g = earthGrav(_lla       = lla,
                  angle_unit = angle_unit)
    
    gl = np.zeros(lla.shape)
    gl[:, 0] = sin(2 * lat)
    gl[:, 2] = 1 + cos(2 * lat)
    
    return g - (((wgs84.omega_E**2) * (wgs84.r + alt)) / 2) * gl