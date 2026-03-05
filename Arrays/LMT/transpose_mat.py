def transpose(mat):
   r=len(mat)
   c=len(mat[0])

   t=[[0 for _ in range(r)] for _ in range(c)]

   for i in range(r):
       for j in range(c):
           t[j][i]=mat[i][j]
   return t

# def transpose(mat):
#     return [list(row) for row in zip(*mat)]

def create_mat():
    rows, cols = map(int,input().split())
    matrix=[]
    for _ in range(rows):
        row=list(map(int,input().split()))
        matrix.append(row)
    return matrix


m=create_mat()

print(transpose(m))