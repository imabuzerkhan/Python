# list method

# ! Append any type of data in he list

name = ["abuzer"]
name.append("danish")
print(name)

# ! sort 

num = [4,3,2]
num.sort()
print(num)

# ? we can also sort with character
char = ['c','t','r']
char.sort(reverse=True)
print(char)

# ! reverse 

name = ["abuzer khan", "danish"]
print(name.reverse()) #it return none because yekhali hai aur ussi list me change karta naya list nahi banta hai string kii tarah
print(name)



# ! pop

pop = [2,3,5,7]
pop.pop(1) #* pop basically koi bhi data ko dlt karne  ke liye kaam aaata hai 
print(pop)


# ! remove

remove = [1,3,5,1,5,2,6,7,3,6,7]
remove.remove(7)   #* its delete the first occurence of data
print(remove)  

# ! insert

data = ["a","b","c","d"]
data.insert(0 , "abuzer")
print(len(data))

# !