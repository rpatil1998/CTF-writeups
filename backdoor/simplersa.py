#!/usr/bin/python2
import gmpy2

p =  24659183668299994531
q =  28278904334302413829
e =  11
c =  589000442361955862116096782383253550042
t = (p-1)*(q-1)
n = p*q

# returns d such that e * d == 1 modulo t, or 0 if no such y exists.
d = gmpy2.invert(e,t)

# Decryption
m = pow(c,d,n)
print "Solved ! m = %d" % m
