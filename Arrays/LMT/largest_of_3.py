n1,n2,n3=map(int,input().split())

if n1>=n2 and n1>=n3:
    print("The largest num is",n1)
elif n2>=n1 and n2>=n3:
    print("The largest num is",n2)
else:
    print("The largest num is",n3)
