# wap to count a vowels no from word Education 

vowels = "aeiou"
word = "education"
count = 0 

for char in word:
  # *if (char == "a" or char == "e" or char=="i" or char == "o" or char == "u"):
  if char in vowels: #! using membership operator to check the count of vowels
    count += 1
print(f"The count of {word} is {count}")