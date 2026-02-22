# Reverse a given Array



# 14

# Problem Statement: You are given an array. The task is to reverse the array and print it.

# Examples
# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# Input: N=6 arr[] = {10,20,30,40}
# Output: {40,30,20,10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.



l=list(map(int,input().split()))
left=0
right=len(l)-1
while left<right:
    l[left],l[right]=l[right],l[left]
    left=left+1
    right=right-1
print(l)