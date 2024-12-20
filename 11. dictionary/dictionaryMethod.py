
# 
# ! items()

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(car.items())
# print(type(car.items()))


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.items()
# y = car.clear()  #! ye dictionary ke andar ke sare value  clear kardeta hai 


# car["year"] = 2018  #! we can also reassign the value in object when use item() also .

# print(x)
# print(y)



car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

z = car.copy()  # Creates a copy of the dictionary
car.clear()     # Clears the original dictionary

print("Original dictionary after clear():", car)
print("Copied dictionary:", z)

car["year"] = 2018  # Adding a new key-value pair to the original dictionary
print("Modified original dictionary:", car)
print("Copied dictionary remains unchanged:", z)
print("---------------------------------------------------------------------------------------------------")



# ! key() method

method = {
  "one" : "fail",
  "two" : "pass" ,
  "three" : "not pass" ,
  "four" : "just pass" , 
  "item" : {
    "first" : "one" 
  }


}


# print(list(method.keys()))

# print(len(method.keys()))
# print("---------------------------------------------------------------------------------------------------")
# print(list(method.values()))
method.update({"boy": "girll"})
print(method)