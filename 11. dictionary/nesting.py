#
#! nesting is also possible in disctionary n python 

student = {
  "name" : "jiwan",
  "surname" : "tajpuriya" , 
  "level" : "bachelor" ,
  "subject" : {
    "math" : 56 ,
    "english" : 34 ,
    "bca" : 12 ,
  }
}
print("the student got marks in math:"+ str(student["subject"]["math"]))
print(student.get("subject").get("bca"))