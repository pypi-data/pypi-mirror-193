import sys
from os.path import dirname

import numpy as np
from numpy import rad2deg

SRC_DIR = dirname(__file__)
sys.path.append(SRC_DIR)

import coordinate
import inputs
import pilotUtils
import rotation


def poseMat(_dcm: np.ndarray,
            _t:   np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Create a 4x4 pose matrix that can be used to apply an affine transform of a
    3 dimensional vector/point from one coordinate frame to another. The two
    coordinate frames do not need to be colocated.

    https://en.wikipedia.org/wiki/Affine_transformation

    Arguments:
    ----------
    _dcm
        Nx3x3 Direction cosine matrix that describes the rotation
        between the two coordinate frames
    _t
        Nx3 Translation vector between the origins of the two
        coordinate frames (unit of distance is arbitrary - 
        up to the user to decide)

    Returns:
    --------
    poseMatrix
        Nx4x4 pose matrix for affine coordinate frame transforms
    '''
    
    dcm = _dcm.copy()
    t   = _t.copy()
    
    inputs.assertDCM(dcm)
    inputs.assert3Vec(t)
    
    if len(dcm.shape) < 3:
        dcm = dcm.reshape(1, 3, 3)
    
    if len(t.shape) < 3:
        t = t.reshape(1, 1, 3)

    poseMatrix = np.zeros((dcm.shape[0], 4, 4))
    
    poseMatrix[:, :3, :3] = dcm
    poseMatrix[:, :3,  3] = np.transpose(t, axes=(0, 2, 1)).squeeze()
    poseMatrix[:,  3,  3] = 1

    return poseMatrix

def pose2dcm(_poseMatrix: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Extract the DCM from a given pose matrix.

    https://en.wikipedia.org/wiki/Affine_transformation
    https://en.wikipedia.org/wiki/Rotation_matrix

    Arguments:
    ----------
    _poseMatrix
        Nx4x4 pose matrix for affine coordinate frame
        transforms

    Returns:
    --------
    dcm
        Nx3x3 DCM extracted from pose matrix
    '''
    
    poseMatrix = _poseMatrix.copy()
    
    inputs.assertPose(poseMatrix)
    
    if len(poseMatrix.shape) < 3:
        poseMatrix = poseMatrix.reshape(1, 4, 4)
    
    dcm = poseMatrix[:, :3, :3]

    return dcm

def pose2t(_poseMatrix: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Extract translation vector from a given pose matrix.

    https://en.wikipedia.org/wiki/Affine_transformation

    Arguments:
    ----------
    _poseMatrix
        Nx4x4 pose matrix for affine coordinate frame
        transforms

    Returns:
    --------
    t
        Nx3 Translation vector extracted from pose matrix
    '''
    
    poseMatrix = _poseMatrix.copy()
    
    inputs.assertPose(poseMatrix)
    
    if len(poseMatrix.shape) < 3:
        poseMatrix = poseMatrix.reshape(1, 4, 4)
    
    t = poseMatrix[:, :3, 3]

    return t

def reversePoseMat(poseMatrix: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Create a reversed 4x4 pose matrix.

    https://en.wikipedia.org/wiki/Affine_transformation

    Arguments:
    ----------
    poseMatrix
        Nx4x4 pose matrix for affine coordinate frame
        transforms

    Returns:
    --------
    inv_poseMatrix
        Nx4x4 Reversed pose matrix for affine coordinate frame
        transforms
    '''
    
    dcm = pose2dcm(poseMatrix)
    t   = pose2t(poseMatrix).T
    t   = t.reshape(t.shape[1], 3, 1)
        
    dcm_T = np.transpose(dcm, axes=(0, 2, 1))
    t_T   = np.transpose(dcm_T @ -t, axes=(0, 2, 1))

    inv_poseMatrix = poseMat(dcm_T, t_T)
    
    return inv_poseMatrix

def poseMatDeriv(_poseMatrix: np.ndarray,
                 derivType:   np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Compute the matrix derivative of the given pose matrix w.r.t the given variable.
    The possible variables include:
    * dRx - w.r.t. rotation around the x axis
    * dRy - w.r.t. rotation around the y axis
    * dRz - w.r.t. rotation around the z axis
    * dtx - w.r.t. translation along the x axis
    * dty - w.r.t. translation along the y axis
    * dtz - w.r.t. translation along the z axis

    This operation is often used when constructing Jacobian matrices for optimization
    problems (i.e. least squares/GN optimization)

    https://en.wikipedia.org/wiki/Affine_transformation
    https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant
    https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm

    Arguments:
    ----------
    _poseMatrix
        4x4 or Nx4x4 pose matrix for affine coordinate frame
        transforms
    derivType
        Variable to take the derivative w.r.t.

    Returns:
    --------
    poseMatrix
        4x4 or Nx4x4 Pose matrix derivative
    '''
    
    poseMatrix = _poseMatrix.copy()
    
    inputs.assertPose(poseMatrix)
    
    if len(poseMatrix.shape) < 3:
        poseMatrix = poseMatrix.reshape(1, 4, 4)
    
    dcm       = pose2dcm(poseMatrix)
    derivPose = np.zeros(poseMatrix.shape)
    vec       = np.zeros((poseMatrix.shape[0], 3))
    
    if derivType == pilotUtils.dRx:
        vec[:, 0] = 1
        
        derivPose[:, :2, :2] = pilotUtils.skew(vec) @ dcm

    elif derivType == pilotUtils.dRy:
        vec[:, 1] = 1
        
        derivPose[:, :2, :2] = pilotUtils.skew(vec) @ dcm

    elif derivType == pilotUtils.dRz:
        vec[:, 2] = 1
        
        derivPose[:, :2, :2] = pilotUtils.skew(vec) @ dcm

    elif derivType == pilotUtils.dtx:
        vec[:, 0] = 1
        
        tempPose = np.zeros(poseMatrix.shape)
        tempPose[:, 3, :2] = vec

        derivPose = tempPose @ poseMatrix

    elif derivType == pilotUtils.dty:
        vec[:, 1] = 1
        
        tempPose = np.zeros(poseMatrix.shape)
        tempPose[:, 3, :2] = vec

        derivPose = tempPose @ poseMatrix

    elif derivType == pilotUtils.dtz:
        vec[:, 2] = 1
        
        tempPose = np.zeros(poseMatrix.shape)
        tempPose[:, 3, :2] = vec

        derivPose = tempPose @ poseMatrix
    
    else:
        assert True == False, 'Invalid derivative type given: {}'.format(derivType)

    return derivPose

def transformPt(_poseMatrix: np.ndarray,
                _x:          np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Applies an affine transformation to vector/point x described by the given pose
    matrix. This affine transformation converts the vector/point x from it's
    initial coordinate frame to another. A common use of this function would be
    to convert a 3D point in an airplane's sensor's body frame into the airplane's
    body frame (and vice versa).

    https://en.wikipedia.org/wiki/Affine_transformation

    Arguments:
    ----------
    poseMatrix
        4x4 or Nx4x4 pose matrix for affine coordinate frame
        transforms
    x
        1x3 or Nx3 vector/point to be transformed

    Returns:
    --------
    new_x
        1x3 or Nx3 vector/point transformed to the new coordinate frame
    '''
    
    poseMatrix = _poseMatrix.copy()
    x          = _x.copy()
    
    inputs.assertPose(poseMatrix)
    inputs.assert3Vec(x)
    
    if len(poseMatrix.shape) == 2:
        poseMatrix = poseMatrix.reshape(1, 4, 4)
    
    if len(x.shape) == 1:
        x = x.reshape(1, 1, 3)
    elif len(x.shape) == 2:
        x = x.reshape(1, x.shape[0], 3)
    
    x_1 = np.ones((x.shape[0], x.shape[1], 4))
    x_1[:, :, :3] = x
    
    new_x_1 = np.transpose((poseMatrix @ np.transpose(x_1, axes=(0, 2, 1))), axes=(0, 2, 1))
    new_x   = new_x_1[:, :, :3].squeeze()

    return new_x

def payload2vehicle(pay, x):
    '''
    Transform a point/set of points/vectors from the payload to vehicle frame
    '''
    
    return transformPt(pay.v_P_p(), x).squeeze()

def vehicle2payload(pay, x):
    '''
    Transform a point/set of points/vectors from the vehicle to payload frame
    '''
    
    return transformPt(pay.p_P_v(), x).squeeze()

def sensor2vehicle(pay, sen, x):
    '''
    Transform a point/set of points/vectors from the sensor to vehicle frame
    '''
    
    return transformPt(pay.v_P_p() @ sen.p_P_s(), x).squeeze()

def vehicle2sensor(pay, sen, x):
    '''
    Transform a point/set of points/vectors from the vehicle to sensor frame
    '''
    
    return transformPt(sen.s_P_p() @ pay.p_P_v(), x).squeeze()

def sensor2payload(pay, sen, x):
    '''
    Transform a point/set of points/vectors from the sensor to payload frame
    '''
    
    return transformPt(sen.p_P_s(), x).squeeze()

def payload2sensor(pay, sen, x):
    '''
    Transform a point/set of points/vectors from the payload to sensor frame
    '''
    
    return transformPt(sen.s_P_p(), x).squeeze()


class vehicle_pose():
    def __init__(self, id):
        self._vehicleID = id
        
        self._lla = np.zeros(3) # dd, dd, m

        self._e_t_e_v = np.zeros(3) # translation vector (in m) from ECEF frame to vehicle's local level/NED frame in the ECEF frame
        self._n_R_e   = np.eye(3)   # dcm from ECEF frame to vehicle's local level/NED frame
        self._v_R_n   = np.eye(3)   # dcm from vehicle's local level/NED frame to vehicle's body frame
        self._n_P_e   = np.eye(4)   # pose matrix that maps points from the ECEF frame to the vehicle's local level/NED frame https://en.wikipedia.org/wiki/Affine_transformation
        self._v_P_e   = np.eye(4)   # pose matrix that maps points from the ECEF frame to the vehicle's body frame https://en.wikipedia.org/wiki/Affine_transformation
    
    def vehicleID(self):
        return self._vehicleID
    
    def e_t_e_v(self):
        '''
        Translation vector from the ECEF to vehicle frame resolved in the ECEF frame
        '''
        
        return self._e_t_e_v
    
    def v_t_v_e(self):
        '''
        Translation vector from the vehicle to ECEF frame resolved in the vehicle frame
        '''
        
        return -self._e_t_e_v
    
    def n_R_e(self):
        '''
        Rotation DCM from the ECEF to navigation frame
        '''
        
        return self._n_R_e
    
    def e_R_n(self):
        '''
        Rotation DCM from the navigation to ECEF frame
        '''
        
        return self._n_R_e.T
    
    def v_R_n(self):
        '''
        Rotation DCM from the navigation to vehicle frame
        '''
        
        return self._v_R_n
    
    def n_R_v(self):
        '''
        Rotation DCM from the vehicle to navigation frame
        '''
        
        return self._v_R_n.T
    
    def n_P_e(self):
        '''
        Pose matrix from the ECEF to navigation frame
        '''
        
        return self._n_P_e
    
    def e_P_n(self):
        '''
        Pose matrix from the navigation to ECEF frame
        '''
        
        return reversePoseMat(self._n_P_e).squeeze()
    
    def v_P_e(self):
        '''
        Pose matrix from the ECEF to vehicle frame
        '''
        
        return self._v_P_e
    
    def e_P_v(self):
        '''
        Pose matrix from the vehicle to ECEF frame
        '''
        
        return reversePoseMat(self._v_P_e).squeeze()
    
    def lla(self, angle_unit=pilotUtils.DEGREES):
        '''
        [Latitude (dd), longitude (dd), and altitude (m)]
        '''
        
        if angle_unit == pilotUtils.DEGREES:
            return self._lla
        return np.array([rad2deg(self._lla[0]),
                         rad2deg(self._lla[1]),
                         self._lla[2]])
    
    def ecef(self):
        '''
        [ECEF-X (m), ECEF-Y (m), ECEF-Z (m)]
        '''
        
        return coordinate.lla2ecef(self._lla, pilotUtils.DEGREES).squeeze()
    
    def euler(self, angle_unit=pilotUtils.DEGREES, NED_to_body=True):
        '''
        321 angles to/from navigation frame
        [roll, pitch, yaw]
        '''
        
        return rotation.dcm2angle(self._v_R_n, angle_unit, NED_to_body, 321).squeeze()
    
    def quat(self, NED_to_body=True):
        '''
        Quaternion to/from navigation frame
        [x, y, z, w]
        '''
        
        if NED_to_body:
            return rotation.dcm2quat(self._v_R_n).squeeze()
        return rotation.dcm2quat(self._v_R_n.T).squeeze()

    def body2ned(self, x):
        '''
        Transform a point/set of points/vectors from the vehicle to navigation frame
        '''
        
        inputs.assert3Vec(x)
        return self._v_R_n.T @ x
    
    def ned2body(self, x):
        '''
        Transform a point/set of points/vectors from the navigation to vehicle frame
        '''
        
        inputs.assert3Vec(x)
        return self._v_R_n @ x
    
    def body2ecef(self, x):
        '''
        Transform a point/set of points/vectors from the vehicle to ECEF frame
        '''
        
        return transformPt(self.e_P_v(), x)
    
    def ecef2body(self, x):
        '''
        Transform a point/set of points/vectors from the ECEF to vehicle frame
        '''
        
        return transformPt(self._v_P_e, x)
    
    def body2lla(self, x):
        '''
        Transform a point/set of points/vectors from the vehicle frame to lat/lon/alt coordinate(s)
        '''
        
        return coordinate.ned2lla(self._v_R_n.T @ x, self._lla, pilotUtils.DEGREES)
    
    def lla2body(self, x):
        '''
        Transform lat/lon/alt coordinate(s) to points/vectors in the vehicle frame
        '''
        
        return self._v_R_n @ coordinate.lla2ned(x, self._lla, pilotUtils.DEGREES)
    
    def update_dcm(self, _v_R_n_):
        '''
        Update navigation to vehicle frame DCM
        '''
        
        inputs.assertDCM(_v_R_n_)
        assert len(_v_R_n_.shape) == 2, 'DCM is not a single 3x3 array'
        
        self._v_R_n = _v_R_n_
        self._v_P_e = poseMat(self._v_R_n @ self._n_R_e, self._e_t_e_v).squeeze()

    def update_loc_lla(self, _lla_, angle_unit=pilotUtils.DEGREES):
        '''
        Update lat/lon/alt
        '''
        
        inputs.assert3Vec(_lla_)
        assert len(_lla_.shape) == 1, 'Coordinate is not a single 1x3 array'
        
        self._lla = _lla_
        
        if angle_unit == pilotUtils.RADIANS:
            self._lla[:2] = rad2deg(_lla_[:2])

        self._e_t_e_v = coordinate.lla2ecef(self._lla, pilotUtils.DEGREES).squeeze()
        self._n_R_e   = coordinate.ecef2ned_dcm(self._lla, pilotUtils.DEGREES).squeeze()
        self._n_P_e   = poseMat(self._n_R_e, self._e_t_e_v).squeeze()
        self._v_P_e   = poseMat(self._v_R_n @ self._n_R_e, self._e_t_e_v).squeeze()

    def update_loc_ecef(self, _ecef_):
        '''
        Update ECEF position
        '''
        
        inputs.assert3Vec(_ecef_)
        assert len(_ecef_.shape) == 1, 'Coordinate is not a single 1x3 array'
        
        self._lla     = coordinate.ecef2lla(_ecef_, pilotUtils.DEGREES).squeeze()
        self._e_t_e_v = _ecef_
        self._n_R_e   = coordinate.ecef2ned_dcm(self._lla, pilotUtils.DEGREES).squeeze()
        self._n_P_e   = poseMat(self._n_R_e, self._e_t_e_v).squeeze()
        self._v_P_e   = poseMat(self._v_R_n @ self._n_R_e, self._e_t_e_v).squeeze()


class payload_pose():
    def __init__(self, vid, pid):
        self._vehicleID = vid
        self._payloadID = pid
        
        self._v_t_v_p = np.zeros(3) # translation vector (in m) from vehicle CG to payload in the vehicle's body frame
        self._p_R_v   = np.eye(3)   # dcm from vehicle's body frame to payload's body frame
        self._p_P_v   = np.eye(4)   # pose matrix that maps points from the vehicle's body frame to the payload's body frame https://en.wikipedia.org/wiki/Affine_transformation
    
    def vehicleID(self):
        return self._vehicleID
    
    def payloadID(self):
        return self._payloadID
    
    def v_t_v_p(self):
        '''
        Translation vector from the vehicle to payload frame resolved in the vehicle frame
        '''
        
        return self._v_t_v_p
    
    def p_t_p_v(self):
        '''
        Translation vector from the payload to vehicle frame resolved in the payload frame
        '''
        
        return -self._v_t_v_p
    
    def p_R_v(self):
        '''
        Rotation DCM from the vehicle to payload frame
        '''
        
        return self._p_R_v
    
    def v_R_p(self):
        '''
        Rotation DCM from the payload to vehicle frame
        '''
        
        return self._p_R_v.T
    
    def p_P_v(self):
        '''
        Pose matrix from the vehicle to payload frame
        '''
        
        return self._p_P_v
    
    def v_P_p(self):
        '''
        Pose matrix from the payload to vehicle frame
        '''
        
        return reversePoseMat(self._p_P_v).squeeze()
    
    def update_v_t_v_p(self, _v_t_v_p_):
        '''
        Update translation vector from the vehicle to payload frame resolved in the vehicle frame
        '''
        
        inputs.assert3Vec(_v_t_v_p_)
        assert len(_v_t_v_p_.shape) == 1, 'Coordinate is not a single 1x3 array'
        
        self._v_t_v_p = _v_t_v_p_
        self._p_P_v   = poseMat(self._p_R_v, self._v_t_v_p).squeeze()
    
    def update_p_t_p_v(self, _p_t_p_v_):
        '''
        Update translation vector from the payload to vehicle frame resolved in the payload frame
        '''
        
        inputs.assert3Vec(_p_t_p_v_)
        assert len(_p_t_p_v_.shape) == 1, 'Coordinate is not a single 1x3 array'
        
        self._v_t_v_p = -_p_t_p_v_
        self._p_P_v   = poseMat(self._p_R_v, self._v_t_v_p).squeeze()
    
    def update_p_R_v(self, _p_R_v_):
        '''
        Update rotation DCM from the vehicle to payload frame
        '''
        
        inputs.assertDCM(_p_R_v_)
        assert len(_p_R_v_.shape) == 2, 'DCM is not a single 3x3 array'
        
        self._p_R_v = _p_R_v_
        self._p_P_v = poseMat(self._p_R_v, self._v_t_v_p).squeeze()
    
    def update_v_R_p(self, _v_R_p_):
        '''
        Update rotation DCM from the payload to vehicle frame
        '''
        
        inputs.assertDCM(_v_R_p_)
        assert len(_v_R_p_.shape) == 2, 'DCM is not a single 3x3 array'
        
        self._p_R_v = _v_R_p_.T
        self._p_P_v = poseMat(self._p_R_v, self._v_t_v_p).squeeze()
    
    def update_p_P_v(self, _p_P_v_):
        '''
        Update pose matrix from the vehicle to payload frame
        '''
        
        inputs.assertPose(_p_P_v_)
        assert len(_p_P_v_.shape) == 2, 'Pose is not a single 4x4 array'
        
        self._p_P_v   = _p_P_v_
        self._p_R_v   = pose2dcm(self._p_P_v).squeeze()
        self._v_t_v_p = pose2t(self._p_P_v).squeeze()
    
    def update_v_P_p(self, _v_P_p_):
        '''
        Update pose matrix from the payload to vehicle frame
        '''
        
        inputs.assertPose(_v_P_p_)
        assert len(_v_P_p_.shape) == 2, 'Pose is not a single 4x4 array'
        
        self._p_P_v   = reversePoseMat(_v_P_p_).squeeze()
        self._p_R_v   = pose2dcm(self._p_P_v).squeeze()
        self._v_t_v_p = pose2t(self._p_P_v).squeeze()


class sensor_pose():
    def __init__(self, vid, pid, sid):
        self._vehicleID = vid
        self._payloadID = pid
        self._sensorID  = sid
        
        self._p_t_p_s = np.zeros(3) # translation vector (in m) from payload to sensor in the payload's body frame
        self._s_R_p   = np.eye(3)   # dcm from payload's body frame to sensor's body frame
        self._s_P_p   = np.eye(4)   # pose matrix that maps points from the payload's body frame to the sensor's body frame https://en.wikipedia.org/wiki/Affine_transformation

    def sensorID(self):
        return self._sensorID

    def p_t_p_s(self):
        '''
        Translation vector from the payload to sensor frame resolved in the payload frame
        '''
        
        return self._p_t_p_s

    def s_t_s_p(self):
        '''
        Translation vector from the sensor to payload frame resolved in the sensor frame
        '''
        
        return -self._p_t_p_s

    def s_R_p(self):
        '''
        Rotation DCM from the payload to sensor frame
        '''
        
        return self._s_R_p

    def p_R_s(self):
        '''
        Rotation DCM from the sensor to payload frame
        '''
        
        return self._s_R_p.T

    def s_P_p(self):
        '''
        Rotation DCM from the payload to sensor frame
        '''
        
        return self._s_P_p

    def p_P_s(self):
        '''
        Pose matrix from the sensor to payload frame
        '''
        
        return reversePoseMat(self._s_P_p).squeeze()

    def update_p_t_p_s(self, _p_t_p_s_):
        '''
        Update translation vector from the payload to sensor frame resolved in the payload frame
        '''
        
        inputs.assert3Vec(_p_t_p_s_)
        assert len(_p_t_p_s_.shape) == 1, 'Coordinate is not a single 1x3 array'
        
        self._p_t_p_s = _p_t_p_s_
        self._s_P_p   = poseMat(self._s_R_p, self._p_t_p_s).squeeze()

    def update_s_t_s_p(self, _s_t_s_p_):
        '''
        Update translation vector from the sensor to payload frame resolved in the sensor frame
        '''
        
        inputs.assert3Vec(_s_t_s_p_)
        assert len(_s_t_s_p_.shape) == 1, 'Coordinate is not a single 1x3 array'
        
        self._p_t_p_s = -_s_t_s_p_
        self._s_P_p   = poseMat(self._s_R_p, self._p_t_p_s).squeeze()

    def update_s_R_p(self, _s_R_p_):
        '''
        Update rotation DCM from the payload to sensor frame
        '''
        
        inputs.assertDCM(_s_R_p_)
        assert len(_s_R_p_.shape) == 2, 'DCM is not a single 3x3 array'
        
        self._s_R_p = _s_R_p_
        self._s_P_p = poseMat(self._s_R_p, self._p_t_p_s).squeeze()

    def update_p_R_s(self, _p_R_s_):
        '''
        Update rotation DCM from the sensor to payload frame
        '''
        
        inputs.assertDCM(_p_R_s_)
        assert len(_p_R_s_.shape) == 2, 'DCM is not a single 3x3 array'
        
        self._s_R_p = _p_R_s_.T
        self._s_P_p = poseMat(self._s_R_p, self._p_t_p_s).squeeze()

    def update_s_P_p(self, _s_P_p_):
        '''
        Update pose matrix from the payload to sensor frame
        '''
        
        inputs.assertPose(_s_P_p_)
        assert len(_s_P_p_.shape) == 2, 'Pose is not a single 4x4 array'
        
        self._s_P_p   = _s_P_p_
        self._s_R_p   = pose2dcm(self._s_P_p).squeeze()
        self._p_t_p_s = pose2t(self._s_P_p).squeeze()

    def update_p_P_s(self, _p_P_s_):
        '''
        Update pose matrix from the sensor to payload frame
        '''
        
        inputs.assertPose(_p_P_s_)
        assert len(_p_P_s_.shape) == 2, 'Pose is not a single 4x4 array'
        
        self._s_P_p   = reversePoseMat(_p_P_s_).squeeze()
        self._s_R_p   = pose2dcm(self._s_P_p).squeeze()
        self._p_t_p_s = pose2t(self._s_P_p).squeeze()
