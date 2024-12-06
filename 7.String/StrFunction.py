# 1 endswith()

name = "abuzer khan"
check1 = name.endswith("an")
print(check1) #? True

# 2 Capitalized

name = "mannu"
name = name.capitalize() #? aur iss tarah karenge to purana ko hii change kardega
# print(name.capitalize()) ye ek naya string bana deta purana ko change nhi karta hai 
print(name)

# ? find

name = "shankar"
check3 = name.find("s")
print(check3)

# check3 = name.find("binod")
# print(check3) #-1 because it not exist

#? count / replace

name = "i am boy am i booy or not Am i disco"
check4 = name.count("am")
check5 = name.replace("am" , "are")
print(check5)
print(check4)

