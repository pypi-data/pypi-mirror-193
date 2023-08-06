import sys
from os.path import dirname

import numpy as np
from numpy import pi

SRC_DIR = dirname(__file__)
sys.path.append(SRC_DIR)

import inputs


RADIANS = True
DEGREES = False

dRx = 0 # w.r.t. rotation around the x axis
dRy = 1 # w.r.t. rotation around the y axis
dRz = 2 # w.r.t. rotation around the z axis
dtx = 3 # w.r.t. translation around the x axis
dty = 4 # w.r.t. translation around the y axis
dtz = 5 # w.r.t. translation around the z axis


def interiorAngle(ref, comp, angle_unit=DEGREES):
    angle_1 = ref - comp
    
    if angle_unit == DEGREES:
        angle_2 = angle_1 - 360
        
    else:
        angle_2 = angle_1 - (2 * np.pi)
    
    if angle_1 < angle_2:
        return angle_1
    return angle_2

def wrapToPi(e):
    return (e + pi) % (2 * pi) - pi

def skew(_w: np.ndarray) -> np.ndarray:
    '''
    Description:
    ------------
    Make a skew symmetric matrix from a 3 element vector. Skew
    symmetric matrices are often used to easily take cross products.

    https://en.wikipedia.org/wiki/Skew-symmetric_matrix

    Arguments:
    ----------
    _w
        Nx3 vector

    Returns:
    --------
    C
        Nx3x3 Skew symmetric matrix of vector w
    '''
    
    w = _w.copy()
    
    inputs.assert3Vec(w)
    
    if len(w.shape) == 1:
        w = w.reshape(1, 3)
    
    C = np.zeros((w.shape[0], 3, 3))

    C[:, 0, 1] = -w[:, 2]
    C[:, 0, 2] =  w[:, 1]
    C[:, 1, 0] =  w[:, 2]
    C[:, 1, 2] = -w[:, 0]
    C[:, 2, 0] = -w[:, 1]
    C[:, 2, 1] =  w[:, 0]

    return C

def constrain(input, min, max):
    if type(input) is np.ndarray:
        input[input < min] = min
        input[input > max] = max
        
        return input
    
    else:
        if input < min:
            return min
        elif input > max:
            return max
        return input

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min