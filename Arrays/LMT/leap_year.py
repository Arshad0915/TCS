def leap_year(n):
    if n<=0:
        return False
    return (n%4==0 and n%100!=0) or (n%400==0)

n=int(input())
if leap_year(n):
    print("Its a leap year")
else:
    print("Its not a leap year")