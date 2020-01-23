import sys
import numpy

inp=open(sys.argv[1],'r')
a=[]
for i in inp:
    a.append(int(i.strip()))
print (f"{numpy.percentile(a, 90):.{2}f}")
print (f"{numpy.median(a):.{2}f}")
print (f"{max(a):.{2}f}")
print (f"{min(a):.{2}f}")
print (f"{sum(a)/len(a):.{2}f}")
