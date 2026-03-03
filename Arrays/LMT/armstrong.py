def cnt_digit(n):
    c=0
    while n>0:
        c=c+1
        n//=10
    return c


def armstrong(n):
    c=cnt_digit(n)
    a=n
    num=0
    while a>0:
        digit=a%10
        num=num+digit**c
        a//=10
    if num==n:
        print("It is armstrong number")
    else:
        print("Its not a armstrong number")

n=int(input("Enter any number:"))
if n<0:
    print("Enter a pos num")
else:
    armstrong(n)