n = int(input())
arr = list(map(int, input().split()))

total = n * (n + 1) // 2
sum_arr = sum(arr)

print(total - sum_arr)