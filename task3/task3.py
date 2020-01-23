import sys

if (sys.argv[1][-1]) != '\\':
  path=sys.argv[1]+'\\Cash'
else:
  path=str(sys.argv[1]+'Cash')
a=[[] for j in range(6)]
for i in range(5):
  file=open(path+str(i+1)+'.txt','r')
  for j in file:
    a[i].append(float(j.strip()))
for i in range(16):
    a[5].append(a[0][i]+a[1][i]+a[2][i]+a[3][i]+a[4][i])
print (a[5].index(max(a[5]))+1)
