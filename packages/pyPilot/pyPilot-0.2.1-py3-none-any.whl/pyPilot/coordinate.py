import sys
from os.path import dirname

import numpy as np
import scipy.linalg as la
from numpy import pi, deg2rad, rad2deg, sin, cos, tan, arcsin, arccos, sqrt, arctan2

SRC_DIR = dirname(__file__)
sys.path.append(SRC_DIR)

import earth
import inputs
import pilotUtils
import wgs84


def lla2ecef(_lla:       np.ndarray,
             angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a LLA coordinate to an ECEF coordinate.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system
    https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system

    Arguments:
    ----------
    lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude and longitude angles (rad
        or degrees)

    Returns:
    --------
    ecef
        Nx3 ECEF coordinate in meters
    '''
    
    lla = _lla.copy()
    
    inputs.assert3Vec(lla)
    
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)

    lat = lla[:, [0]]
    lon = lla[:, [1]]
    alt = lla[:, [2]]

    eradvec = earth.earthRad(lla, angle_unit)
    Rns = eradvec[:, [0]]

    if angle_unit == pilotUtils.DEGREES:
        lat = deg2rad(lat)
        lon = deg2rad(lon)

    ecef = np.hstack([(Rns + alt) * cos(lat) * cos(lon),
                      (Rns + alt) * cos(lat) * sin(lon),
                      ((1 - wgs84.ecc_sqrd) * Rns + alt) * sin(lat)])

    return ecef

def ecef2lla(_ecef:      np.ndarray,
             angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Convert an ECEF coordinate to a LLA coordinate.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system
    https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system
    https://www.mathworks.com/help/aeroblks/ecefpositiontolla.html

    Arguments:
    ----------
    _ecef
        Nx3 ECEF coordinate in meters
    angle_unit
        Unit of the latitude and longitude angles (rad
        or degrees)

    Returns:
    --------
    lla
        Nx3 LLA coordinate (altitude in meters)
    '''
    
    ecef = _ecef.copy()
    
    inputs.assert3Vec(ecef)
    
    if len(ecef.shape) == 1:
        ecef = ecef.reshape(1, 3)

    x = ecef[:, [0]]
    y = ecef[:, [1]]
    z = ecef[:, [2]]

    x_sqrd = x**2
    y_sqrd = y**2

    lon = arctan2(y, x)
    lat = np.ones(lon.shape) * 400

    s      = sqrt(x_sqrd + y_sqrd)
    beta   = arctan2(z, (1 - wgs84.f) * s)
    mu_bar = arctan2(z + (((wgs84.ecc_sqrd * (1 - wgs84.f)) / (1 - wgs84.ecc_sqrd)) * wgs84.a * sin(beta)**3),
                     s - (wgs84.ecc_sqrd * wgs84.a * cos(beta)**3))

    while ~(np.abs(lat - mu_bar) <= 1e-10).all():
        lat    = mu_bar
        beta   = arctan2((1 - wgs84.f) * sin(lat),
                          cos(lat))
        mu_bar = arctan2(z + (((wgs84.ecc_sqrd * (1 - wgs84.f)) / (1 - wgs84.ecc_sqrd)) * wgs84.a * sin(beta)**3),
                         s - (wgs84.ecc_sqrd * wgs84.a * cos(beta)**3))

    lat = mu_bar

    N = wgs84.a / sqrt(1 - (wgs84.ecc_sqrd * sin(lat)**2))
    h = (s * cos(lat)) + ((z + (wgs84.ecc_sqrd * N * sin(lat))) * sin(lat)) - N

    if angle_unit == pilotUtils.DEGREES:
        lat = rad2deg(lat)
        lon = rad2deg(lon)
    
    lat = lat.reshape(lat.size, 1)
    lon = lon.reshape(lon.size, 1)
    h   = h.reshape(h.size, 1)

    lla = np.hstack([lat,
                     lon,
                     h])

    return lla

def ecef2ned_dcm(_lla:       np.ndarray,
                 angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Find the direction cosine matrix that describes the rotation from the ECEF
    coordinate frame to the NED frame given a lat/lon/alt location.

    https://www.mathworks.com/help/aeroblks/directioncosinematrixeceftoned.html
    https://en.wikipedia.org/wiki/Rotation_matrix
    https://en.wikipedia.org/wiki/Geographic_coordinate_system
    https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system

    Arguments:
    ----------
    _lla
        Nx3 LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude and longitude angles (rad
        or degrees)

    Returns:
    --------
    C
        Nx3x3 ECEF to NED DCM
    '''
    
    lla = _lla.copy()
    
    inputs.assert3Vec(lla)
    
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)

    lat = lla[:, [0]]
    lon = lla[:, [1]]

    if angle_unit == pilotUtils.DEGREES:
        lat = deg2rad(lat)
        lon = deg2rad(lon)

    C = np.zeros((lla.shape[0], 3, 3))

    C[:, 0, 0] = -sin(lat) * cos(lon)
    C[:, 0, 1] = -sin(lat) * sin(lon)
    C[:, 0, 2] =  cos(lat)

    C[:, 1, 0] = -sin(lon)
    C[:, 1, 1] =  cos(lon)
    C[:, 1, 2] =  np.zeros(lon.shape)

    C[:, 2, 0] = -cos(lat) * cos(lon)
    C[:, 2, 1] = -cos(lat) * sin(lon)
    C[:, 2, 2] = -sin(lat)

    return C

def ecef2ned(_ecef:      np.ndarray,
             _lla_ref:   np.ndarray,
             angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Convert an ECEF coordinate to a NED coordinate.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system
    https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system

    Arguments:
    ----------
    _ecef
        Nx3 ECEF coordinate in meters
    _lla_ref
        Nx3 LLA coordinate of the NED frame origin (altitude in meters)
    angle_unit
        Unit of the latitude and longitude angles (rad
        or degrees)

    Returns:
    --------
    ned
        Nx3 NED coordinate in meters
    '''
    
    ecef    = _ecef.copy()
    lla_ref = _lla_ref.copy()
    
    inputs.assert3Vec(ecef)
    inputs.assert3Vec(lla_ref)
    
    if len(ecef.shape) == 1:
        ecef = ecef.reshape(1, 3)
    
    if len(lla_ref.shape) == 1:
        lla_ref = lla_ref.reshape(1, 3)
    
    ecef_ref = lla2ecef(lla_ref, angle_unit)
    C        = ecef2ned_dcm(lla_ref, angle_unit)

    return C @ (ecef - ecef_ref)

def lla2ned(lla:        np.ndarray,
            lla_ref:    np.ndarray,
            angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a LLA coordinate to a NED coordinate.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    lla
        Nx3 LLA coordinate (altitude in meters)
    lla_ref
        Nx3 LLA coordinate of the NED frame origin (altitude in meters)
    angle_unit
        Unit of the latitude and longitude angles (rad
        or degrees)

    Returns:
    --------
    ned
        Nx3 NED coordinate in meters
    '''

    ecef = lla2ecef(lla, angle_unit)
    ned  = ecef2ned(ecef, lla_ref, angle_unit)

    return ned

def ned2ecef(_ned:       np.ndarray,
             _lla_ref:   np.ndarray,
             angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a NED coordinate to an ECEF coordinate.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system
    https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system

    Arguments:
    ----------
    _ned
        Nx3 NED coordinate in meters
    _lla_ref
        Nx3 LLA coordinate of the NED frame origin (altitude in meters)
    angle_unit
        Unit of the latitude and longitude angles (rad
        or degrees)

    Returns:
    --------
    ecef
        Nx3 ECEF coordinate in meters
    '''
    
    ned     = _ned.copy()
    lla_ref = _lla_ref.copy()
    
    inputs.assert3Vec(ned)
    inputs.assert3Vec(lla_ref)
    
    if len(ned.shape) == 1:
        ned = ned.reshape(1, 3)
    
    if len(lla_ref.shape) == 1:
        lla_ref = lla_ref.reshape(1, 3)

    lat_ref = lla_ref[:, 0]
    lon_ref = lla_ref[:, 1]

    if angle_unit == pilotUtils.DEGREES:
        lat_ref = deg2rad(lat_ref)
        lon_ref = deg2rad(lon_ref)

    ecef_ref = lla2ecef(lla_ref, angle_unit)
    C        = np.zeros((ned.shape[0], 3, 3))

    C[:, 0, 0] = -sin(lat_ref) * cos(lon_ref)
    C[:, 0, 1] = -sin(lat_ref) * sin(lon_ref)
    C[:, 0, 2] =  cos(lat_ref)

    C[:, 1, 0] = -sin(lon_ref)
    C[:, 1, 1] =  cos(lon_ref)
    C[:, 1, 2] =  np.zeros(lon_ref.shape)

    C[:, 2, 0] = -cos(lat_ref) * cos(lon_ref)
    C[:, 2, 1] = -cos(lat_ref) * sin(lon_ref)
    C[:, 2, 2] = -sin(lat_ref)

    rot_ned = np.transpose(C, axes=(0, 2, 1)) @ ned
    ecef    = ecef_ref + rot_ned

    return ecef

def ned2lla(ned:        np.ndarray,
            lla_ref:    np.ndarray,
            angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a NED coordinate to a LLA coordinate.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    ned
        Nx3 NED coordinate in meters
    lla_ref
        Nx3 LLA coordinate of the NED frame origin (altitude in meters)
    angle_unit
        Unit of the latitude and longitude angles (rad
        or degrees)

    Returns:
    --------
    lla
        Nx3 LLA coordinate (altitude in meters)
    '''

    ecef     = ned2ecef(ned, lla_ref, angle_unit)
    ecef_ref = lla2ecef(lla_ref, angle_unit)
    ecef    += ecef_ref

    lla = ecef2lla(ecef, angle_unit)

    return lla

def bearingLla(_lla_1:     np.ndarray,
               _lla_2:     np.ndarray,
               angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the bearing between two LLA coordinates.

    http://www.movable-type.co.uk/scripts/latlong.html
    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _lla_1
        Nx3 First LLA coordinate (altitude in meters)
    _lla_2
        Nx3 Second LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude, longitude, and bearing
        angles (True for rad and False for degrees)

    Returns:
    --------
    bearing
        Nx1 bearing between the two given LLA coordinates
    '''
    
    lla_1 = _lla_1.copy()
    lla_2 = _lla_2.copy()
    
    inputs.assert3Vec(lla_1)
    inputs.assert3Vec(lla_2)
    
    if len(lla_1.shape) == 1:
        lla_1 = lla_1.reshape(1, 3)
    
    if len(lla_2.shape) == 1:
        lla_2 = lla_2.reshape(1, 3)
    
    lat_1 = lla_1[:, [0]]
    lon_1 = lla_1[:, [1]]

    lat_2 = lla_2[:, [0]]
    lon_2 = lla_2[:, [1]]

    if angle_unit == pilotUtils.DEGREES:
        lat_1 = deg2rad(lat_1)
        lon_1 = deg2rad(lon_1)

        lat_2 = deg2rad(lat_2)
        lon_2 = deg2rad(lon_2)

    deltaLon = lon_2 - lon_1

    x = cos(lat_2) * sin(deltaLon)
    y = (cos(lat_1) * sin(lat_2)) - (sin(lat_1) * cos(lat_2) * cos(deltaLon))
    
    if angle_unit == pilotUtils.DEGREES:
        return (rad2deg(arctan2(x, y)) + 360) % 360
    return pilotUtils.wrapToPi(arctan2(x, y))

def bearingNed(_ned_1: np.ndarray,
               _ned_2: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the bearing between two NED coordinates.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _ned_1
        Nx3 First NED coordinate in meters
    _ned_2
        Nx3 Second NED coordinate in meters
    angle_unit
        Unit of the latitude, longitude, and bearing
        angles (True for rad and False for degrees)

    Returns:
    --------
    bearing
        Nx1 bearing between the two given LLA coordinates
    '''
    
    ned_1 = _ned_1.copy()
    ned_2 = _ned_2.copy()
    
    inputs.assert3Vec(ned_1)
    inputs.assert3Vec(ned_2)
    
    if len(ned_1.shape) == 1:
        ned_1 = ned_1.reshape(1, 3)
    
    if len(ned_2.shape) == 1:
        ned_2 = ned_2.reshape(1, 3)
    
    n_1 = ned_1[:, [0]]
    e_1 = ned_1[:, [1]]

    n_2 = ned_2[:, [0]]
    e_2 = ned_2[:, [1]]

    x = e_2 - e_1
    y = n_2 - n_1

    return (rad2deg(arctan2(x, y)) + 360) % 360

def distanceLla(_lla_1:     np.ndarray,
                _lla_2:     np.ndarray,
                angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the arc distance between two LLA coordinates.

    http://www.movable-type.co.uk/scripts/latlong.html
    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _lla_1
        Nx3 First LLA coordinate (altitude in meters)
    _lla_2
        Nx3 Second LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude and longitude angles (rad
        or degrees)

    Returns:
    --------
    dist
        Nx1 distance between the two given LLA coordinates in meters
    '''
    
    lla_1 = _lla_1.copy()
    lla_2 = _lla_2.copy()
    
    inputs.assert3Vec(lla_1)
    inputs.assert3Vec(lla_2)
    
    if len(lla_1.shape) == 1:
        lla_1 = lla_1.reshape(1, 3)
    
    if len(lla_2.shape) == 1:
        lla_2 = lla_2.reshape(1, 3)
    
    lat_1 = lla_1[:, [0]]
    lon_1 = lla_1[:, [1]]

    lat_2 = lla_2[:, [0]]
    lon_2 = lla_2[:, [1]]

    if angle_unit == pilotUtils.DEGREES:
        lat_1 = deg2rad(lat_1)
        lon_1 = deg2rad(lon_1)

        lat_2 = deg2rad(lat_2)
        lon_2 = deg2rad(lon_2)

    deltaLat = lat_2 - lat_1
    deltaLon = lon_2 - lon_1

    _a = (sin(deltaLat / 2) * sin(deltaLat / 2)) + cos(lat_1) * cos(lat_2) * (sin(deltaLon / 2)) * (sin(deltaLon / 2))

    azimuth = bearingLla(lla_1, lla_2, angle_unit)
    radius  = earth.earthAzimRad(lla_1, azimuth, angle_unit) # TODO: Add altitude?

    return 2 * radius * arctan2(sqrt(_a), sqrt(1 - _a))

def distanceNed(_ned_1: np.ndarray,
                _ned_2: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the total distance between two NED coordinates.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _ned_1
        Nx3 First NED coordinate in meters
    _ned_2
        Nx3 Second NED coordinate in meters

    Returns:
    --------
    dist
        Nx1 total distance between the two given NED coordinates
    '''
    
    ned_1 = _ned_1.copy()
    ned_2 = _ned_2.copy()
    
    inputs.assert3Vec(ned_1)
    inputs.assert3Vec(ned_2)
    
    if len(ned_1.shape) == 1:
        ned_1 = ned_1.reshape(1, 3)
    
    if len(ned_2.shape) == 1:
        ned_2 = ned_2.reshape(1, 3)
    
    ned_diff = ned_2 - ned_1
    
    return la.norm(ned_diff, axis=1)[:, np.newaxis]

def distanceNedHoriz(_ned_1: np.ndarray,
                     _ned_2: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the horizontal distance between two NED coordinates.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _ned_1
        Nx3 First NED coordinate in meters
    _ned_2
        Nx3 Second NED coordinate in meters

    Returns:
    --------
    dist
        Nx1 horizontal distance between the two given NED coordinates
    '''
    
    ned_1 = _ned_1.copy()
    ned_2 = _ned_2.copy()
    
    inputs.assert3Vec(ned_1)
    inputs.assert3Vec(ned_2)
    
    if len(ned_1.shape) == 1:
        ned_1 = ned_1.reshape(1, 3)
    
    if len(ned_2.shape) == 1:
        ned_2 = ned_2.reshape(1, 3)
    
    ned_diff = (ned_2 - ned_1)[:, :2]

    return la.norm(ned_diff, axis=1)[:, np.newaxis]

def distanceNedVert(_ned_1: np.ndarray,
                    _ned_2: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the vertical distance between two NED coordinates.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _ned_1
        Nx3 First NED coordinate in meters
    _ned_2
        Nx3 Second NED coordinate in meters

    Returns:
    --------
    dist
        Nx1 vertical distance between the two given NED coordinates
    '''
    
    ned_1 = _ned_1.copy()
    ned_2 = _ned_2.copy()
    
    inputs.assert3Vec(ned_1)
    inputs.assert3Vec(ned_2)
    
    if len(ned_1.shape) == 1:
        ned_1 = ned_1.reshape(1, 3)
    
    if len(ned_2.shape) == 1:
        ned_2 = ned_2.reshape(1, 3)
    
    dist = (ned_2 - ned_1)[:, 3]
    
    return dist

def distanceEcef(_ecef_1: np.ndarray,
                 _ecef_2: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the total distance between two ECEF coordinates.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system
    https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system

    Arguments:
    ----------
    _ecef_1
        Nx3 First ECEF coordinate in meters
    _ecef_2
        Nx3 Second ECEF coordinate in meters

    Returns:
    --------
    dist
        Nx1 total distance between the two given ECEF coordinates
    '''
    
    ecef_1 = _ecef_1.copy()
    ecef_2 = _ecef_2.copy()
    
    inputs.assert3Vec(ecef_1)
    inputs.assert3Vec(ecef_2)
    
    if len(ecef_1.shape) == 1:
        ecef_1 = ecef_1.reshape(1, 3)
    
    if len(ecef_2.shape) == 1:
        ecef_2 = ecef_2.reshape(1, 3)
    
    ecef_diff = ecef_2 - ecef_1
    
    return la.norm(ecef_diff, axis=1)[:, np.newaxis]

def elevationLla(_lla_1:     np.ndarray,
                 _lla_2:     np.ndarray,
                 angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the elevation angle between two LLA coordinates.

    http://www.movable-type.co.uk/scripts/latlong.html
    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _lla_1
        Nx3 First LLA coordinate (altitude in meters)
    _lla_2
        Nx3 Second LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude, longitude, and elevation
        angles (True for rad and False for degrees)

    Returns:
    --------
    elevation
        Nx1 elevation angle between the two given LLA coordinates
    '''
    
    lla_1 = _lla_1.copy()
    lla_2 = _lla_2.copy()
    
    inputs.assert3Vec(lla_1)
    inputs.assert3Vec(lla_2)
    
    if len(lla_1.shape) == 1:
        lla_1 = lla_1.reshape(1, 3)
    
    if len(lla_2.shape) == 1:
        lla_2 = lla_2.reshape(1, 3)
    
    lat_1 = lla_1[:, [0]]
    lon_1 = lla_1[:, [1]]
    alt_1 = lla_1[:, [2]]

    lat_2 = lla_2[:, [0]]
    lon_2 = lla_2[:, [1]]
    alt_2 = lla_2[:, [2]]

    if angle_unit == pilotUtils.DEGREES:
        lat_1 = deg2rad(lat_1)
        lon_1 = deg2rad(lon_1)

        lat_2 = deg2rad(lat_2)
        lon_2 = deg2rad(lon_2)

    dist   = distanceLla(lla_1, lla_2, angle_unit)
    height = alt_2 - alt_1

    return rad2deg(arctan2(height, dist))

def elevationNed(_ned_1: np.ndarray,
                 _ned_2: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate the elevation angle between two NED coordinates.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _ned_1
        Nx3 First NED coordinate (altitude in meters)
    _ned_2
        Nx3 Second NED coordinate (altitude in meters)

    Returns:
    --------
    elevation
        Nx1 elevation angle between the two given NED coordinates
    '''
    
    ned_1 = _ned_1.copy()
    ned_2 = _ned_2.copy()
    
    inputs.assert3Vec(ned_1)
    inputs.assert3Vec(ned_2)
    
    if len(ned_1.shape) == 1:
        ned_1 = ned_1.reshape(1, 3)
    
    if len(ned_2.shape) == 1:
        ned_2 = ned_2.reshape(1, 3)
    
    d_1 = -ned_1[:, [2]]
    d_2 = -ned_2[:, [2]]

    dist   = distanceNed(ned_1, ned_2)
    height = d_2 - d_1

    return rad2deg(arctan2(height, dist))

def LDAE2lla(_lla:       np.ndarray,
             _dist:      np.ndarray,
             _azimuth:   np.ndarray,
             _elevation: np.ndarray,
             angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate a LLA coordinate based on a given LLA coordinate, distance,
    azimuth, and elevation angle.

    http://www.movable-type.co.uk/scripts/latlong.html
    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _lla
        Nx3 LLA coordinate (altitude in meters)
    _dist
        1xN or Nx1 "As the crow flies" distance between the two
        LLA coordinates in meters
    _azimuth
        1xN or Nx1 Azimuth angle between the two LLA coordinates
    _elevation
        1xN or Nx1 Elevation angle between the two LLA coordinates
    angle_unit
        Unit of the latitude, longitude, azimuth, and
        elevation angles (True for rad and False for degrees)

    Returns:
    --------
    new_lla
        Nx3 New LLA coordinate (altitude in meters)
    '''
    
    lla = _lla.copy()
    
    inputs.assert3Vec(lla)
    
    if type(_dist) is not np.ndarray:
        dist = np.array([_dist])
    else:
        dist = _dist.flatten()
    
    if type(_azimuth) is not np.ndarray:
        azimuth = np.array([_azimuth])
    else:
        azimuth = _azimuth.flatten()
    
    if type(_elevation) is not np.ndarray:
        elevation = np.array([_elevation])
    else:
        elevation = _elevation.flatten()
    
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)
    
    lat = lla[:, [0]]
    lon = lla[:, [1]]
    alt = lla[:, [2]]

    if angle_unit == pilotUtils.DEGREES:
        lat = deg2rad(lat)
        lon = deg2rad(lon)

        azimuth   = deg2rad(azimuth)
        elevation = deg2rad(elevation)

    radius   = earth.earthAzimRad(lla, _azimuth, angle_unit) # TODO: Add altitude?
    adj_dist = dist / radius

    lat_2 = arcsin(sin(lat) * cos(adj_dist) + cos(lat) * sin(adj_dist) * cos(azimuth))
    lon_2 = lon + arctan2(sin(azimuth) * sin(adj_dist) * cos(lat),
                          cos(adj_dist) - sin(lat) * sin(lat_2))

    if angle_unit == pilotUtils.DEGREES:
        new_lla = np.hstack([rad2deg(lat_2),
                             rad2deg(lon_2),
                             alt + (dist * tan(elevation))])
    else:
        new_lla = np.hstack([lat_2,
                             lon_2,
                             alt + (dist * tan(elevation))])

    return new_lla

def NDAE2ned(_ned:       np.ndarray,
             _dist:      np.ndarray,
             _azimuth:   np.ndarray,
             _elevation: np.ndarray,
             angle_unit: bool=False) -> np.ndarray:
    '''
    Description:
    ------------
    Calculate a NED coordinate based on a given NED coordinate, distance,
    azimuth, and elevation angle.

    https://en.wikipedia.org/wiki/Geographic_coordinate_system

    Arguments:
    ----------
    _ned
        Nx3 NED coordinate in meters
    _dist
        1xN or Nx1 Horizontal distance between the two
        NED coordinates in meters
    _azimuth
        1xN or Nx1 Azimuth angle between the two NED coordinates
    _elevation
        1xN or Nx1 Elevation angle between the two NED coordinates
    angle_unit
        Unit of the azimuth and elevation angles (True for rad and False for degrees)

    Returns:
    --------
    new_ned
        Nx3 New NED coordinate in meters
    '''
    
    ned = _ned.copy()
    
    inputs.assert3Vec(ned)
    
    if type(_dist) is not np.ndarray:
        dist = np.array([_dist])
    else:
        dist = _dist.flatten()
    
    if type(_azimuth) is not np.ndarray:
        azimuth = np.array([_azimuth])
    else:
        azimuth = _azimuth.flatten()
    
    if type(_elevation) is not np.ndarray:
        elevation = np.array([_elevation])
    else:
        elevation = _elevation.flatten()
    
    if len(lla.shape) == 1:
        lla = lla.reshape(1, 3)
    
    n = ned[:, [0]]
    e = ned[:, [1]]
    d = ned[:, [2]]

    if angle_unit == pilotUtils.DEGREES:
        azimuth   = deg2rad(azimuth)
        elevation = deg2rad(elevation)

    new_ned = np.hstack([n + (dist * cos(azimuth)),
                         e + (dist * sin(azimuth)),
                         d + (dist * tan(elevation))])

    return new_ned

def intersectLla(_lla_1:    np.ndarray,
                 bearing_1: np.ndarray,
                 _lla_2:    np.ndarray,
                 bearing_2: np.ndarray) -> np.ndarray:
    '''
    Credits:
        - http://www.movable-type.co.uk/scripts/latlong.html
    
    Given two points and two bearings, find the great circle intersection coordinate
    
    Parameters
    ----------
    lla_1
        Nx3 First LLA coordinate (altitude in meters)
    bearing_1
        First point's bearing to intersection point (degrees)
    lla_2
        Nx3 Second LLA coordinate (altitude in meters)
    bearing_2
        Second point's bearing to intersection point (degrees)
    
    Returns
    -------
    np.ndarray
        Latitude and longitude in DD of the intersection point -> [lat (dd), lon (dd)]
    '''
    
    lla_1 = _lla_1.copy()
    lla_2 = _lla_2.copy()
    
    inputs.assert3Vec(lla_1)
    inputs.assert3Vec(lla_2)
    
    if len(lla_1.shape) == 1:
        lla_1 = lla_1.reshape(1, 3)
    
    if len(lla_2.shape) == 1:
        lla_2 = lla_2.reshape(1, 3)
    
    if type(bearing_1) is not np.ndarray:
        brng_1 = np.array([[bearing_1]])
    else:
        brng_1 = bearing_1.flatten()[:, np.newaxis]
    
    if type(bearing_2) is not np.ndarray:
        brng_2 = np.array([[bearing_2]])
    else:
        brng_2 = bearing_2.flatten()[:, np.newaxis]
    
    brng_1 = deg2rad(bearing_1)
    brng_2 = deg2rad(bearing_2)
    
    lat_1 = lla_1[:, [0]]
    lon_1 = lla_1[:, [1]]
    alt_1 = lla_1[:, [2]]

    lat_2 = lla_2[:, [0]]
    lon_2 = lla_2[:, [1]]
    alt_2 = lla_2[:, [2]]
    
    del_lat = lat_2 - lat_1
    del_lon = lon_2 - lon_1
    
    avg_alt = (alt_1 + alt_2) / 2.0
    
    del_12  = 2 * arcsin(sqrt(sin(del_lat / 2.0)**2 + (cos(lat_1) * cos(lat_2) * (sin(del_lon / 2.0)**2))))
    theta_a = arccos((sin(lat_2) - (sin(lat_1) * cos(del_12))) / (sin(del_12) * cos(lat_1)))
    theta_b = arccos((sin(lat_1) - (sin(lat_2) * cos(del_12))) / (sin(del_12) * cos(lat_2)))
    
    if sin(del_lon) > 0:
        theta_12 = theta_a
        theta_21 = (2 * pi) - theta_b
    
    else:
        theta_12 = (2 * pi) - theta_a
        theta_21 = theta_b
    
    alpha_1 = brng_1   - theta_12
    alpha_2 = theta_21 - brng_2
    
    alpha_3    = arccos((-cos(alpha_1) * cos(alpha_2)) + (sin(alpha_1) * sin(alpha_2) * cos(del_12)))
    del_13     = arctan2(sin(del_12)   * sin(alpha_1)  * sin(alpha_2),   cos(alpha_2) + (cos(alpha_1) * cos(alpha_3)))
    lat_3      = arcsin((sin(lat_1)    * cos(del_13))  + (cos(lat_1)   * sin(del_13)  * cos(brng_1)))
    del_lon_13 = arctan2(sin(brng_1)   * sin(del_13)   * cos(lat_1),     cos(del_13)  - (sin(lat_1)   * sin(lat_3)))
    lon_3      = lon_1 + del_lon_13
    
    # Dist int to lla_1
    dist_to_lla1 = distanceLla(_lla_1     = np.hstack([rad2deg(lat_3), rad2deg(lon_3), avg_alt]),
                               _lla_2     = lla_1,
                               angle_unit = False)
    
    # Dist int to lla_2
    dist_to_lla2 = distanceLla(_lla_1     = np.hstack([rad2deg(lat_3), rad2deg(lon_3), avg_alt]),
                               _lla_2     = lla_2,
                               angle_unit = False)
    
    # Weighted avg
    total_dist = dist_to_lla1 + dist_to_lla2
    avg_alt    = ((total_dist / dist_to_lla1) * alt_2) + ((total_dist / dist_to_lla2) * alt_1)
    
    return np.hstack([rad2deg(lat_3), rad2deg(lon_3), avg_alt])

def arc_angle(lla_1:      np.ndarray,
              lla_2:      np.ndarray,
              angle_unit: bool=False) -> np.ndarray:
    '''
    Find Arc angle between geodetic coordinates
    
    Parameters
    ----------
    lla_1
        Nx3 First LLA coordinate (altitude in meters)
    lla_2
        Nx3 Second LLA coordinate (altitude in meters)
    angle_unit
        Unit of the latitude, longitude, and elevation
        angles (True for rad and False for degrees)
    
    Returns
    -------
    np.ndarray
        Arc angle between the two coordinates
    '''
    
    dist = distanceLla(_lla_1     = lla_1,
                       _lla_2     = lla_2,
                       angle_unit = angle_unit)
    
    azimuth = bearingLla(_lla_1     = lla_1,
                         _lla_2     = lla_2,
                         angle_unit = angle_unit)
    
    earth_rad = earth.earthAzimRad(_lla       = lla_1,
                                   _azimuth   = azimuth,
                                   angle_unit = angle_unit) # TODO: Add altitude?
    
    return dist / earth_rad
