set term pdf

A= 100.
D=20.
h= 0.2
k=0.1

f(x) = D/x*A + h*x/2

g(x,T) =  A/T + h/2*x*x/D/T + k*(D-x/T)

set xrange [0:150]
#set xrange [118:123]
set yrange [10:40]

set output "eoq_loss_0_1.pdf"

plot f(x),  g(x,5), g(x,7.2), g(x,8)

#plot g(x,7.5), g(x,8), g(x,8.5)




