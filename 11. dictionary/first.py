#  what is dictionary

# ! for example in other language we say object 

object = {
  "name" : "abuzer",
  "age" : 23 ,
  "father's name" : "shalauddin khan" ,
  "mother name" : "rehan khatoon"
}

object["name"] = "khan bhai"  #! we can also change the existing value in dict
object ["hobby"] = ["cricket" , "playing" , "singing"] ,

print(object)
access = object["name"]
print(access)

# ! also we used get() function to access name age etc

fathername = object.get("father's name")
print(fathername)