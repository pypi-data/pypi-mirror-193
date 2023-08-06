import numpy as np


def assertPose(input, arg_name='Input') -> None:
    assert type(input) is np.ndarray, '{} pose is not an array'.format(arg_name)
    assert len(input.shape) > 1,      '{} pose has fewer dimensions than expected'.format(arg_name)
    
    if len(input.shape) == 2:
        assert input.shape == (4, 4), '{} pose is not a 4x4 array'.format(arg_name)
    
    elif len(input.shape) == 3:
        assert input.shape[1:] == (4, 4), '{} poses are not 4x4 arrays'.format(arg_name)
    
    else:
        assert True == False, '{} pose has an invalid number of dimensions'.format(arg_name)

def assertDCM(input, arg_name='Input') -> None:
    assert type(input) is np.ndarray, '{} DCM is not an array'.format(arg_name)
    assert len(input.shape) > 1,      '{} DCM has fewer dimensions than expected'.format(arg_name)
    
    if len(input.shape) == 2:
        assert input.shape == (3, 3), '{} DCM is not a 3x3 array'.format(arg_name)
    
    elif len(input.shape) == 3:
        assert input.shape[1:] == (3, 3), '{} DCMs are not 3x3 arrays'.format(arg_name)
    
    else:
        assert True == False, '{} DCM has an invalid number of dimensions'.format(arg_name)

def assert4Vec(input, arg_name='Input') -> None:
    assert type(input) is np.ndarray, '{} vector is not an array'.format(arg_name)
    assert input.shape[-1]  == 4,     '{} vectors are not 1x4 arrays'.format(arg_name)
    assert len(input.shape) <= 3,     '{} vector has an invalid number of dimensions'.format(arg_name)

def assert3Vec(input, arg_name='Input') -> None:
    assert type(input) is np.ndarray, '{} vector is not an array'.format(arg_name)
    assert input.shape[-1]  == 3,     '{} vectors are not 1x3 arrays'.format(arg_name)
    assert len(input.shape) <= 3,     '{} vector has an invalid number of dimensions'.format(arg_name)