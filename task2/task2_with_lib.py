import sys
from shapely.geometry import Polygon, Point # it will not work without this library. I hope you have it installed. Also I wrote a different version, long, but more autonomic - look at the second file.

i1=open(sys.argv[1],'r')
figura=[]
for i in i1:
   figura.append(list(map(float, i.split()))) # creating a figure for polygon class
poly = Polygon([(figura[0]),(figura[1]),(figura[2]),(figura[3])])
i2=open(sys.argv[2],'r')
for i in i2: # applying methods from geometry
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
