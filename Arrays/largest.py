# Find the Largest element in an array



# 22

# Problem Statement: Given an array, we have to find the largest element in the array.

# Examples
# Example 1:
# Input:
#  arr[] = {2, 5, 1, 3, 0}  
# Output:
#  5  
# Explanation:
  
# 5 is the largest element in the array.

# Example 2:
# Input:
#  arr[] = {8, 10, 5, 7, 9}  
# Output:
#  10  
# Explanation:
  
# 10 is the largest element in the array.



l=list(map(int,input().split()))
largest=l[0]

if not l:
    print("empty list")
else:
    for i in range(1,len(l)):
      if l[i]>largest:
        largest=l[i]
    print(largest)

