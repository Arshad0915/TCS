def rev(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n//=10
    return rev

n=int(input("Enter any number:"))
if n<0:
    print("Not a palindrome")
else:
    if rev(n)==n:
        print("Palindrome")
    else:
        print("Not a palindrome")