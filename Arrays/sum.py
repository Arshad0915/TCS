# Calculate Sum of the Elements of the Array



# 0

# Problem Statement: Given an array arr of size n, the task is to find the sum of all the elements in the array .

# Examples

# Input: N = 5, array[] = {1,2,3,4,5}
# Output: 15
# Explanation: Sum of all the elements is 1+2+3+4+5 = 15

# Input:  N=6, array[] = {1,2,1,1,5,1}
# Output: 11
# Explanation: Sum of all the elements is 1+2+1+1+5+1 = 11




l=list(map(int,input().split()))

sum=0
for i in l:
    sum+=i
print(sum)
