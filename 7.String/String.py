#  chapter strat from string 

name = "my name is mohammad abuzer khan"
print(name)

# ? second example 
# ? we write string in three way
name = "abuzer"
name2 = 'khan'
name3 = '''md'''
print(name + " " + name2 + " " + name3) #* this process is called concatination 

# ? can we add string and wrong it possible or not lets check

# name = "mannu khan"
# age = 23 
# merge = name + age 
# print(merge) #* its not possible to add string and number but it can possible when we use type casting change the intring into int value


# ? how to check the length of string 

name = "joshan shrestha"
print(len(name)) #* its gives 15 its also count white space 

# ? another way to check the length of string

name = "ishan bhai"
check = len(name)
print(check) 

# ? get knowlede escapes seqquence let know what is this

myName = "mrs anand\tkumar khan and\ni am from nepal "
# ! \n simple create new line and \t creat a space 
print(myName)