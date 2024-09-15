# returning the list of the sum position in an array

"""mylist=[int(x) for  x in input().split()]
target=int(input())
found=False
mlist=[]
for i in range(len(mylist)-1):
    if mylist[i]+mylist[i+1]==target:
        found=True
        mlist=[i+1,i+2]
    if found:
        print(mlist)
        break"""
import ctypes as ct
#value_1=ct.c_int(10)# o =output
# print(value_1) o=c_long(10)
# print(value_1.value) o=10
#print(id(value_1.value))#140723410307800
#ptr=ct.pointer(value_1)
#print(id(ptr.contents))#2073049480272

# print(id(ptr.contents.value))#140723410307800


#a=10
#ptr=ct.pointer(ct.c_int(a))

# swapping using pointers
'''def fun(a,b):
    temp=a.contents.value
    a.contents.value=b.contents.value
    b.contents.value=temp
    print(f"{a.contents.value}\n{b.contents.value}")
a=ct.pointer(ct.c_int(10))
b=ct.pointer(ct.c_int(20))
fun(a,b)
print("A")'''

# taking out the duplicates in a list
"""mylist=[int(x) for x in input().split()]
unique_list=[]
for i in mylist:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)"""

#sort an array using pointers
"""a= 10 not linked like pointers because these are primintive dt and they are immutable 
b=a
a=6
b=4
print(f"a={a}\nb={b}")"""
"""
a=[10]
b=a
a[0]=4
b[0]=9
print(f"a={a}\nb={b}")
print(id(b))
print(id(a))"""
"""
list1=[int(x) for x in input().split()]
list2=list1

def selection_sort(list2):
    # Traverse through all list elements
    for i in range(len(list2)):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, len(list2)):
            if list2[j] < list2[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        list2[i], list2[min_index] = list2[min_index], list2[i]  # swap using index "pointers"


# Call the selection sort
selection_sort(list2)

print("Sorted array:", list1)  # Output: [11, 12, 22, 25, 64]"""

# finding the biggest element in an array using pointers
"""
list1=[int(x) for x in input().split()]
list2=list1
def big_element(list2):
    list2.sort()
    big=list2[len(list2)-1]
    return big
print(f"biggest element in the array:{big_element(list2)}")"""

# target position returning in an array
""" list1=[int(x) for x in input().split()]
target=int(input("enter the target element:"))
mylist=[]
found=False
for i in range(len(list1)-1):
    if list1[i]+list1[i+1]==target:
        mylist=[i+1,i+2]
        break
if found:
    print(mylist)"""

# 2d array in python
""""
m,n=(map(int,input().split()))
list1=[int(x) for x in input().split()]
list2=[list1[i*n:(i+1)*n] for i in range(m)]
print(list2)"""
a=[[1,2,3],[4,5,7]]
#print(len(a)) 2-no of rows

"""n=len(a[0])
for i in range(n):
    for j in range(len(a)):
        print(a[j][i],end=" ")
    print()
"""
# sum of a matrix
'''b=[[1,2],[1,2]]
sumb=0
for i in range(0,len(b)):
    sumb=sumb+sum(b[i])
print(sumb)'''

#dense to sparse matrix

'''dense_matrix=[[0,9,0],[0,2,1],[1,0,0]]
def d_s(dm):
    sparse_matrix=[]
    for i in range(len(dm)):
        for j in range(len(dm[i])):
            if dm[i][j]!=0:
                sparse_matrix.append((i,j,dm[i][j]))
    return sparse_matrix
sparse_matrix1=[d_s(dense_matrix)]
for i in sparse_matrix1:
    print(f"{i[0][1]} {i[1][2]} {i[2]}")'''

# hackerrank contest question
# Input for first matrix
m, n = map(int, input().split())  
k = int(input())  
a = [int(x) for x in input().split()]  
asp = [a[i * 3:(i + 1) * 3] for i in range(k)]  # Convert to a list of triplets

# Input for second matrix
p, q = map(int, input().split())
l = int(input())  
b = [int(x) for x in input().split()]  
bsp = [b[i * 3:(i + 1) * 3] for i in range(l)] 

# Function to convert sparse matrix to dense matrix
def sparse_to_dense(matrix1, col, row):
    M = [[0 for x in range(col)] for x in range(row)]
    for (i, j, value) in matrix1:
        M[i][j] = value
    return M

# Convert sparse matrices to dense matrices
A = sparse_to_dense(asp, n, m)
B = sparse_to_dense(bsp, q, p)

# Function to print matrix
def print_list(matrix1, row, col):
    for i in range(row):
        for j in range(col):
            print(matrix1[i][j], end=" ")
        print()

# Check if multiplication is possible (n == p)
if n != p:
    print("Matrix multiplication not possible.")
else:
    # Initialize result matrix C with zeros (m x q)
    C = [[0 for _ in range(q)] for _ in range(m)]

    # Matrix multiplication logic
    for i in range(m):
        for j in range(q):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    # Print the result matrix C
    print_list(C, m, q)
m=2
q=2
C=[[14,0],[0,18]]
# DENSE TO SPARSE
z=sum(x.count(0) for x in C )
c=[]
def dense_to_sparse(matrix,row,col):
    for i in range(row):
        for j in range(col):
            if matrix[i][j]!=0:
                c.append((i,j,matrix[i][j]))
dense_to_sparse(C,m,q)

print(c)
    






