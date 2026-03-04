def linear_search(arr,key):
    for i in arr:
        if i==key:
            return True
    return False

def linear_search_1(arr, key):
    for index, value in enumerate(arr):
        if value == key:
            return index
    return -1


l=list(map(int,input().split()))
key=int(input())
if linear_search(l,key):
    print("Found")
else:
    print("Not found")
