def count_vowels_consonants(s):
    s=s.lower()
    l=['a','e','i','o','u']
    v,c=0,0
    for ch in s:
        if ch.isalpha():
            if ch in l:
                v+=1
            else:
                c+=1
    return v,c

s=input("Enter any string")
v,c=count_vowels_consonants(s)
print(f"no of vowels:{v}")
print(f"no of consonants:{c}")
