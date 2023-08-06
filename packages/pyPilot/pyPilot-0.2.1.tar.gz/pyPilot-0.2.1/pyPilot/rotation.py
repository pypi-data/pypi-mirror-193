import sys
from os.path import dirname

import numpy as np
from numpy import deg2rad, rad2deg, sin, cos, arcsin, arccos, arctan2
from scipy.spatial.transform import Rotation as R

SRC_DIR = dirname(__file__)
sys.path.append(SRC_DIR)

import inputs
import pilotUtils


def angle2dcm(_angles:           np.ndarray,
              angle_unit:        bool=False,
              NED_to_body:       bool=True,
              rotation_sequence: int=321) -> np.ndarray:
    '''
    Description:
    ------------
    This function converts a vector of euler angles into a Direction Cosine
    Matrix (DCM) given a rotation and frame sequence. In the case of this
    function, the returned DCM maps vectors from one coordinate frame (either
    North-East-Down (NED) or body frame) into the other. This is done by
    multiplying the DCM with the vector to be rotated: v_body = DCM * v_NED.

    https://en.wikipedia.org/wiki/Rotation_matrix
    https://en.wikipedia.org/wiki/Axes_conventions
    https://en.wikipedia.org/wiki/Euler_angles
    
    Arguments:
    ----------
    angles
        Nx3 Vector of euler angles to describe the rotation -> [roll, pitch, yaw]
    angle_unit
        Unit of the euler angles (True for rad and False for degrees)
    NED_to_body
         Rotate either to or from the NED frame (True for from and False for to the NED frame)
    rotation_sequence
        The order in which the euler angles are applied
        to the rotation. 321 is the standard rotation
        sequence for aerial navigation
    
    Returns:
    --------
    dcm
        Nx3x3 Direction cosine matrix (rotation matix)
    '''
    
    angles = _angles.copy()
    
    inputs.assert3Vec(angles)
    
    if len(angles.shape) == 1:
        angles = angles.reshape(1, 3)
    
    num_angles = angles.shape[0]
    
    if angle_unit == pilotUtils.DEGREES:
        roll  = deg2rad(angles[:, 0])
        pitch = deg2rad(angles[:, 1])
        yaw   = deg2rad(angles[:, 2])
    else:
        roll  = angles[:, 0]
        pitch = angles[:, 1]
        yaw   = angles[:, 2]
    
    # For a single angle, DCM R1 would be:
    # R1 = np.array([[1,          0,         0],
    #                [0,  cos(roll), sin(roll)],
    #                [0, -sin(roll), cos(roll)]])
    
    R1 = np.zeros((num_angles, 3, 3))
    R1[:, 0, 0] = 1
    R1[:, 1, 1] = cos(roll)
    R1[:, 1, 2] = sin(roll)
    R1[:, 2, 1] = -sin(roll)
    R1[:, 2, 2] = cos(roll)

    # For a single angle, DCM R2 would be:
    # R2 = np.array([[cos(pitch), 0, -sin(pitch)],
    #                [0,          1,           0],
    #                [sin(pitch), 0,  cos(pitch)]])
    
    R2 = np.zeros((num_angles, 3, 3))
    R2[:, 0, 0] = cos(pitch)
    R2[:, 0, 2] = -sin(pitch)
    R2[:, 1, 1] = 1
    R2[:, 2, 0] = sin(pitch)
    R2[:, 2, 2] = cos(pitch)

    # For a single angle, DCM R3 would be:
    # R3 = np.array([[ cos(yaw), sin(yaw), 0],
    #                [-sin(yaw), cos(yaw), 0],
    #                [ 0,        0,        1]])
    
    R3 = np.zeros((num_angles, 3, 3))
    R3[:, 0, 0] = cos(yaw)
    R3[:, 0, 1] = sin(yaw)
    R3[:, 1, 0] = -sin(yaw)
    R3[:, 1, 1] = cos(yaw)
    R3[:, 2, 2] = 1

    if rotation_sequence == 321:
        dcms = R1 @ R2 @ R3
    elif rotation_sequence == 312:
        dcms = R2 @ R1 @ R3
    elif rotation_sequence == 231:
        dcms = R1 @ R3 @ R2
    elif rotation_sequence == 213:
        dcms = R3 @ R1 @ R2
    elif rotation_sequence == 132:
        dcms = R2 @ R3 @ R1
    elif rotation_sequence == 123:
        dcms = R3 @ R2 @ R1
    else:
        dcms = R1 @ R2 @ R3

    if not NED_to_body:
        return np.transpose(dcms, axes=(0, 2, 1))

    return dcms

