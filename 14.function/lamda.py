#  practicing lambda
cell = lambda x : x + 4 
result = cell(2)
print(result)
# print(cell(2))

#  lambda with two parameter
sum = lambda a , b : a * b + a
result2 = sum(2 , 5)
print(result2)

#  using lambda and function ech other

def SumNum(num1) :
  return lambda x : x + num1
double = SumNum(5)
print(double(4))