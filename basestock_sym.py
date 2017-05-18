import numpy as np
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save

from matplotlib import style
style.use('ggplot')


D = np.array([1,2,3,0,4,4,2,0,1,3]) # demand during a period
L = 3 # leadtime

X = np.zeros_like(D) # demand during leadtime

for t in range(L):
    X[t] = sum(D[0:t+1])

for t in range(L, len(D)):
    X[t] = sum(D[t-L+1:t+1])
print(X)    

fig = plt.figure()
plt.plot(D, 'o-', markersize=2, label="D")
plt.plot(X, 'o-', markersize=4, label='X')

plt.xlabel('$t$')
# plt.ylabel('$D_t$ / $X_t$')
plt.title('Demand and demand during leadtime')
plt.grid(True)
plt.legend(loc='upper right')
# plt.show()
tikz_save('basestock_demand_figures.tex', figureheight='5cm', figurewidth='12cm')


r = 5

IP = (r+1)*np.ones_like(D)

IL = np.zeros_like(D) # end of period inventory level
IL[0] = IP[0] - D[0]

for t in range(1, L):
    IL[t] = IL[t-1] - D[t]
    
for t in range(L, len(D)):
    IL[t] = IL[t-1] - D[t] + D[t-L] 

# print(IL)
    
fig = plt.figure()
plt.plot(IP, 'o-', markersize=2, label="IP")
plt.plot(IL, 'o-', markersize=4, label='IL')
plt.ylim((-6,6))
plt.xlabel('$t$')
# plt.ylabel('$D_t$ / $X_t$')
plt.title('Inventory position $IP_t$ and inventory level $IL_t$')
plt.grid(True)
plt.legend(loc='lower right')
# plt.show()
tikz_save('basestock_position_figures.tex', figureheight='5cm', figurewidth='12cm')

It = np.maximum(IL, 0)
Bt = - np.minimum(IL, 0)

fig = plt.figure()
plt.plot(It, 'o-', markersize=2, label="$I_t$")
plt.plot(Bt, 'o-', markersize=4, label='$B_t$')
plt.ylim(ymax=7)
plt.xlabel('$t$')
plt.title('On hand and backlog')
plt.grid(True)
plt.legend(loc='lower right')
# plt.show()
tikz_save('basestock_on_hand_figures.tex', figureheight='5cm', figurewidth='12cm')

I = It.mean()
B = Bt.mean()
print(I)
print(B)

S = (I>0).sum()
print(S)

