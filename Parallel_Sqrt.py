
from IPython import parallel
rc = parallel.Client()
rc.block = True
dview = rc[:]

from math import *
from numpy import *




x = [ 9.50129,  2.31139,  6.06843,  4.85982,  8.91299,  7.62097,  4.56468,  0.18504,
         8.21407,  4.44703,  6.15432,  7.91937,  9.21813,  7.38207,  1.76266,  4.05706,
         9.3547,   9.16904,  4.1027,   8.9365,   0.57891,  3.52868,  8.13166,  0.09861,
         1.38891,  2.02765,  1.98722,  6.03792,  2.72188,  1.98814]

y = [ 23.57002,   7.95719,  17.26218,  15.00733,  21.67951,  21.43285,  15.31852,
      5.33244,  21.75544,  14.06871,  17.12194,  21.56453,  22.84794,  21.94733,
      8.38893,  13.22806,  24.77616,  23.39737,  13.10976,  22.04064,   6.45224,
      10.72118,  21.97765,   6.82079,  7.08604,   9.9133,   10.22844,  15.48212,
      9.00279,   9.54743]


def for1(j):
    n=30
    sum_x=0
    sum_y=0
    sum_xx=0
    sum_xy=0
    
    for i in range(j,n/2+j):
   
        sum_x=sum_x+x[i]
        sum_y=sum_y+y[i]
        xx=pow(x[i],2)
        sum_xx=sum_xx+xx
        xy=x[i]*y[i]
        sum_xy=sum_xy+xy
    
    
    return([sum_x, sum_xy, sum_xx, sum_y])


n =30
res1=for1(0)
res2=for1((n/2))

  
a=(-(res1[0]+res2[0])*(res1[1]+res2[1])+(res1[2]+res2[2])*(res1[3]+res2[3]))/(n*(res1[2]+res2[2])-(res1[0]+res2[0])*(res1[0]+res2[0]))
b=(-(res1[0]+res2[0])*(res1[3]+res2[3])+n*(res1[1]+res2[1]))/(n*(res1[2]+res2[2])-(res1[0]+res2[0])*(res1[0]+res2[0]))

print "The required straight line is Y=%sX+(%s)"%(b,a)


