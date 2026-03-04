def second_largest(l):
    first=float('-inf')
    second=float('-inf')
    for i in l:
        if i>first:
            second=first
            first=i
        elif i>second and i!=first:
            second=i
    if second==float('-inf'):
        return None
    return second

l=list(map(int,input().split()))
print(second_largest(l))