# -*- coding: utf-8 -*-

def dump_row(i, R):
  print('R[', i, '] = ', sep='', end='')
  for j in range(i+1):
    print(R[j], ' ', sep='', end='')
  print()


def romberg(f, a, b, max_steps, acc):
  Rp = [0 for _ in range(max_steps)] # Previous row
  Rc = [0 for _ in range(max_steps)] # Current row
  h = (b-a) # Step size
  Rp[0] = (f(a) + f(b)) * h * 0.5 # First trapezoidal step
  dump_row(0, Rp); # Print first row

  for i in range(1, max_steps):
    h /= 2
    c = 0
    ep = 1 << (i-1) # 2^(n-1)

    for j in range(1, ep+1):
      c += f(a+(2*j-1)*h)

    Rc[0] = h*c + 0.5 * Rp[0] # R(i,0)

    for j in range(1, i+1):
      n_k = 4**j
      Rc[j] = (n_k * Rc[j-1] - Rp[j-1]) / (n_k-1) # compute R(i,j)

    # Print ith column of R, R[i,i] is the best estimate so far
    dump_row(i, Rc);

    if i > 1 and abs(Rp[i-1] - Rc[i]) < acc:
      return Rc[i-1]

    # swap Rn and Rc as we only need the last row
    rt = Rp
    Rp = Rc
    Rc = rt

  return Rp[max_steps-1] # return our best guess

"""## Definicja funkcji G"""

from math import exp, pi, sqrt


def G(t):
  def internal(x):
    return exp(-(x**2) / 2)
  return romberg(internal, 0, t, 1000, 0.001)

"""## Definicja funkcji Phi"""

def phi(t):
  if t < 0:
    return 1 - phi(-t)
  return 0.5 + 1/sqrt(2 * pi) * G(t)

"""## Kilka przykładów i testów"""

t = 0.5
print('G(', t, ') = ', G(t), sep ='')

"""#### Chcemy, aby bardzo małe t było bliskie 0 oraz bardzo duże t było bliskie 1"""

t2 = 10000
print('Phi(', t2, ') = ', phi(t2), sep ='')
t3 = - 10000
print('Phi(', t3, ') = ', phi(t3), sep ='')

"""#### Kilka losowych przykładów"""

t4 = 3
t5 = 1.5
t6 = 1
t7 = 0.75
t8 = 0.5
t9 = 0.25
t10 = 0.1
t11 = 0

print('Phi(', t4, ') = ', phi(t4), sep ='')
print('Phi(', t5, ') = ', phi(t5), sep ='')
print('Phi(', t6, ') = ', phi(t6), sep ='')
print('Phi(', t7, ') = ', phi(t7), sep ='')
print('Phi(', t8, ') = ', phi(t8), sep ='')
print('Phi(', t9, ') = ', phi(t9), sep ='')
print('Phi(', t10, ') = ', phi(t10), sep ='')
print('Phi(', t11, ') = ', phi(t11), sep ='')
