def rev_str(s):
    return s[::-1]

def rev_str_1(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

def rev_str_2(s):
    s = list(s)
    left, right = 0, len(s)-1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        
    return "".join(s)


s=input("Enter any string")
print(rev_str(s))