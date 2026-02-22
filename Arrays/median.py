# Find Median of the given Array



# 0

# Problem Statement: Given an unsorted array, find the median of the given array.

# What is a Median?
# Median is defined as the value which is present in the middle for a series of values. Note, in order to find the median of an array of integers, we must make sure they are sorted.

# Mathematically,



# Examples
# Example 1:
# Input:
#  [2,4,1,3,5]
# Output:
#  3

# Example 2:
# Input:
#  [2,5,1,7]
# Output:
#  3.5





l=list(map(int,input().split()))
l.sort()
n=len(l)
if n%2!=0:
    print(l[n//2])
else:
    mid=n//2
    print((l[mid-1]+l[mid])/2)