def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)


n=int(input("Enter any number"))
if n<0:
    print("Factorial for neg numbers not defined")
else:
    print(fact(n))