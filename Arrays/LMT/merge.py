n1 = int(input())
a = list(map(int, input().split()))

n2 = int(input())
b = list(map(int, input().split()))

merged = []

for i in range(n1):
    merged.append(a[i])

for i in range(n2):
    merged.append(b[i])

for num in merged:
    print(num, end=" ")