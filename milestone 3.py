import math
import numpy as np
from scipy.optimize import minimize


class C():#cob douglus utility function
    def __init__(self, alpha, a, c, t):
        self.alpha = alpha
        self.a = a
        self.c = c
        self.t = t
    def f(self, q, sign = -1):
        return sign*alpha*pow(q, alpha) - c*q - t*q
    def opt(self):
        s = minimize(self.f, q)
        return s
    def utility(self):
        return f(minimize(self.f, q))

class E():
    def __init__(self, beta, b):
        self.beta = beta
        self.b = b
    def cost(self, q):
        return b * pow(q, beta)

class CG():
    def __init__(self, alpha, a, beta, b, c):
        self.alpha = alpha
        self.a = a
        self.beta = beta
        self.b = b
        self.c = c
    def f(self, q, sign = -1):
        return sign*alpha*pow(q, alpha) - b * pow(q, beta) - c * q
    def opt(self):
        s = minimize(self.f, q)
        return s
    def utility(self):
        return f(minimize(self.f, q))

class Producer():
    def __init__(self, q):
        self.l = l
        self.q = l

#=============================================================
def tryIt(S, C, Pa, Pb, w):
    pi = S.optPi(Pa, Pb, w)
    Qa = [C.optQa(Pa, Pb, w, pi), S.optQb(Pa, Pb, w)]
    Qb = [C.optQb(Pa, Pb, w, pi), S.optQb(Pa, Pb, w)]
    H = [C.optH(Pa, Pb, w, pi), S.optH(Pa, Pb, w)]
    return [Qa, Qb, H]



#============================================================
#imput
c = float(raw_input("c : "))
alpha = float(raw_input("alpha : "))
beta = float(raw_input("beta : "))
a = float(raw_input("a : "))
b = float(raw_input("b : "))

#whole equilibrium
whole = CG(alpha, a, beta, b, c)
q_whole = whole.opt()
if q_whole < 0:
    print("there will not be an equilibrium")
    exit()
#equilibrium without government
part = C(alpha, a, c, 0)
q_part = part.opt()

#loss
ex = E(beta, b)
loss = ex.cost(q_part)

#find right tax
down = 0
up = part.utility() / q_part
for i in range 10:
    t = (up + down)/2
    qt = C(alpha, a, c, t).opt()
    if qt > q_whole:
        down = t
    elif qt < q_whole:
        up = t
    else:
        break
t = t = (up + down)/2

print("equilibrium without considering externality : consume " + str(q_part) + " units and work " + str(Producer(q_part).l) + " hours")
print("utility : " + str(part.utility()))
print("loss : " + str(loss) + )
print("equilibrium considering externality : consume " + str(q_whole) + " units and work " + str(Producer(q_whole).l) + " hours")
print("utility : " + str(whole.utility()))
print("tax implimented to deal with externality : " + str(t))
