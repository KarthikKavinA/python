#Program to find greatest of three numbers.
a,b,c=map(int,input().split())
if a>b:
  if a>c:
    print(a)
  else:
    print(c)
elif b>a:
  if b>c:
    print(b)
  else:
    print(c)
elif c>a and c>b:
  print(c)
else:
  print("Invalid Input")
  
    
