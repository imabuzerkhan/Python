# fibnacii series
a = 0
b = 1 
print(a , b , end= " ")

for _ in range (8):
  Next_term = a + b 
  print(Next_term , end= " ") 
  a , b = b , Next_term 
