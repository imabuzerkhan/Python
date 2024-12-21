# while loop

# ! print hello world 10 times for using while loop

# count = 1
# while count<=10 :
#   print("hello world")
#   count += 1 

  # ! print 1 to 100 number for using while loops

# count = 1
# while count<=100:
#   print("the no is" , count)
#   count +=1


  # ! print number from 100 to 1
# count = 100
# while count>=1:
#     print("the number is:" , count )
#     count -= 1

  # ! print multiplication table of number n
# number = int(input("enter the number:"))
# count = 1
# while count<=10 :
#   print(number*count)
#   count += 1


# ! print the elemnt of the following list using a loop

num = [1,2,3,4,5,6,7,8,9,0]
idx = 0
while idx <= len(num) - 1:  # Error: `list` is not the name of your list; it should be `num`
  print(num[idx])  # Error: `[idx]` creates a list with the value of `idx`; it should be `num[idx]`
  idx += 1

