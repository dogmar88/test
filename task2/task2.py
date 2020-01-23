import sys # I have a shorter version of this program in the second file. It is more elegant, but I'm don't sure you have the geometric library installed.

class Point(list): # defying classes of points, segments, figures, and checking methods
	def __init__(self,x,y):
	  self.x=x
	  self.y=y

class Segment(list):
  def __init__(self,x,y):
    self.p1 = x
    self.p2 = y
    self.length=(((self.p2.x - self.p1.x)**2) + ((self.p2.y - self.p1.y) ** 2)) ** 0.5

  def checkpoint(self,p):
    seg1 = Segment(self.p1, p)	
    seg2 = Segment(p, self.p2)
    if self.length == seg1.length + seg2.length: return True
    else: return False

class Figure(list):
  def __init__(self,a, b, c, d):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.e = Segment(a,b)
    self.f = Segment(b,c)
    self.g = Segment(c,d)
    self.h = Segment(d,a)

  def pointInside(self,point):
    figure_x = [self.a.x, self.b.x, self.c.x, self.d.x]
    figure_y = [self.a.y, self.b.y, self.c.y, self.d.y]
    c = False
    for i in range(4):
      if ((((figure_y[i] <= point.y) and (point.y < figure_y[i-1])) or ((figure_y[i-1] <= point.y) and (point.y < figure_y[i]))) and (point.x > (figure_x[i-1] - figure_x[i]) * (point.y - figure_y[i]) / (figure_y[i-1] - figure_y[i]) + figure_x[i])):
        c = True
    return c

def whereThePoint (figure, point): # that main method of output
    if point.x == b[0].x and point.y == b[0].y or point.x == b[1].x and point.y == b[1].y or point.x == b[2].x and point.y == b[2].y or point.x == b[3].x and point.y == b[3].y:
      return 0
    if figure.e.checkpoint(point)==True or figure.f.checkpoint(point)==True or figure.g.checkpoint(point)==True or figure.h.checkpoint(point)==True:
      return 1
    if figure.pointInside(point):
      return 2
    return 3

inp=open(sys.argv[1],'r')
a=[]
b=[]
for i in inp:
    a.append(list(map(float,i.strip().split())))
for i in a:
    b.append(Point(i[0],i[1]))
e=Figure(b[0],b[1],b[2],b[3])
inp=open(sys.argv[2],'r')
for i in inp:
    a=list(map(float,i.strip().split()))
    c=Point(a[0],a[1])
    print (whereThePoint(e,c))