def dcm2angle(_dcm:              np.ndarray,
              angle_unit:        bool=False,
              NED_to_body:       bool=True,
              rotation_sequence: int=321) -> np.ndarray:
    '''
    Description:
    ------------
    This function converts a Direction Cosine Matrix (DCM) into the 
    corresponding euler angles.

    https://en.wikipedia.org/wiki/Rotation_matrix
    https://en.wikipedia.org/wiki/Axes_conventions
    https://en.wikipedia.org/wiki/Euler_angles

    Arguments:
    ----------
    _dcm
        Nx3x3 Direction cosine matrix (rotation matix)
    angle_unit
        Unit of the euler angles (True for rad and False for degrees)
    NED_to_body
         Rotate either to or from the NED frame (True for from and False for to the NED frame)
    rotation_sequence
        The order in which the euler angles are applied
        to the rotation. 321 is the standard rotation
        sequence for aerial navigation

    Returns:
    --------
    angles
        Nx3 Vector of euler angles to describe the rotation -> [roll, pitch, yaw]
    '''
    
    dcm = _dcm.copy()
    
    inputs.assertDCM(dcm)
    
    if len(dcm.shape) < 3:
        dcm = dcm.reshape(1, 3, 3)
    
    if not NED_to_body:
        dcm = np.transpose(dcm, axes=(0, 2, 1))
    
    if rotation_sequence == 321:
        angles = np.hstack([arctan2(dcm[:, 1, [2]], dcm[:, 2, [2]]),  # Roll
                           -arcsin(dcm[:,  0, [2]]),                  # Pitch
                            arctan2(dcm[:, 0, [1]], dcm[:, 0, [0]])]) # Yaw
    
    elif rotation_sequence == 312:
        angles = np.hstack([arcsin(dcm[:,  1, [2]]),                  # Roll
                           -arctan2(dcm[:, 0, [2]], dcm[:, 2, [2]]),  # Pitch
                           -arctan2(dcm[:, 1, [0]], dcm[:, 1, [1]])]) # Yaw
    
    elif rotation_sequence == 231:
        angles = np.hstack([ arctan2(dcm[:, 2, [1]], dcm[:, 1, [1]]), # Roll
                            -arctan2(dcm[:, 0, [2]], dcm[:, 0, [0]]), # Pitch
                             arcsin(dcm[:,  0, [1]])])                # Yaw
    
    elif rotation_sequence == 213:
        angles = np.hstack([-arcsin(dcm[:,  2, [1]]),                  # Roll
                             arctan2(dcm[:, 2, [0]], dcm[:, 2, [2]]),  # Pitch
                             arctan2(dcm[:, 0, [1]], dcm[:, 1, [1]])]) # Yaw
    
    elif rotation_sequence == 132:
        angles = np.hstack([arctan2(dcm[:, 1, [2]], dcm[:, 1, [1]]), # Roll
                            arctan2(dcm[:, 2, [0]], dcm[:, 0, [0]]), # Pitch
                           -arcsin(dcm[:,  1, [0]])])                # Yaw
    
    elif rotation_sequence == 123:
        angles = np.hstack([-arctan2(dcm[:, 2, [1]], dcm[:, 2, [2]]),  # Roll
                             arcsin(dcm[:,  2, [0]]),                  # Pitch
                            -arctan2(dcm[:, 1, [0]], dcm[:, 0, [0]])]) # Yaw

    if angle_unit == pilotUtils.DEGREES:
        angles = rad2deg(angles)

    return angles

