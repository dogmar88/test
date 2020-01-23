import sys
import numpy # well i guess numpy is a basic library for python programmers.

inp=open(sys.argv[1],'r')
a=[]
for i in inp:
    a.append(int(i.strip()))
print (f"{numpy.percentile(a, 90):.{2}f}") # it is decimal formation of numbers after the point. It can be failed in Python 2.
print (f"{numpy.median(a):.{2}f}")
print (f"{max(a):.{2}f}")
print (f"{min(a):.{2}f}")
print (f"{sum(a)/len(a):.{2}f}")
