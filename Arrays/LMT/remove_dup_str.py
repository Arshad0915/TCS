def remove_dup(s):
    l=set()
    res=[]
    for ch in s:
        if ch not in l:
            res.append(ch)
            l.add(ch)
    return "".join(res)



s=input("Enter any string")
print(remove_dup(s))