def angle2quat(angles:            np.ndarray,
               angle_unit:        bool=False,
               NED_to_body:       bool=True,
               rotation_sequence: int=321) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a sequence of euler angles to an equivalent unit quaternion.

    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
    https://en.wikipedia.org/wiki/Axes_conventions
    https://en.wikipedia.org/wiki/Euler_angles

    Arguments:
    ----------
    angles
        Nx3 Vector of euler angles to describe the rotation -> [roll, pitch, yaw]
    angle_unit
        Unit of the euler angles (True for rad and False for degrees)
    NED_to_body
         Rotate either to or from the NED frame (True for from and False for to the NED frame)
    rotation_sequence
        The order in which the euler angles are applied
        to the rotation. 321 is the standard rotation
        sequence for aerial navigation

    Returns:
    --------
    np.ndarray
        Nx4 Quaternion that describes the rotation -> [x, y, z, w]
    '''
    
    r = R.from_matrix(angle2dcm(angles, angle_unit, NED_to_body, rotation_sequence))
    
    return r.as_quat()

def quat2angle(quat:              np.ndarray,
               angle_unit:        bool=False,
               NED_to_body:       bool=True,
               rotation_sequence: int=321) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a unit quaternion to the equivalent sequence of euler angles
    about the rotation_sequence axes.

    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
    https://en.wikipedia.org/wiki/Axes_conventions
    https://en.wikipedia.org/wiki/Euler_angles

    Arguments:
    ----------
    quat
        Nx4 Quaternion that describes the rotation -> [x, y, z, w]
    angle_unit
        Unit of the euler angles (True for rad and False for degrees)
    NED_to_body
         Rotate either to or from the NED frame (True for from and False for to the NED frame)
    rotation_sequence
        The order in which the euler angles are applied
        to the rotation. 321 is the standard rotation
        sequence for aerial navigation

    Returns:
    --------
    np.ndarray
        Nx3 Vector of euler angles to describe the rotation -> [roll, pitch, yaw]
    '''
    
    inputs.assert4Vec(quat)
    
    r = R.from_quat(quat)

    return dcm2angle(r.as_matrix(), angle_unit, NED_to_body, rotation_sequence)

