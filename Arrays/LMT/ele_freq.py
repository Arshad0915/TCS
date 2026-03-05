def element_freq(nums,key):
    return nums.count(key)

# def element_freq(nums,key):
#     count = 0
#     for num in nums:
#         if num == key:
#             count += 1
#     return count



l=list(map(int,input().split()))
key=int(input())
print(element_freq(l,key))