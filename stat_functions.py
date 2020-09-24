import math

class DiscProb:
    def __init__(self):
        self.sum = 0
    
    # Binomial function
    def bin(self, x, n, p):
        return math.comb(n, x) * pow(p,x) * pow(1 - p,n - x)
    
    # Sum of binomials
    def Bin(self, y, n, p):
        self.sum = 0
        for i in range(0, y+1):
            self.sum += self.bin(i, n, p)
        return self.sum
    
    # Poisson distribution
    def poisson(self, x, u):
        return (pow(math.e, -u) * pow(u, x)) / (math.factorial(x))

    def sumPoisson(self, n, u):
        self.sum = 0
        for i in range(0, n+1):
            self.sum += self.poisson(i, u)
        return self.sum
    # Negative binomial distribution
    def negbin(self, x, r, p):
        return math.comb(x + r - 1, r - 1)*pow(p, r)*pow(1 - p,x)

    def sumNegbin(self, n, r, p):
        self.sum = 0
        for i in range(0, n+1):
            self.sum += self.negbin(i, r, p)
        return self.sum
