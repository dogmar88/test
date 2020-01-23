import sys
from shapely.geometry import Polygon, Point

i1=open(sys.argv[1],'r')
figura=[]
for i in i1:
   figura.append(list(map(float, i.split())))
poly = Polygon([(figura[0]),(figura[1]),(figura[2]),(figura[3])])
i2=open(sys.argv[2],'r')
for i in i2:
    p=Point(map(float, i.strip().split()))
    if list(map(float, i.strip().split())) in figura:
      print ('0')
      continue
    if poly.intersects(p)==True and poly.contains(p)==True:
      print ('2')
      continue
    if poly.intersects(p)==True:
      print ('1')
    else:
      print ('3')
