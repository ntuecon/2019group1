import math
import numpy as np
import scipy
from scipy.optimize import minimize

global p
p = 1

class C():#cobb douglus utility function
    def __init__(self, alpha, a, beta, b, c, p, t,delta):
        self.alpha = alpha
        self.a = a
        self.c = c
        self.p = p
        self.t = t
        self.beta = beta
        self.b = b
        self.delta = delta
    def f(self, x, sign = -1):
        return sign*(self.a*pow(x[0], self.alpha) - self.p*x[0] + self.p*x[1] - self.c*pow(x[1],self.delta ) - self.t*x[0])
    def bnds(self):
        return ((0, None), (0, None))
    def opt(self):
        return minimize(self.f,(2, 0), method='SLSQP', bounds=self.bnds())
    def q(self):
        return self.opt().x[0]
    def l(self):
        return self.opt().x[1]
    def utility(self):
        return self.opt().fun - self.e()
    def e(self):
        return self.b * pow(self.q(), self.beta)


class CG():
    def __init__(self, alpha, a, beta, b, c, p,delta):
        self.alpha = alpha
        self.a = a
        self.c = c
        self.p = p
        self.beta = beta
        self.b = b
        self.delta = delta
    def f(self, x, sign = -1):
        return sign*(self.a*pow(x[0], self.alpha) - self.b*pow(x[0], self.beta)- self.p*x[0] + self.p*x[1] - self.c*pow(x[1],self.delta))
    def bnds(self):
        return ((0, None), (0, None))
    def opt(self):
        return minimize(self.f,(2, 0), method='SLSQP', bounds=self.bnds())
    def q(self):
        return self.opt().x[0]
    def l(self):
        return self.opt().x[1]
    def utility(self):
        return self.opt().fun

#============================================================

#imput
c = float(raw_input("c : "))
alpha = float(raw_input("alpha : "))
beta = float(raw_input("beta : "))
a = float(raw_input("a : "))
b = float(raw_input("b : "))
delta = float(raw_input("delta : "))
#equilibrium without government
part = C(alpha, a, beta, b, c, p, 0, delta)
print "equilibrium without considering externality : consume " + str(part.q()) + " and work " + str(part.l()) + " hours "
print "utility : " + str(part.utility())

#loss
print "loss : " + str(part.e())
#whole equilibrium
whole = CG(alpha, a, beta, b, c, p, delta)
print "equilibrium considering externality : consume " + str(whole.q()) + " and work " + str(whole.l()) + " hours "
print "utility : " + str(whole.utility())

#find right tax
down = 0
up = part.utility() / part.q()
for i in range (10):
    t = (up + down)/2
    qt = C(alpha, a, beta, b, c, p, t, delta).opt()
    if qt > whole.q():
        down = t
    elif qt < whole.q():
        up = t
    else:
        break
t  = (up + down)/2
print "tax implimented to deal with externality : " + str(t)
