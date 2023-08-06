import logging

logger = logging.getLogger('quake_inverse_sq._sqrt_pure_python')

logger.warning('No native extension found. Falling back to pure python implementation.')
del logger, logging # epic memory safety for absolutely no fucking reasons

from ctypes import c_float, c_int32, cast, byref, POINTER
from math import sqrt

def coarse_inv_sqrt(number: float):
    THREEHALFS = 1.5
    x2 = number * 0.5
    y = c_float(number)
    WHAT_THE_FUCK = 0x5f3759df
    i = cast(byref(y), POINTER(c_int32)).contents.value
    i = c_int32(WHAT_THE_FUCK - (i >> 1))
    y = cast(byref(i), POINTER(c_float)).contents.value
    y = y * (THREEHALFS - (x2 * y * y))
    return y
def fined_inv_sqrt(number: float):
    return 1/sqrt(number)