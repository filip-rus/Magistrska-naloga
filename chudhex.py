import time
from decimal import Decimal, getcontext
from decimal import *
#algoritem vrne t-to števko pi v šestnajstiškem sestavu

def binary_split(a, b):
    if b == a + 1:
        Pab = -(6*a - 5)*(2*a - 1)*(6*a - 1)
        Qab = 10939058860032000 * a**3
        Rab = Pab * (545140134*a + 13591409)
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)
        
        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab

#digits = število vseh izračunanih decimalk
#t hex decimalka na mestu t
#t mora biti manj kot digits*0.83
def chudnovsky(digits,t):
    start = time.time()
    DIGITS_PER_TERM = 14.181647462725477
    getcontext().prec = digits + 3
    N = int(digits/DIGITS_PER_TERM + 1)
    P1n, Q1n, R1n = binary_split(1, N)
    pi = (426880 * Decimal(10005).sqrt() * Q1n) / (13591409*Q1n + R1n)
    test = hex(int(pi*Decimal(pow(16,t)) - 16*int(pi*Decimal(pow(16,t-1)))))
    pi = pi.to_eng_string()[:-2]
    end = time.time()
    return (test,end-start)