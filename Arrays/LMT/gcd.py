n1=int(input("Enter 1st number"))
n2=int(input("Enter 2nd number"))

if n2==0:
    print(abs(n1))
else:
    while n2!=0:
      n1,n2=n2,n1%n2
    print(abs(n1))



