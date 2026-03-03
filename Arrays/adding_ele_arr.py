class Solution:
    def insert_at_begin(self,a,ele):
        a.insert(0,ele)
        
    def insert_at_end(self,a,ele):
        a.append(ele)
        
    def insert_at_pos(self,a,ele,pos):
        if pos < 0 or pos > len(a):
            print("Invalid position")
        else:
            a.insert(pos,ele)
        

if  __name__=="__main__":
    a=Solution()

    l=list(map(int,input().split()))
    n1=int(input("Enter ele to insert at beginning"))
    a.insert_at_begin(l,n1)
    print(l)
    n2=int(input("Enter ele to insert at end"))
    a.insert_at_end(l,n2)
    print(l)
    n3,pos=map(int,input().split())
    a.insert_at_pos(l,n3,pos)
    print(l)
    