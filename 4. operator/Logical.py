# logical operator
"""
three types of logical operators are ( not , and , or)
"""
# not operator
# its always gives pstive to negative value
a = 23
b= 24
result = not(a==b)
print(result)

fa =34
fb=34
result2 = not(fa>=fb)
print(result2)


# and operator
#  in this operator if two value are true than this operator gives true other its determines false let see in example

firstname = "shayam"
secondname= "sundar"
checkNames = ((firstname == secondname) and (secondname == firstname))
print(checkNames)


# or operators
# in or operators if one value is true than than its gives true value

firstnum = 23
secondnum = 34
checknum = ((a==b)or(a<b))
print(checknum)