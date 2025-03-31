from uncertainties import ufloat
from uncertainties.umath import * 
import math
# Units in M
D = ufloat(3.10, 0.15)
A = ufloat(0.26, 0.005)
B = ufloat(0.452, 0.003)
o = 2039*2*math.pi
r = ufloat(0.00156, 0.005)
c = (4*A * D**2 * (o))/(r * (D + B))

print(c)
