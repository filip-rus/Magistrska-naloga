from decimal import Decimal, getcontext
import time
#100 1000 5000 10.000
#neoptimizirani algoritmi za vse formule bratov chudnovsky
#  =e/sqrt(a^3) sum (fact) \frac{b + cn}{a}
#test = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
test = Decimal('3.141592')
def algo(i,dec,e,a,b,c):
    start = time.time()
    extra_prec = 3
    getcontext().prec = dec + extra_prec
    delni_prejšnji = Decimal(100)
    delni_novi = Decimal(b)
    n = 0
    sd = 1
    bs = 1
    while (delni_prejšnji - delni_novi) != 0:
        delni_prejšnji = delni_novi
        bs = bs*(6*n + 6)*(6*n + 5)*(6*n + 4)*(6*n + 3)*(6*n + 2)*(6*n + 1)
        sd = sd*(3*n + 3)*(3*n + 2)*(3*n + 1)*(n+1)**3*(-a)**(3)
        ss = bs*(b + c*(n+1))
        n += 1
        delni_novi += Decimal(ss)/Decimal(sd)
    delni_novi *= Decimal(e)/Decimal(a**Decimal(1.5))
    pi = Decimal(1/delni_novi)
    pi = pi.to_eng_string()[:-2]
    end = time.time()
    if i == 1:
        return (pi,n,end-start)
    else:
        return(n,end-start)
    

from decimal import Decimal, getcontext
import time
#100 1000 5000 10.000
#neoptimiziran
#  =e/sqrt(a^3) sum (fact) \frac{b + cn}{a}
#test = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
test = Decimal('3.141592')
def algo2(i,dec,e,a,b,c):
    start = time.time()
    extra_prec = 3
    getcontext().prec = dec + extra_prec
    delni_prejšnji = Decimal(100)
    delni_novi = Decimal(b)
    n = 0
    sd = 1
    bs = 1
    while (delni_prejšnji - delni_novi) != 0:
        delni_prejšnji = delni_novi
        bs = bs*(6*n + 6)*(6*n + 5)*(6*n + 4)*(6*n + 3)*(6*n + 2)*(6*n + 1)
        sd = sd*(3*n + 3)*(3*n + 2)*(3*n + 1)*(n+1)**3*(a)**(3)
        ss = bs*(b + c*(n+1))
        n += 1
        delni_novi += Decimal(ss)/Decimal(sd)
    delni_novi *= Decimal(e)/Decimal(a**Decimal(1.5))
    pi = Decimal(1/delni_novi)
    pi = pi.to_eng_string()[:-2]
    end = time.time()
    if i == 1:
        return (pi,n,end-start)
    else:
        return(n,end-start)
    
from decimal import Decimal, getcontext
import time
#100 1000 5000 10.000
#neoptimiziran
#  =e/sqrt(a^3) sum (fact) \frac{b + cn}{a}
#test = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
test = Decimal('3.141592')
def algo3(i,dec,e,a,b,c,s):
    start = time.time()
    extra_prec = 3
    getcontext().prec = dec + extra_prec
    delni_prejšnji = Decimal(100)
    delni_novi = Decimal(b)
    n = 0
    sd = 1
    bs = 1
    while (delni_prejšnji - delni_novi) != 0:
        delni_prejšnji = delni_novi
        bs = bs*(6*n + 6)*(6*n + 5)*(6*n + 4)*(6*n + 3)*(6*n + 2)*(6*n + 1)
        sd = sd*(3*n + 3)*(3*n + 2)*(3*n + 1)*(n+1)**3*(a)**(3)*(s)
        ss = bs*(b + c*(n+1))
        n += 1
        delni_novi += Decimal(ss)/Decimal(sd)
    delni_novi *= Decimal(e)/Decimal(s**Decimal(0.5)*(a)**Decimal(1.5))
    pi = Decimal(1/delni_novi)
    pi = pi.to_eng_string()[:-2]
    end = time.time()
    if i == 1:
        return (pi,n,end-start)
    else:
        return(n,end-start)
    
from decimal import Decimal, getcontext
import time
#100 1000 5000 10.000
#neoptimiziran
#  =e/sqrt(a^3) sum (fact) \frac{b + cn}{a}
#test = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
test = Decimal('3.141592')
def algo4(i,dec,e,a,b,c,s):
    start = time.time()
    extra_prec = 3
    getcontext().prec = dec + extra_prec
    delni_prejšnji = Decimal(100)
    delni_novi = Decimal(b)
    n = 0
    sd = 1
    bs = 1
    while (delni_prejšnji - delni_novi) != 0:
        delni_prejšnji = delni_novi
        bs = bs*(6*n + 6)*(6*n + 5)*(6*n + 4)*(6*n + 3)*(6*n + 2)*(6*n + 1)
        sd = sd*(3*n + 3)*(3*n + 2)*(3*n + 1)*(n+1)**3*(a)**(3)
        ss = bs*(b + c*(n+1))
        n += 1
        delni_novi += Decimal(ss)/Decimal(sd)
    delni_novi *= Decimal(e)/Decimal(s**Decimal(0.5)*(a)**Decimal(1.5))
    pi = Decimal(1/delni_novi)
    pi = pi.to_eng_string()[:-2]
    end = time.time()
    if i == 1:
        return (pi,n,end-start)
    else:
        return(n,end-start)