from fractions import *

p = [ Fraction(1,6),
      Fraction(1,5),
      Fraction(1,4),
      Fraction(1,8),
      Fraction(11,120),
      Fraction(1,6)
      ]

G = [0]*len(p) # distribution function of X
G[0] = p[0]

for i in range(1,len(p)):
    G[i] = G[i-1] + p[i]
    print(i, p[i], G[i])


theta = sum(i*p[i] for i in range(6))
print(theta)

def B_base(r):
    return sum((i-r-1)*p[i] for i in range(r+1, len(p)))

for r in range(len(p)):
    print(r, B_base(r))

def I_base(r):
    return r+1-theta + B_base(r)

for r in range(len(p)):
    print(I_base(r))

# q,r model

def S(Q,r):
    res = sum(G[i] for i in range(r, r+Q))
    return res/Q

print(S(2,1))

def B(Q,r):
    res = sum(B_base(i) for i in range(r, r+Q))
    return res/Q

print(B(2,1))

def I(Q,r):
    return Fraction(Q+1,2) + r - theta + B(Q,r)


print(I(2,1))
    
    
    
