def mat_add(m1,m2):
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
      return "Matrix dimensions must match"
    r1=len(m1)
    c1=len(m1[0])

    sum_mat=[[0 for _ in range(c1)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c1):
            sum_mat[i][j]=m1[i][j]+m2[i][j]
    return sum_mat


def create_mat():
    rows,cols=map(int,input().split())
    data=input().strip()

    nums=list(map(int,data.split(",")))

    matrix=[]

    k=0

    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append(nums[k])
            k+=1
        matrix.append(row)
    return matrix

# def create_mat():
#     rows, cols = map(int,input().split())

#     matrix=[]
#     for _ in range(rows):
#         row=list(map(int,input().split()))
#         matrix.append(row)

#     return matrix

m1=create_mat()
m2=create_mat()

print(mat_add(m1,m2))