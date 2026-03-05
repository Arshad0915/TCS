def is_sorted(nums):
    n=len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True

l=list(map(int,input().split()))
if is_sorted(l):
    print("The arr is sorted")
else:
    print("The arr is not sorted")