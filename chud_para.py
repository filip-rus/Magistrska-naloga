from decimal import Decimal, getcontext
import time
#neoptimiziran chudnovsky algoritem
# e/\sqrt(a)^3 = sum (fact) \frac{b + cn}{d}
#test = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
test = Decimal('3.141592')
def algo(dec):
    start = time.time()
    extra_prec = 3
    getcontext().prec = dec + extra_prec
    delni_prejšnji = Decimal(100)
    delni_novi = Decimal(13591409)
    n = 0
    sd = 1
    bs = 1
    while abs(delni_prejšnji - delni_novi) > 10**(-dec):
        delni_prejšnji = delni_novi
        bs = bs*(6*n + 6)*(6*n + 5)*(6*n + 4)*(6*n + 3)*(6*n + 2)*(6*n + 1)
        sd = sd*(3*n + 3)*(3*n + 2)*(3*n + 1)*(n+1)**3*(-640320)**(3)
        ss = bs*(13591409 + 545140134*(n+1))
        n += 1
        delni_novi += Decimal(ss)/Decimal(sd)
    delni_novi *= Decimal(12)/Decimal(640320).sqrt()
    pi = Decimal(1/delni_novi)
    pi = pi.to_eng_string()[:-2]
    end = time.time()
    return end-start