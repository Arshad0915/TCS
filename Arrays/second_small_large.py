# Find Second Smallest and Second Largest Element in an array



# 9

# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

# Examples
# Example 1:
# Input:
#  [1, 2, 4, 7, 7, 5]  
# Output:
  
# Second Smallest : 2  
# Second Largest : 5  
# Explanation:
#   The elements are sorted as 1, 2, 4, 5, 7, 7.  
# Hence, the second smallest element is 2, and the second largest element is 5.

# Example 2:
# Input:
#  [1]  
# Output:
  
# Second Smallest : -1  
# Second Largest : -1  
# Explanation:
#   Since there is only one element in the array, it is both the largest and smallest element.  
# Therefore, there is no second smallest or second largest element present.








# l=list(map(int,input().split()))

# l.sort()
# print(f"second smallest:{l[1]}")
# print(f"second largest::{l[len(l)-2]}")

l=list(map(int,input().split()))

if len(l)<2:
    print("need atleast 2 elements")

else:
    small=second_smallest=float('inf')
    large=second_largest=float('-inf')
    for i in range(len(l)):
        if l[i]<small:
            second_smallest=small
            small=l[i]
        elif l[i]<second_smallest and l[i]!=small:
            second_smallest=l[i]
        if l[i]>large:
            second_largest=large
            large=l[i]
        elif l[i]>second_largest and l[i]!=large:
            second_largest=l[i]

print(f"Second largest:{second_largest}")
print(f"Second smallest:{second_smallest}")

