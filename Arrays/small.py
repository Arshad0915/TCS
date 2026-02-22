# Find the smallest element in an array



# 8

# Problem Statement: Given an array, we have to find the smallest element in the array.

# Examples
# Example 1:
# Input:
#  arr[] = {2, 5, 1, 3, 0}  
# Output:
#  0  
# Explanation:
#   0 is the smallest element in the array.

# Example 2:
# Input:
#  arr[] = {8, 10, 5, 7, 9}  
# Output:
#  5  
# Explanation:
#   5 is the smallest element in the array.




l=list(map(int,input().split()))
small=l[0]
for i in range(1,len(l)):
    if l[i]<small:
        small=l[i]
print(small)
