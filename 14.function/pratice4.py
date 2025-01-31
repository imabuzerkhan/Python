import math
def circle(radius) :
  CircleVal =  round (math.pi ** radius * 2 , 2)
  Circumference = round ( 2 * math.pi ** radius , 2)
  return CircleVal , Circumference
result = circle(2)
print(result) 
