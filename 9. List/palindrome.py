
list_1 = [1,2,1]
list_2 = [2,1,2]

copy_list = list_1.copy()
copy_list.reverse()

if (copy_list == list_1):
  print("it is palindrome")
else:
  print("it is not palindrome")