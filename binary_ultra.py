import time
from decimal import Decimal, getcontext
from decimal import *
#decimalke z metodo binarne ločitve

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

def chudnovsky(digits):
    start = time.time()
    DIGITS_PER_TERM = 14.181647462725477
    getcontext().prec = digits + 3
    N = int(digits/DIGITS_PER_TERM + 1)
    P1n, Q1n, R1n = binary_split(1, N)
    pi = (426880 * Decimal(10005).sqrt() * Q1n) / (13591409*Q1n + R1n)
    pi = pi.to_eng_string()[:-2]
    end = time.time()
    return (pi,end-start)



#isti algoritem z uporabo gypy2
import time
from gmpy2 import mpz, isqrt


def binary_split(a, b):
    if b == a + 1:
        Pab = mpz(-(6*a - 5)*(2*a - 1)*(6*a - 1))
        Qab = mpz(10939058860032000 * a**3)
        Rab = mpz(Pab * (545140134*a + 13591409))
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)
        
        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab


def chudnovsky_bs(digits):
    start = time.time()
    DIGITS_PER_TERM = 14.181647462725477
    N = int(digits/DIGITS_PER_TERM + 1)
    """Chudnovsky algorithm."""
    P1n, Q1n, R1n = binary_split(1, N)
    kvadrat = mpz(10)**(2*digits)
    pi = (426880 * isqrt(10005*kvadrat) * Q1n) // (13591409*Q1n + R1n)  
    end = time.time()
    return end-start

