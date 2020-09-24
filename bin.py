from math import comb
from math import factorial
from math import e


class DiscProb:
    def __init__(self):
        pass

    def bin(x, n, p):
        return comb(n, x)*pow(p,x)*pow(1-p,n-x)

    def Bin(y, n, p):
        sum = 0
        for i in range(0, y+1):
            sum += bin(i, n, p)
        return sum

    def poisson(x, u):
        return (pow(e, -u)*pow(u, x))/(factorial(x))

    def sumPoisson(n, u):
        sum = 0
        for i in range(0, n+1):
            sum += poisson(i,u)
        return sum
    
    def negbin(x, r, p):
        return comb(x+r-1, r-1)*pow(p, r)*pow(1-p,x)

    def sumNegbin(n, r, p):
        sum = 0
        for i in range(0, n+1):
            sum += negbin(i, r, p)
        return sum
