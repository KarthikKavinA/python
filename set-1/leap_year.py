#program to check whether a given year is leap or not?
y=int(input())
if y%4==0:
  if y%100!=0:
    print("yes")
  else:
    if y%400==0:
      print("yes")
    else:
      print("no")
else:
  print("no")
