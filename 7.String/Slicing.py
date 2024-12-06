# 
# ! this is more important topic for macchine leraning and python also 
# ? so what is slicing ? jaha tak main samjha huu isko aisa bol sake the kii hum apne data ka kaha se kaha tak value chaiye expale dekh lete hai na 


Sentences = "we are from united state of America and we are decide to stay in nepal for 2 month. "
Slice2 = Sentences[0:10] #? ek baat yaad rakho last ka index count nhi hota usse ek phele wala count hota hai 
slice3 = Sentences[5:len(Sentences)] #? agar last index nhi denge length daldenge to samaj jayega kii value last chaiye isko

print(slice3)
print(Slice2)

# ? negative slicing bhi hota hai 

work = "doctor"
check = work[-4:-1] #? iss tarah se negative value ka use bkar sakte hai slicing me 
print(check)