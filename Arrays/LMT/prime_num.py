import math
n=int(input("Enter a number"))
if n<=1:
    print("Not a prime")
else:
    isprime=True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            isprime=False
            break
    print("Prime") if isprime else print("Not a prime")

