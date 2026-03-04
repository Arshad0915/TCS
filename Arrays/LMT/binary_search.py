def binary_seach(arr,ele):
    arr.sort()
    l=0
    r=len(arr)-1
   
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==ele:
            return f"Element found at index{mid}"
            
        elif arr[mid]>ele:
            r=mid-1
        else:
            l=mid+1
    return "Element not found"

l=list(map(int,input().split()))
ele=int(input())
print(binary_seach(l,ele))
