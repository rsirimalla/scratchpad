# Environment variables
import os
os.environ['something'] = 'something'


# loops
for num in range(1,100,2):
  print(num)

  
# Named tuple (More readable way of representing tuples - object like)
# Regular way 
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
from math import sqrt
line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
# Named tuple way
from collections import namedtuple
Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
from math import sqrt
line_length = sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)

