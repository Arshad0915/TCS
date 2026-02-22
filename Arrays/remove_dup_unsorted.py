# Remove Duplicates From an Unsorted Array

# 0

# Problem Statement: Given an unsorted array, remove duplicates from the array.

# Examples
# Input: arr[]={2,3,1,9,3,1,3,9}
# Output: {2,3,1,9}
# Explanation: Removed all the duplicate elements.
# Input: arr[]={4,3,9,2,4,1,10,89,34}
# Output: {4,3,9,2,1,10,89,34}
# Explanation: Removed all the duplicate elements.



l=list(map(int,input().split()))
seen=set()
l1=[]
n=len(l)
for i in l:
    if i not in seen:
        seen.add(i)
        l1.append(i)
print(l1)
