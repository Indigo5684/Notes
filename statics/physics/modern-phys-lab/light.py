from uncertainties import ufloat
from uncertainties.umath import * 
import math
# Units in CM
D = ufloat(3.1, 0.15)
A = ufloat(0.26, 0.005)
B = ufloat(0.452, 0.003)
omega = ufloat(2000*2*math.pi, 0)
r = ufloat(0.00156, 0.005)
c = 4*(A * D**2 * omega)/(r * (D + B))

print(c)