
from collections import Counter
l=list(map(int,input().split()))

d=Counter(l)
for k,v in d.items():
    if v>1:
        print(k,end=" ")
        

# l = list(map(int, input().split()))
# d = {}

# for i in l:
#     d[i] = d.get(i, 0) + 1

# for k, v in d.items():
#     if v > 1:
#         print(k, end=" ")