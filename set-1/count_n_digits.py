#Count number of Digits in an integer.
n=int(input())
c=0
while(n>0):
    n=n//10
    c=c+1
print(c)
