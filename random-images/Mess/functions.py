from __future__ import division
from math import cos,sin, e, pi, exp

LITUUS_K = 2.3

def butterfly(theta):
    return e**(sin(theta)) - 2*cos(4*theta) + sin((2*theta-pi)/(24))**5

def leaf(theta):
    return (1 + 0.9 * cos(8 * theta)) * (1 + 0.1 * cos(24 * theta)) * (0.9 + 0.05 * cos(200 * theta)) * (1 + sin(theta))

def spiral(theta):
    return 3 * exp(0.2*theta)

def lituus(theta):
    return (LITUUS_K/theta)**0.5