def quat2dcm(quat: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a single unit quaternion to one DCM.

    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
    https://en.wikipedia.org/wiki/Rotation_matrix
    https://en.wikipedia.org/wiki/Axes_conventions

    Arguments:
    ----------
    quat
        Nx4 Quaternion that describes the rotation

    Returns:
    --------
    np.ndarray
        Nx3x3 DCM that rotates vectors from one coordinate frame to the other
    '''
    
    inputs.assert4Vec(quat)
    
    r = R.from_quat(quat)
    
    return r.as_matrix()

def dcm2quat(dcm: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a DCM to a unit quaternion.

    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
    https://en.wikipedia.org/wiki/Rotation_matrix
    https://en.wikipedia.org/wiki/Axes_conventions

    Arguments:
    ----------
    dcm
        Nx3x3 Direction cosine matrix (rotation matix)

    Returns:
    --------
    np.ndarray
        Nx4 Quaternion that describes the rotation -> [x, y, z, w]
    '''
    
    inputs.assertDCM(dcm)
    
    r = R.from_matrix(dcm)
    
    return r.as_quat()

def vec2dcm(vec: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a Rodrigues rotation vector to a DCM.

    **NOTE: The Rodrigues vector's rotation angle must be in RADIANS.**

    https://courses.cs.duke.edu/fall13/compsci527/notes/rodrigues.pdf
    https://en.wikipedia.org/wiki/Rotation_matrix

    Arguments:
    ----------
    vec
        Nx3 Rodrigues rotation vector

    Returns:
    --------
    np.ndarray
        Nx3x3 Direction cosine matrix (rotation matix)
    '''
    
    inputs.assert3Vec(vec)

    r = R.from_rotvec(vec)
    
    return r.as_matrix()

def dcm2vec(dcm: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a DCM to a Rodrigues rotation vector.

    https://courses.cs.duke.edu/fall13/compsci527/notes/rodrigues.pdf
    https://en.wikipedia.org/wiki/Rotation_matrix

    Arguments:
    ----------
    dcm
        Nx3x3 Direction cosine matrix (rotation matix)

    Returns:
    --------
    np.ndarray
        Nx3 Rodrigues rotation vector (rotation angle is in RADIANS)
    '''
    
    inputs.assertDCM(dcm)
    
    r = R.from_matrix(dcm)
    
    return r.as_rotvec()

def vec2quat(vec: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a Rodrigues rotation vector to a quaternion.

    **NOTE: The Rodrigues vector's rotation angle must be in RADIANS.**

    https://courses.cs.duke.edu/fall13/compsci527/notes/rodrigues.pdf
    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation

    Arguments:
    ----------
    vec
        Nx3 Rodrigues rotation vector

    Returns:
    --------
    np.ndarray
        Nx4 Quaternion that describes the rotation -> [x, y, z, w]
    '''
    
    inputs.assert3Vec(vec)
    
    r = R.from_rotvec(vec)
    
    return r.as_quat()

def quat2vec(quat: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a quaternion to a Rodrigues rotation vector.

    https://courses.cs.duke.edu/fall13/compsci527/notes/rodrigues.pdf
    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation

    Arguments:
    ----------
    quat
        Nx4 Quaternion that describes the rotation -> [x, y, z, w]

    Returns:
    --------
    vec
        Nx3 Rodrigues rotation vector (rotation angle is in RADIANS)
    '''
    
    inputs.assert4Vec(quat)
    
    r = R.from_quat(quat)
    
    return r.as_rotvec()

def vec2angle(vec:               np.ndarray,
              angle_unit:        bool=False,
              NED_to_body:       bool=True,
              rotation_sequence: int=321) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a Rodrigues rotation vector to a vector of euler angles.

    **NOTE: The Rodrigues vector's rotation angle must be in RADIANS.**

    https://courses.cs.duke.edu/fall13/compsci527/notes/rodrigues.pdf
    https://en.wikipedia.org/wiki/Axes_conventions
    https://en.wikipedia.org/wiki/Euler_angles

    Arguments:
    ----------
    vec
        Nx3 Rodrigues rotation vector
    angle_unit
        Unit of the euler angles (True for rad and False for degrees)
    NED_to_body
         Rotate either to or from the NED frame (True for from and False for to the NED frame)
    rotation_sequence
        The order in which the euler angles are applied
        to the rotation. 321 is the standard rotation
        sequence for aerial navigation

    Returns:
    --------
    np.ndarray
        Nx3 Vector of euler angles
    '''
    
    return dcm2angle(vec2dcm(vec),
                     angle_unit,
                     NED_to_body,
                     rotation_sequence)

def angle2vec(angles:            np.ndarray,
              angle_unit:        bool=False,
              NED_to_body:       bool=True,
              rotation_sequence: int=321) -> np.ndarray:
    '''
    Description:
    ------------
    Convert a vector of euler angles to a Rodrigues rotation vector.

    https://courses.cs.duke.edu/fall13/compsci527/notes/rodrigues.pdf
    https://en.wikipedia.org/wiki/Axes_conventions
    https://en.wikipedia.org/wiki/Euler_angles

    Arguments:
    ----------
    angles
        Nx3 Vector of euler angles
    angle_unit
        Unit of the euler angles (True for rad and False for degrees)
    NED_to_body
         Rotate either to or from the NED frame (True for from and False for to the NED frame)
    rotation_sequence
        The order in which the euler angles are applied
        to the rotation. 321 is the standard rotation
        sequence for aerial navigation

    Returns:
    --------
    np.ndarray
        Nx3 Rodrigues rotation vector (rotation angle is in RADIANS)
    '''
    
    return dcm2vec(angle2dcm(angles, angle_unit, NED_to_body, rotation_sequence))

def quatMult(_quat_1: np.ndarray,
             _quat_2: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Apply a quaternion multiplication (assumes quaternions have
    the form -> [x, y, z, w])
    
    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation

    Arguments:
    ----------
    _quat_1
        Nx4 First set of quaternions to apply in the multiplication -> [x, y, z, w]
    _quat_2
        Nx4 Second set of quaternions to apply in the multiplication -> [x, y, z, w]
    
    Returns:
    --------
    np.ndarray
        Nx4 Quaternions from multiplying two sets of quaternions together -> [x, y, z, w]
    '''
    
    inputs.assert4Vec(_quat_1)
    inputs.assert4Vec(_quat_2)
    
    quat_1 = _quat_1.copy()
    quat_2 = _quat_2.copy()
    
    if len(quat_1.shape) == 1:
        quat_1 = quat_1.reshape(1, 4)
    
    if len(quat_2.shape) == 1:
        quat_2 = quat_2.reshape(1, 4)
    
    a1 = quat_1[:, 3]
    b1 = quat_1[:, 0]
    c1 = quat_1[:, 1]
    d1 = quat_1[:, 2]
    
    a2 = quat_2[:, 3]
    b2 = quat_2[:, 0]
    c2 = quat_2[:, 1]
    d2 = quat_2[:, 2]
    
    new_quat = np.zeros(quat_1.shape)
    
    new_quat[:, 3] = a1*a2 - b1*b2 - c1*c2 - d1*d2
    new_quat[:, 0] = a1*b2 + b1*a2 + c1*d2 - d1*c2
    new_quat[:, 1] = a1*c2 - b1*d2 + c1*a2 + d1*b2
    new_quat[:, 2] = a1*d2 + b1*c2 - c1*b2 + d1*a2
    
    return new_quat

def quatInv(_quat: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Find the inverse quaternion
    
    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation

    Arguments:
    ----------
    _quat
        Nx3 Quaternions to take the inverse of -> [x, y, z, w]
    
    Returns:
    --------
    quat
        Nx3 Inverses of the input quaternions -> [x, y, z, w]
    '''
    
    inputs.assert4Vec(_quat)
    
    quat = _quat.copy()
    
    if len(quat.shape) == 1:
        quat = quat.reshape(1, 4)
    
    quat[:, :3] = -quat[:, :3]
    
    return quat

def quatRotVec(_quat: np.ndarray,
               _vec:  np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Rotate a vector using the given quaternion
    
    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation

    Arguments:
    ----------
    _quat
        Nx4 Quaternion that describes the desired rotation -> [x, y, z, w]
    _vec
        Nx3 Vector to be rotated
    
    Returns:
    --------
    new_vec
        Nx3 Rotated vector
    '''
    
    inputs.assert4Vec(_quat)
    
    quat = _quat.copy()
    
    if len(quat.shape) == 1:
        quat = quat.reshape(1, 4)
    
    invQuat = quatInv(quat)
    
    vec = _vec.copy()
    
    if len(_vec.shape) == 1:
        vec = vec.reshape(1, 3)
    
    vec = np.hstack([vec,
                     np.zeros((vec.shape[0], 1))])
    
    new_vec = quatMult(quatMult(quat, vec), invQuat)[:, :3]
    
    return new_vec

def interQuat(_quat_1: np.ndarray,
              _quat_2: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Find the intermediate quaternion that represents the rotation from
    one orientation to a second one (both also represented by quaternions)
    
    https://stackoverflow.com/a/22167097/9860973
    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation

    Arguments:
    ----------
    _quat_1
        Nx4 First set of quaternions -> [x, y, z, w]
    _quat_2
        Nx4 Second set of quaternions -> [x, y, z, w]
    
    Returns:
    --------
    int_quat
        Nx4 intermediate quaternions that rotates from the first set of
        quaternions to the second set -> [x, y, z, w]
    '''
    
    inputs.assert4Vec(_quat_1)
    inputs.assert4Vec(_quat_2)
    
    quat_1 = _quat_1.copy()
    quat_2 = _quat_2.copy()
    
    if len(quat_1.shape) == 1:
        quat_1 = quat_1.reshape(1, 4)
    
    if len(quat_2.shape) == 1:
        quat_2 = quat_2.reshape(1, 4)
    
    invQuat_1 = quatInv(quat_1)
    int_quat  = quatMult(quat_2, invQuat_1)
    
    return int_quat

def quatParts(_quat:      np.ndarray,
              angle_unit: bool=False) -> tuple:
    '''
    Description:
    ------------
    Break out a given quaternion into the rotation angle
    and rotation vector
    
    https://eater.net/quaternions
    https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation

    Arguments:
    ----------
    _quat
        Nx4 Quaternion to find the rotation angle and rotation vector from -> [x, y, z, w]
    angle_unit
        Unit of the quaternion angle (True for rad and False for degrees)
    
    Returns:
    --------
    tuple
        Quaternion rotation angle and vector -> (Nx1 theta, Nx3 vector)
    '''
    
    inputs.assert4Vec(_quat)
    
    quat = _quat.copy()
    
    if len(quat.shape) == 1:
        quat.reshape(1, 4)
    
    theta = 2.0 * arccos(quat[:, 3])
    vecs  = quat[:, :3] / sin(theta / 2.0)
    
    if angle_unit is pilotUtils.DEGREES:
        theta = rad2deg(theta)
    
    return (theta, vecs)

def dcmRates(_dcm:           np.ndarray,
             _angular_rates: np.ndarray,
             angle_unit:     bool=False) -> np.ndarray:
    '''
    https://www.vectornav.com/resources/inertial-navigation-primer/math-fundamentals/math-attitudetran
    '''
    
    inputs.assertDCM(_dcm)
    inputs.assert3Vec(_angular_rates)
    
    dcm           = _dcm.copy()
    angular_rates = _angular_rates.copy()
    
    if len(dcm.shape) == 2:
        dcm = dcm.reshape(1, 3, 3)
    
    if len(angular_rates.shape) == 1:
        angular_rates = angular_rates.reshape(1, 3)
    
    if angle_unit is pilotUtils.DEGREES:
        angular_rates = deg2rad(angular_rates)
    
    return -pilotUtils.skew(angular_rates) @ dcm

def quatRates(_quat:          np.ndarray,
              _angular_rates: np.ndarray,
              angle_unit:     bool=False) -> np.ndarray:
    '''
    https://www.vectornav.com/resources/inertial-navigation-primer/math-fundamentals/math-attitudetran
    '''
    
    inputs.assert4Vec(_quat)
    inputs.assert3Vec(_angular_rates)
    
    quat          = _quat.copy()
    angular_rates = _angular_rates.copy()
    
    if len(quat.shape) == 1:
        quat = quat.reshape(1, 4)
    
    if len(angular_rates.shape) == 1:
        angular_rates = angular_rates.reshape(1, 3)
    
    if angle_unit is pilotUtils.DEGREES:
        angular_rates = deg2rad(angular_rates)
    
    return quatRotVec(quat, angular_rates) / 2.0

def angleRates(_angles:           np.ndarray,
               _angular_rates:    np.ndarray,
               angle_unit:        bool=False,
               NED_to_body:       bool=True,
               rotation_sequence: int=321) -> np.ndarray:
    '''
    https://www.vectornav.com/resources/inertial-navigation-primer/math-fundamentals/math-attitudetran
    '''
    
    inputs.assert3Vec(_angles)
    inputs.assert3Vec(_angular_rates)
    
    angles        = _angles.copy()
    angular_rates = _angular_rates.copy()
    
    if len(angles.shape) == 1:
        angles = angles.reshape(1, 3)
    
    if len(angular_rates.shape) == 1:
        angular_rates = angular_rates.reshape(1, 3)
    
    if angle_unit is pilotUtils.DEGREES:
        angles        = deg2rad(angles)
        angular_rates = deg2rad(angular_rates)
    
    pitch = angles[:, 1]
    
    angles[:, 3] = 0
    
    return (angle2dcm(angles,
                      pilotUtils.RADIANS,
                      NED_to_body,
                      rotation_sequence) @ angular_rates) / cos(pitch)