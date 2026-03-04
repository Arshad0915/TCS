def gcd(a,b):
    while b:
        a,b=b,a%b
    return abs(a)

def lcm(a,b):
    if a==0 or b==0:
        return 0
    return abs(a*b)//gcd(a,b)

n1,n2=map(int,input().split())
print(lcm(n1,n2))