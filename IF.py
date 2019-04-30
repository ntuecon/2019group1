import math
class C_B_U():#cob douglus utility function
    def __init__(self, alpha, beta, c):
        self.alpha = alpha
        self.beta = beta
        self.c = c
    def optQa(self, Pa, Pb, w, pi):
        return pow((pow((beta/Pb), alpha)*pow((Pa/alpha), (beta-1))*w/c), (1/(1-beta-alpha)))
    def optQb(self, Pa, Pb, w, pi):
        return pow((pow((Pa/alpha), alpha)*pow((beta/Pb), (alpha-1))*w/c), (1/(1-beta-alpha)))
    def optH(self, Pa, Pb, w, pi):
        return pow(((alpha+beta)/alpha*(pow((beta/Pb), beta)*pow((Pa/alpha), (beta-1))*w/c)), (1/(1-beta-alpha)))*Pa/w-pi/w

class SupplyFunction():
    def __init__(self, ca, cb):
        self.ca = ca
        self.cb = cb
    def optQa(self, Pa, Pb, w):
        return ((Pa-ca)/(2*w))
    def optQb(self, Pa, Pb, w):
        return ((Pb-cb)/(2*w))
    def optH(self, Pa, Pb, w):
        return (self.optQa(Pa, Pb, w)*self.optQa(Pa, Pb, w))+(self.optQb(Pa, Pb, w)*self.optQb(Pa, Pb, w))
    def optPi(self, Pa, Pb, w):
        return (Pa*self.optQb(Pa, Pb, w)-ca)*self.optQa(Pa, Pb, w) + (Pb*self.optQb(Pa, Pb, w)-ca)*self.optQa(Pa, Pb, w) - w * self.optH(Pa, Pb, w)

#=============================================================
def tryIt(S, C, Pa, Pb, w):
    pi = S.optPi(Pa, Pb, w)
    Qa = [C.optQa(Pa, Pb, w, pi), S.optQb(Pa, Pb, w)]
    Qb = [C.optQb(Pa, Pb, w, pi), S.optQb(Pa, Pb, w)]
    H = [C.optH(Pa, Pb, w, pi), S.optH(Pa, Pb, w)]
    return [Qa, Qb, H]



#============================================================
ca = float(raw_input("Cost of product A :"))
cb = float(raw_input("Cost of product B : "))
c = float(raw_input("c : "))
alpha = float(raw_input("alpha : "))
beta = float(raw_input("beta : "))

S = SupplyFunction(ca, cb)
C = C_B_U(alpha, beta, c)
Pa = ca+1
Pb = cb+1
w = c+1
test = tryIt(S, C, Pa, Pb, w)
for i in range(100):
    w2 = w+1
    test2 = tryIt(S, C, Pa, Pb, w2)
    if abs(test2[2][0]-test2[2][1]) < abs(test[2][0]-test[2][1]):
        w = w2
        test = test2
for i in range(100):
    test = tryIt(S, C, Pa, Pb, w)
    if test[0][0]> test[0][1]:
        Pa += 1
    elif test[0][0]< test[0][1]:
        Pa -= 1
    if test[1][0]> test[1][1]:
        Pb += 1
    elif test[1][0]< test[1][1]:
        Pb -= 1
