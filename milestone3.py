import math
import numpy as np
from scipy import optimize

optimize.show_options(solver= 'minimize_scalar', disp=False)

class C():#cob douglus utility function
    def __init__(self, alpha, a, beta, b, c, p, t):
        self.alpha = alpha
        self.a = a
        self.c = c
        self.p = p
        self.t = t
        self.beta = 0
        self.b = 0
    def f(self, x, sign = -1):
        return sign*(self.a*pow(x, self.alpha) - self.p*x + self.p*pow(x, 2) - self.c*pow(x, 2) - self.t*x)
    def opt(self):
        s = optimize.minimize_scalar(self.f)
        return s.x
    def utility(self):
        return -optimize.minimize_scalar(self.f).fun

class E():
    def __init__(self, beta, b):
        self.beta = beta
        self.b = b
    def cost(self, q):
        return b * pow(q, beta)

class CG():
    def __init__(self, alpha, a, beta, b, c, p, t):
        self.alpha = alpha
        self.a = a
        self.beta = beta
        self.b = b
        self.c = c
        self.p = p
        self.t = 0
    def f(self, x, sign = -1):
        return sign*(self.a*pow(x, self.alpha) - self.b * pow(x, self.beta) - self.c * pow(x, 2))
    def opt(self):
        s = optimize.minimize_scalar(self.f, bounds=(0, 10000), method='bounded')
        return s.x
    def utility(self):
        return -optimize.minimize_scalar(self.f).fun

class Producer():
    def __init__(self):
        pass
    def l(self, q):
        return pow(q, 2)
    def w(self, p):
        return p
#============================================================
#max u by p
def maxC(alpha, a, beta, b, c, t):
    p = 1
    u = C(alpha, a, beta, b, c, p, t).utility()
    for i in range(2, 10000):
        if (C(alpha, a, beta, b, c, i, t).utility()>u):
            p = i
            u = C(alpha, a, beta, b, c, p, t).utility()
        else:
            break
    return p

def maxCG(alpha, a, beta, b, c, t):
    p = 1
    u = CG(alpha, a, beta, b, c, p, t).utility()
    for i in range(2, 10000):
        if (CG(alpha, a, beta, b, c, i, t).utility()>u):
            p = i
            u = CG(alpha, a, beta, b, c, p, t).utility()
        else:
            break
    return p
#============================================================

# part = C(1, 1, 1, 1, 1, 1, 0)
# print part.opt()
#
# part = CG(1, 1, 1, 1, 1, 1, 0)
# print part.opt()
#imput
c = float(raw_input("c : "))
alpha = float(raw_input("alpha : "))
beta = float(raw_input("beta : "))
a = float(raw_input("a : "))
b = float(raw_input("b : "))

#equilibrium without government
p = maxC(alpha, a, beta, b, c, 0)
part = C(alpha, a, beta, b, c, p, 0)
q_part = part.opt()
if q_part < 0:
    print("there will not be an equilibrium")
    exit()
print "equilibrium without considering externality : consume " + str(q_part) + " units at price " + str(p) + " and work " + str(Producer(q_part).l) + " hours at wage " + str(Producer(p).w)
print "utility : " + str(part.utility())

#loss
ex = E(beta, b)
loss = ex.cost(q_part)
print "loss : " + str(loss)

#whole equilibrium
p = maxCG(alpha, a, beta, b, c, 0)
whole = CG(alpha, a, beta, b, c, p, 0)
q_whole = whole.opt()
if q_whole < 0:
    print("there will not be an equilibrium")
    exit()
print "equilibrium considering externality : consume " + str(q_whole) + " units at price " + str(p) + " and work " + str(Producer(q_whole).l) + " hours at wage " + str(Producer(p).l)
print "utility : " + str(whole.utility())

#find right tax
down = 0
up = part.utility() / q_part
for i in range (10):
    t = (up + down)/2
    qt = C(alpha, a, c, t).opt()
    if qt > q_whole:
        down = t
    elif qt < q_whole:
        up = t
    else:
        break
t = t = (up + down)/2
print "tax implimented to deal with externality : " + str(t)
