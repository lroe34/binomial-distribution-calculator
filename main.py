from math import factorial
from fractions import Fraction
n=int(input('n='))
p=float(input('p='))
probList=[]

for k in range(0,n+1): 
    c=(factorial(n)/(factorial(n-k)*factorial(k)))
    x=c*(p**k)
    y=(1-p)**(n-k)
    #probList.append("{:.3f}".format(x*y))
    probList.append(Fraction(x*y).limit_denominator())
print(probList)