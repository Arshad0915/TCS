def isanagram(s1,s2):
    d1={}
    for ch in s1:
        d1[ch]=d1.get(ch,0)+1
    d2={}
    for ch in s2:
        d2[ch]=d2.get(ch,0)+1
    return d1==d2

def isanagram_1(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

from collections import Counter

def isanagram_2(s1, s2):
    return Counter(s1) == Counter(s2)


s1,s2=input().split(",")
if isanagram(s1,s2):
    print("They are anagrams")
else:
    print("They are not anagrams")