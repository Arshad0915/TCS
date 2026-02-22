# Rotate array by K elements : Block Swap Algorithm



# 0

# Problem Statement: Given an array of n size, rotate the array by k elements using the Block Swap Algorithm.

# Examples
# Input : N = 5, array[] = {1, 2, 3, 4, 5}, K = 2
# Output (Left Rotation) : {3, 4, 5, 1, 2}
# Explanation : After rotating left by 2, the first two elements move to the end.

# Input : N = 5, array[] = {1, 2, 3, 4, 5}, K = 2
# Output (Right Rotation) : {4, 5, 1, 2, 3}
# Explanation : After rotating right by 2, the last two elements move to the start.








# l=list(map(int,input().split()))
# k=int(input())
# n=len(l)
# k=k%n
# l1=l[:k]
# l2=l[k:]
# print(l2+l1)

class Solution:
    def reverse(self,a,l,r):
        while l<r:
            a[l],a[r]=a[r],a[l]
            l+=1
            r-=1
    def left_rotation(self,a,k):
        n=len(a)
        k=k%n
        if k==0:
            return
        self.reverse(a,0,k-1)
        self.reverse(a,k,n-1)
        self.reverse(a,0,n-1)
    
    def right_rotation(self,a,k):
        n=len(a)
        self.left_rotation(a,n-(k%n))


if __name__=="__main__":
    a=Solution()
    l=list(map(int,input().split()))
    k=int(input())
    l2=l.copy()
    print("Left rotation:")
    a.left_rotation(l,k)
    print(l)
    print("Right rotation:")
    a.right_rotation(l2,k)
    print(l2)



