n=int(input("Enter any number:"))
tot=0
n=abs(n)
while n>0:
    tot=tot+n%10
    n//=10
print(tot)