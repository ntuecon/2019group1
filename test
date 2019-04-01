p = int(raw_input('Price of lemonade'))
c = int(raw_input('Cost of lemonade'))
w = int(raw_input('Wage of wokers'))
a = int(raw_input('utility function of lemonades U = a*Q + b, a = '))
b = int(raw_input('utility function of lemonades U = a*Q + b, b = '))
ul = int(raw_input('how much you hate work'))
fq = int(raw_input('how many person/hour it takes to make a lemonade'))

class function:
    def __init__(self, slope, shift):
        self.slope = slope
        self.shift = shift
    def shift_function(self, shift_num):
        self.shift += shift_num
    def rotate_function(self, rotate_num):
        self.slope += rotate_num
    def value(self, x):
        return self.slope * x + self.shift
uq = function(a, b)

q = 0
C = fq * q *(w-ul) - p*q + uq.value(q)
F = (p-c) *q -fq*q*w
TU = C+F
q_new = q+1
C_new=fq*q_new*(w-ul) - p*q_new + uq.value(q_new)
F_new = (p-c) *q_new -fq*q_new*w
TU_new = C_new+F_new
while TU_new > TU & C_new > 0 & F_new > 0:
    q = q+1
    C = fq*q*(w-ul) - p*q + uq.value(q)
    F = (p-c) *q -fq*q*w
    TU = C+F
    q_new = q+1
    C_new=fq*q_new*(w-ul) - p*q_new + uq.value(q_new)
    F_new = (p-c) *q_new -fq*q_new*w
    TU_new = C_new+F_new


print "there will be " + str(q) + " cups of lemonades in this world"
