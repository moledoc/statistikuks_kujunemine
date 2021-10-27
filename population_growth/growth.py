import time
import math

def nb_year(p0,percent,aug,p):
    if percent == 0 :
        return (p-p0)/aug
    r = 1+percent/100
    c = (aug+p*r-p)/(aug+p0*r-p0)
    return math.ceil(math.log(c)/math.log(r))

def nb_year_iter(p0,percent,aug,p):
    count = 0
    while p0 < p:
        count += 1
        p0 = (1+percent/100)*p0 + aug
    return count

i = 1000
p0 = 100
p = 0.001
aug = 10
pn = 100_000_000_000_000_000
print(f"P_0: {p0}\ngrowth: {p}\nnew inhab.: {aug}")
print(f'{"P_N":<20}{"Calculation time":<20}{"Iteration time":<20}{"Calculation value":<20}{"Iteration value":<20}{"Speedup":<20}')
while i < pn:
    start_calc=time.monotonic()
    calculated = nb_year(p0,p,aug,i)
    end_calc=time.monotonic()
    iterated = start_iter=time.monotonic()
    iterated = nb_year_iter(p0,p,aug,i)
    end_iter=time.monotonic()
    calc_time = end_calc-start_calc
    iter_time = end_iter-start_iter
    print(f'{i:<20}{round(calc_time,10):<20.2e}{round(iter_time,10):<20.2e}{calculated:<20}{iterated:<20}{round(iter_time/calc_time,2):<20}')
    i *= 10