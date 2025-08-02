"""
Control Systems Engineering, 6th, Norman Nise
ch3p1, Pg. 793
"""

import numpy as np
import control as ctrl
# Installed the above package using the alternate install from source
# instructions here: https://python-control.readthedocs.io/en/0.8.0/intro.html
# Was actually pretty easy.


print('ch3p1')
A = np.array([[0,1,0],[0,0,1],[-9,-8,-7]])

print('ch3p2')
C = np.array([2,3,4]) # When it comes to multiplication, Numpy knows when to
B = np.array([[7],[8],[9]]) # treat the array as a row or a column vector?

print('ch3p3')
D = 0
F = ctrl.ss(A,B,C,D)

print('ch3p4')
print('Numerator-denominator representation conversion')

print('Controller canonical form')
num = 24 # Define numerator of G(s) = C(s)/R(s)
den = np.array([1,9,26,24]) # Define denominator of G(s)
sys = ctrl.tf2ss(num,den) # Convert G(s) to controller canonical form, store
sys                       # matrices A, B, C, D and display
print('Phase-variable form')
P = np.array([[0,0,1],[0,1,0],[1,0,0]]) # Form transformation matrix
Ap = np.linalg.inv(P)
Ap = Ap@A@P # Form A matrix, phase-variable form
Bp = np.linalg.inv(P)@B # Form B vector, phase-variable form
Cp = C@P # Form C vector, phase-variable form
Dp =D # Form D vector, phase-variable form
print('LTI object representation')
T = ctrl.tf(num,den) # Represent T(s) = 24/(s^3+9s^2+26s+24) as an LTI
                     # transfer object
Tss = ctrl.ss(T)
