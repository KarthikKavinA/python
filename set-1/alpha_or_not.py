#Program to check whether a character is an alphabet or not.
n=input()
if n.isalpha():
  print("Alphabet")
elif not(n.isalpha()):
  print("No")
else:
  print("Invalid Input")
