n=int(input("Enter any number:"))
if n<=0:
    print("Enter a pos num")
else:
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b